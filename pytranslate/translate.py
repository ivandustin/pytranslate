from pyllm import llm
from .constants import SPACE, EMPTY
from .encode import encode
from .join import join


def translate(language, definitions, words):
    text = join(SPACE, words)
    prompt = encode([definitions, {"text": text, language: EMPTY}])
    return llm(prompt)
