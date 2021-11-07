from enum import IntEnum


# allows us to use a word instead of a magic number
class DartMultiplier(IntEnum):
    MISS = 0
    SINGLE = 1
    DOUBLE = 2
    TREBLE = 3
