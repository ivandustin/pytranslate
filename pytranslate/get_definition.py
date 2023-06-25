from .constants import TXT
from .first import first


def get_definition(directory, word):
    return first(list(directory.rglob(word + TXT)))
