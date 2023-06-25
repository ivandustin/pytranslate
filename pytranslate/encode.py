from multipledispatch import dispatch
from .constants import COLON, SPACE, NEWLINE
from .join import join


@dispatch(list)
def encode(xs):
    return join(NEWLINE * 2, map(encode, xs))


@dispatch(dict)
def encode(dictionary):
    return join(NEWLINE, [encode(key, value) for key, value in dictionary.items()])


@dispatch(str, str)
def encode(key, value):
    return encode(key) + COLON + SPACE + encode(value)


@dispatch(str)
def encode(string):
    return string.strip()
