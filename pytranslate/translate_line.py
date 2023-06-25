from functools import partial
from .get_definition import get_definition
from .normalize import normalize
from .read_file import read_file
from .translate import translate
from .constants import SPACE


def translate_line(definitions, language, line):
    words = normalize(line.split(SPACE))
    files = map(partial(get_definition, definitions), set(words))
    definitions = normalize(map(read_file, files))
    translation = translate(language, definitions, words)
    return translation
