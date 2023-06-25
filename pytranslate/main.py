from functools import partial
from pyllm import llm
from .constants import ASTERISK, TXT, PROMPTS, MODEL
from .writelines import writelines
from .read_file import read_file
from .to_prompt import to_prompt
from .get_args import get_args
from .explode import explode
from .clean import clean
from .mkdir import mkdir
from .first import first


def main():
    args = get_args()
    input_dir = args.input
    language = args.language
    definitions = args.definitions
    mkdir(input_dir.parent / language)
    filepaths = list(input_dir.glob(ASTERISK + TXT))
    contents = map(read_file, filepaths)
    entries = map(lambda content: clean(content.splitlines()), contents)
    entries = list(
        map(lambda lines: list(map(lambda line: clean(explode(line)), lines)), entries)
    )
    words = set([word for entries in entries for words in entries for word in words])
    definitions = clean(
        map(
            read_file,
            map(lambda word: first(list(definitions.rglob(word + TXT))), words),
        )
    )
    dictionary = dict(zip(words, definitions))
    entries = map(
        lambda entry: list(map(partial(to_prompt, language, dictionary), entry)),
        entries,
    )
    entries = map(
        lambda prompts: (prompts, clean(map(partial(llm, model=MODEL), prompts))),
        entries,
    )
    for filepath, (prompts, lines) in zip(filepaths, entries):
        directory = filepath.parent.parent / language
        pfile = directory / (filepath.stem + PROMPTS + TXT)
        outfile = directory / filepath.name
        writelines(pfile, prompts)
        writelines(outfile, lines)
