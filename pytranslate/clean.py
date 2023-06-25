from .identity import identity
from .strip import strip


def clean(xs):
    return list(filter(identity, map(strip, xs)))
