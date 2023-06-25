from functools import partial
from .translate_line import translate_line
from .normalize import normalize
from .read_file import read_file
from .constants import UTF8


def translate_file(definitions, language, filepath):
    lines = normalize(read_file(filepath).splitlines())
    translations = map(partial(translate_line, definitions, language), lines)
    output = filepath.parent.parent / language / filepath.name
    with open(output, "w", encoding=UTF8) as file:
        file.writelines(translations)
