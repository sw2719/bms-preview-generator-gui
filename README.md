# Overview
This is a GUI frontend for [MikiraSora's BmsPreviewAudioGenerator](https://github.com/MikiraSora/BmsPreviewAudioGenerator).

[한국어 설명은 여기 (Click here for a Korean README)](README_ko.md)

# Features
* Generate preview audio files of multiple BMS directories with single click, without copy-pasting and editing commands.
* ...and that's pretty much it.

# Usage
1. Download [BmsPreviewAudioGenerator](https://github.com/MikiraSora/BmsPreviewAudioGenerator/releases/latest) and [this program](https://github.com/sw2719/bms-preview-generator-gui/releases/latest).
    - .NET Core 3.1 is required for BmsPreviewAudioGenerator. If you don't have it installed, you can download it [here](https://dotnet.microsoft.com/download/dotnet-core/3.1).
2. Unzip this program first.
3. Unzip BmsPreviewAudioGenerator folder inside program directory (where BmsPreviewAudioGeneratorGUI.exe is located).
    - The BmsPreviewAudioGenerator folder should be inside the program directory, not its contents.
4. Run BmsPreviewAudioGeneratorGUI.exe.
5. Add directories containg BMS. You can just drag and drop folders inside the directory list. Alternatively, click 'Add' button to open folder dialog if you prefer it that way.
   - Preview audio files are generated in parallel, so spliting directories as much as possible is recommended to speed up the generation.
6. Adjust generator options if needed, and click 'Start' button.
