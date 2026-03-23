import pefile
from packaging import version


def get_file_version(file_path: str) -> version.Version:
    pe = pefile.PE(file_path)
    version_info = pe.VS_FIXEDFILEINFO[0]
    pe.close()
    return version.Version(f"{version_info.FileVersionMS >> 16}.{version_info.FileVersionMS & 0xFFFF}.{version_info.FileVersionLS >> 16}.{version_info.FileVersionLS & 0xFFFF}")
