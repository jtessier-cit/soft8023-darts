from enum import IntEnum


# allows us to use a word instead of a magic number
class DartMultiplier(IntEnum):
    MISS = 0
    SINGLE = 1
    DOUBLE = 2
    TREBLE = 3


# allows us to set multiple status values for matches
class MatchStatus(IntEnum):
    INVALID = 0
    WAITING = 1
    IN_PROGRESS = 2
    FINISHED = 3
