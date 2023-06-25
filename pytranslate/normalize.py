from .identity import identity
from .strip import strip


def normalize(xs):
    return list(filter(identity, map(strip, xs)))
