from .constants import UTF8


def writelines(filepath, lines):
    with open(filepath, "w", encoding=UTF8) as file:
        file.writelines(lines)
