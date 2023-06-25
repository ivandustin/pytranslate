from .constants import UTF8


def read_file(filepath):
    return filepath.read_text(encoding=UTF8)
