from .constants import SPACE, EMPTY
from .encode import encode
from .join import join


def to_prompt(language, dictionary, words):
    context = list(map(lambda word: dictionary[word], words))
    text = join(SPACE, words)
    return encode([context, {"text": text, language: EMPTY}])
