from functools import partial
from .translate_file import translate_file
from .get_args import get_args
from .mkdir import mkdir


def main():
    args = get_args()
    input_dir = args.input
    language = args.language
    definitions = args.definitions
    mkdir(input_dir.parent / language)
    filepaths = input_dir.glob("*.txt")
    list(map(partial(translate_file, definitions, language), filepaths))
