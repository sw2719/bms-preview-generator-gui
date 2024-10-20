# nuitka-project: --standalone
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --windows-console-mode=disable

import sys
import os
import re
import shlex
import argparse
import threading
import time
import zipfile
import requests

from functools import partial
from typing import Dict, List

from packaging import version
from pefile import PE
from pypdl import Pypdl
from pypdl.utls import default_logger

from PySide6.QtCore import Qt, QProcess, QLibraryInfo, QTranslator, QLocale, QThread, Signal, QIODevice, QFile, QTextStream
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QMessageBox, QFileDialog, QWidget, QProgressDialog
import qdarktheme

from ui.ui_main import Ui_MainWindow
from ui.ui_about import Ui_AboutForm
from ui.ui_license import Ui_LicenseForm

import resources  # noqa
from util.github import get_latest_release

VERSION = '0.2.0'
CHECK_API_URL = 'https://api.github.com/repos/sw2719/bms-preview-generator-gui/releases/latest'
RELEASES_URL = 'https://github.com/sw2719/bms-preview-generator-gui/releases'
REPO_URL = 'https://github.com/sw2719/bms-preview-generator-gui'

DEFAULT_START = '20000'
DEFAULT_END = '40000'
DEFAULT_FADE_IN = '1000'
DEFAULT_FADE_OUT = '2000'
DEFAULT_FILE_NAME = "preview_auto_generated.ogg"
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
CORE_COUNT = os.cpu_count()


# WIP
class Generator:
    def __init__(self, path: str, version: str):
        self.path = path
        self.version = version


class UpdateThread(QThread):
    completed = Signal(bool, str, Exception)

    def run(self):
        try:
            response = requests.get(CHECK_API_URL)
            response.raise_for_status()
            data = response.json()
            new_version = data['tag_name']
            self.completed.emit(True, new_version, None)

        except (requests.RequestException, requests.JSONDecodeError) as e:
            self.completed.emit(False, "", e)


class ExtractThread(QThread):
    completed = Signal(bool)

    def __init__(self, path: str, **kwargs):
        super().__init__(**kwargs)
        self.path = path

    def run(self):
        print('Extract thread start')
        while True:
            try:
                with zipfile.ZipFile(self.path, 'r') as zip_ref:
                    zip_ref.extractall(f"{CURRENT_PATH}/BmsPreviewAudioGenerator/")

                os.remove(self.path)
                break

            except zipfile.BadZipFile:
                time.sleep(1)
                continue

        self.completed.emit(True)


class BmsPreviewAudioGeneratorGUI(QApplication):
    def __init__(self, nocheck: bool, language: None | str):
        super().__init__(sys.argv)
        qdarktheme.setup_theme("auto")

        path = QLibraryInfo.path(QLibraryInfo.TranslationsPath)
        translator = QTranslator(self)

        if translator.load(QLocale.system(), 'qtbase', '_', path):
            self.installTranslator(translator)

        path = ':/translations'
        translator = QTranslator(self)

        if language is None:
            language = QLocale.system()

        if translator.load(language, 'bmsgui', '_', path):
            self.installTranslator(translator)

        self.threads = []

        self.main_window = QMainWindow()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.setWindowTitle(self.main_window.windowTitle() + f' (Version {VERSION})')

        self.directories: List[str] = []
        self.processes: List[QProcess] = []

        self.ui.output_textedit.setReadOnly(True)

        self.about_window = QWidget(self.main_window, Qt.WindowType.Window)
        about_ui = Ui_AboutForm()
        about_ui.setupUi(self.about_window)
        about_ui.version_label.setText(self.tr('Version {0}').format(VERSION))

        self.license_window = QWidget(self.about_window, Qt.WindowType.Window)
        license_ui = Ui_LicenseForm()
        license_ui.setupUi(self.license_window)

        about_ui.github_button.clicked.connect(lambda: os.startfile(REPO_URL))
        about_ui.license_button.clicked.connect(self.license_window.show)

        path = ":/ui/about_license.txt"
        f = QFile(path)
        if f.open(QIODevice.ReadOnly | QFile.Text):
            text = QTextStream(f).readAll()
            license_ui.about_textedit.setText(text)
            f.close()

        self.ui.action_check_update.triggered.connect(self.check_for_updates)
        self.ui.action_about.triggered.connect(self.about_window.show)
        self.ui.action_exit.triggered.connect(self.exit)

        self.ui.add_button.clicked.connect(self.add_directory_ui)
        self.ui.add_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.ui.remove_button.clicked.connect(self.remove_directory)
        self.ui.remove_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.ui.dir_listwidget.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.ui.dir_listwidget.currentItemChanged.connect(self.update_button_status)
        self.ui.dir_listwidget.fileDropped.connect(self.add_directories)

        self.ui.action_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ui.action_button.setEnabled(False)
        self.ui.action_button.clicked.connect(self.start)

        self.ui.thread_auto_checkbox.clicked.connect(
            self.on_thread_auto_checkbox)

        self.ui.start_edit.setText(DEFAULT_START)
        self.ui.end_edit.setText(DEFAULT_END)
        self.ui.fade_in_edit.setText(DEFAULT_FADE_IN)
        self.ui.fade_out_edit.setText(DEFAULT_FADE_OUT)
        self.ui.filename_edit.setText(DEFAULT_FILE_NAME)
        self.ui.thread_spinbox.setValue(CORE_COUNT)
        self.ui.param_edit.setText('')

        self.ui.progressbar.hide()
        self.ui.progress_label.hide()

        self.main_window.show()

        self.generator = None
        self.get_generator()

        if nocheck:
            self.print(self.tr('nocheck is enabled.'))

        if not self.generator and not nocheck:
            msgbox = QMessageBox(parent=self.main_window)
            msgbox.setIcon(QMessageBox.Icon.Warning)

            msgbox.setText(self.tr(
                "BmsPreviewAudioGenerator.exe not found. Download now?"))
            msgbox.setInformativeText(self.tr(
                "BmsPreviewAudioGenerator.exe is required to generate audio previews."))
            msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            if msgbox.exec() == QMessageBox.StandardButton.Yes:
                self.download_generator()

    def print(self, text: str):
        self.ui.output_textedit.appendPlainText(text)

    def clear(self):
        self.ui.output_textedit.clear()

    def get_generator(self) -> str | None:
        # TODO: Get program version
        for directory in os.listdir(CURRENT_PATH):
            if os.path.isdir(directory) and 'BmsPreviewAudioGenerator.exe' in os.listdir(directory):
                path = os.path.join(directory, 'BmsPreviewAudioGenerator.exe')
                print(path)
                self.generator = path
                self.print(self.tr('Found BmsPreviewAudioGenerator.exe at {0}').format(self.generator))

        else:
            return None

    def download_generator(self):
        try:
            release = get_latest_release()

        except requests.HTTPError:
            QMessageBox.critical(self.main_window, self.tr('Error'), self.tr('Failed to download BmsPreviewAudioGenerator.\nPlease try again or manually download.'))
            sys.exit(1)

        file_name = release['asset_name']
        url = release['asset_url']

        progress = QProgressDialog(self.tr("Downloading {0}...".format(file_name)), "", 0, 100, parent=self.main_window)
        progress.setWindowModality(Qt.WindowModal)
        progress.setCancelButton(None)
        progress.forceShow()

        dl = Pypdl(allow_reuse=False, logger=default_logger("Pypdl"))
        dl.start(
            url=url,
            file_path=CURRENT_PATH,
            segments=4,
            display=False,
            multisegment=False,
            block=False,
            retries=0,
            mirror_func=None,
            etag=True,
            overwrite=True
        )

        # print the progress
        while dl.progress < 100:
            progress.setValue(dl.progress)
            if progress.wasCanceled():
                dl.stop()
                sys.exit()

        progress.setValue(99)
        progress.setLabelText(self.tr("Extracting..."))

        def on_extract_finish():
            nonlocal progress
            nonlocal extract_thread

            # do cleanup stuff
            progress.accept()
            self.threads.remove(extract_thread)
            extract_thread.deleteLater()
            self.get_generator()

        extract_thread = ExtractThread(f"{CURRENT_PATH}/{file_name}")
        extract_thread.completed.connect(on_extract_finish)
        extract_thread.start()

        self.threads.append(extract_thread)

    def check_for_updates(self):
        update_thread = UpdateThread(self)

        def on_check_complete(check_success, new_version, exc):
            if check_success:
                if version.parse(new_version) > version.parse(VERSION):
                    reply = QMessageBox.question(self.main_window, self.tr('Update available'),
                                                 self.tr('New version {0} is available. Open the release page?').format(new_version),
                                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                    if reply == QMessageBox.StandardButton.Yes:
                        os.startfile(RELEASES_URL)
                else:
                    QMessageBox.information(self.main_window, self.tr('No updates available'), self.tr('You are using the latest version.'))
            else:
                exception_string = str(exc)
                QMessageBox.critical(self.main_window, self.tr('Failed to check for updates'), self.tr("Failed to check for updates:\n{0}").format(exception_string))

        update_thread.completed.connect(on_check_complete)
        update_thread.start()

    def update_button_status(self):
        if self.ui.dir_listwidget.currentItem():
            self.ui.remove_button.setEnabled(True)
        else:
            self.ui.remove_button.setEnabled(False)

        if self.ui.dir_listwidget.count():
            self.ui.action_button.setEnabled(True)
        else:
            self.ui.action_button.setEnabled(False)

    def remove_directory(self):
        current_item = self.ui.dir_listwidget.currentItem()
        if current_item:
            self.directories.remove(current_item.text())
            self.ui.dir_listwidget.takeItem(self.ui.dir_listwidget.currentRow())

        self.update_button_status()

    def add_directories(self, directories: List[str]):
        for directory in directories:
            if os.path.isdir(directory) and directory not in self.directories:
                self.directories.append(directory)
                self.ui.dir_listwidget.addItem(directory)
            elif not os.path.isdir(directory):
                self.print(self.tr('Failed to add {0}: This is not a directory.').format(directory))
            elif directory in self.directories:
                self.print(self.tr('Failed to add {0}: This directory is already added.').format(directory))
            else:
                self.print(self.tr('Failed to add {0}: Unknown error.').format(directory))

        self.update_button_status()

    def add_directory_ui(self):
        directory = QFileDialog.getExistingDirectory(self.main_window, self.tr('Select a directory'))
        if directory:
            self.add_directories([directory])

    def start(self):
        if not self.generator:
            self.print(self.tr('Unable to generate because BmsPreviewAudioGenerator.exe was not found.'))
            return

        self.clear()
        self.ui.dir_listwidget.setAcceptDrops(False)
        self.ui.dir_listwidget.currentItemChanged.disconnect(self.update_button_status)
        self.ui.dir_listwidget.setSelectionMode(QListWidget.SelectionMode.NoSelection)

        self.ui.start_edit.setEnabled(False)
        self.ui.end_edit.setEnabled(False)
        self.ui.fade_in_edit.setEnabled(False)
        self.ui.fade_out_edit.setEnabled(False)
        self.ui.filename_edit.setEnabled(False)
        self.ui.param_edit.setEnabled(False)

        self.ui.progressbar.setMaximum(0)
        self.ui.progressbar.show()
        self.ui.progress_label.setText(f"1/{len(self.directories)}")
        self.ui.progress_label.show()
        progress_pattern = r'(\d+\/\d+)\s+\((\d+\.\d+%)\)'

        def read_output(process: QProcess, item_index: int):
            data = process.readAllStandardOutput().data()
            decoded_string = data.decode('mbcs')

            self.print(decoded_string)
            self.ui.output_textedit.verticalScrollBar().setValue(self.ui.output_textedit.verticalScrollBar().maximum())

            progress = re.search(progress_pattern, decoded_string)
            if progress:
                item_progress = progress.group(1).split('/')  # format: done/total
                done = int(item_progress[0])
                total = int(item_progress[1])

                if not self.ui.progressbar.maximum():
                    self.ui.progressbar.setMaximum(total)

                self.ui.progressbar.setValue(done)

        def on_finish(path: str, exit_code, _):
            if exit_code:
                self.print(f'Preview generation of {path} failed.')
            else:
                self.print(f'Preview generation of {path} finished.')

            process = self.processes.pop(0)
            process.close()
            process.deleteLater()

            self.ui.dir_listwidget.takeItem(0)

            if self.processes:
                self.ui.progressbar.setMaximum(0)
                self.ui.progress_label.setText(f"{len(self.directories) - len(self.processes) + 1}/{len(self.directories)}")
                self.print(f'Start process: {self.generator} {" ".join(self.processes[0].arguments())}')
                self.processes[0].start()
            else:  # All processes are finished
                self.directories.clear()

                self.ui.dir_listwidget.clear()
                self.ui.dir_listwidget.setAcceptDrops(True)
                self.ui.dir_listwidget.currentItemChanged.connect(self.update_button_status)
                self.ui.dir_listwidget.setSelectionMode(QListWidget.SelectionMode.NoSelection)

                self.ui.start_edit.setEnabled(True)
                self.ui.end_edit.setEnabled(True)
                self.ui.fade_in_edit.setEnabled(True)
                self.ui.fade_out_edit.setEnabled(True)
                self.ui.filename_edit.setEnabled(True)
                self.ui.param_edit.setEnabled(True)

                self.ui.action_button.show()
                self.ui.action_button.setEnabled(False)
                self.ui.add_button.setEnabled(True)
                self.ui.progressbar.hide()
                self.ui.progress_label.hide()

        for index, directory in enumerate(self.directories):
            arg_dir = os.path.abspath(directory).replace('\\', '/')
            start = self.ui.start_edit.text()
            end = self.ui.end_edit.text()
            fade_in = self.ui.fade_in_edit.text()
            fade_out = self.ui.fade_out_edit.text()
            save_name = self.ui.filename_edit.text()

            arguments = [
                '-batch',
                f'-path="{arg_dir}"',
                f'-start="{start}"',
                f'-end="{end}"',
                f'-save_name="{save_name}"',
                '-support_extend_format',
                f'-fade_in="{fade_in}"',
                f'-fade_out="{fade_out}"',
                f'-thread={self.ui.thread_spinbox.value()}'
            ]

            arguments = arguments + shlex.split(self.ui.param_edit.text())

            process = QProcess(parent=self.main_window)
            process.setProgram(self.generator)
            process.setNativeArguments(' '.join(arguments))

            process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
            process.readyReadStandardOutput.connect(partial(read_output, process, index))
            process.finished.connect(partial(on_finish, str(directory)))

            self.processes.append(process)

        self.ui.action_button.hide()
        self.ui.add_button.setEnabled(False)
        self.ui.remove_button.setEnabled(False)

        self.print(f'Start process: {self.generator} {" ".join(self.processes[0].arguments())}')
        self.processes[0].start()

    def on_thread_auto_checkbox(self):
        self.ui.thread_spinbox.setReadOnly(self.ui.thread_auto_checkbox.isChecked())
        if self.ui.thread_auto_checkbox.isChecked():
            self.ui.thread_spinbox.setValue(CORE_COUNT)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nocheck', action='store_true', help='Do not check for BmsPreviewAudioGenerator.exe')
    parser.add_argument('-l', '--lang', help='Force language', required=False, default=None)
    args = parser.parse_args()
    bms_gui = BmsPreviewAudioGeneratorGUI(args.nocheck, args.lang)
    sys.exit(bms_gui.exec())


if __name__ == '__main__':
    main()