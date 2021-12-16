import json

import pika as pika

from service.match_service import MatchVisitTemplate
from service.match_service import MatchManager
# Lab 03 add MatchStatus
from datatype.enums import DartMultiplier, MatchStatus

# CHECKOUTS = {
#     170: "T20 T20 Bull",
#     167: "T20 T19 Bull",
#     164: "T20 T18 Bull",
#     161: "T20 T17 Bull",
#     160: "T20 T20 D20",
#
#     136: "T20 T20 D8",
#
#     36: "D18"
# }

CHECKOUTS = {
    2: "D1",
    3: "1 D1",
    4: "D2",
    5: "3 D1",
    6: "D3",
    7: "5 D1",
    8: "D4",
    9: "5 D2",
    10: "D5",
    11: "3 D4",
    12: "D6",
    13: "3 D5",
    14: "D7",
    15: "3 D6",
    16: "D8",
    17: "3 D7",
    18: "D9",
    19: "3 D8",
    20: "D10",
    21: "1 D10",
    22: "D11",
    23: "5 D9",
    24: "D12",
    25: "3 D11",
    26: "D13",
    27: "3 D12",
    28: "D14",
    29: "1 D14",
    30: "D15",
    31: "3 D14",
    32: "D16",
    33: "3 D15",
    34: "D17",
    35: "7 D14",
    36: "D18",
    37: "5 D16",
    38: "D19",
    39: "1 D19",
    40: "D20",
    41: "3 D19",
    42: "4 D19",
    43: "5 D19",
    44: "6 D19",
    45: "7 D19",
    46: "8 D19",
    47: "9 D19",
    48: "10 D19",
    49: "11 D19",
    50: "12 D19",
    51: "13 D19",
    52: "12 D20",
    53: "15 D19",
    54: "14 D20",
    55: "15 D20",
    56: "16 D20",
    57: "17 D20",
    58: "18 D20",
    59: "19 D20",
    60: "20 D20",
    61: "3 20 D19",
    62: "16 8 D19",
    63: "14 9 D20",
    64: "9 15 D20",
    65: "7 18 D20",
    66: "6 20 D20",
    67: "13 16 D19",
    68: "11 19 D19",
    69: "10 19 D20",
    70: "10 20 D20",
    71: "14 19 D19",
    72: "18 16 D19",
    73: "17 18 D19",
    74: "16 18 D20",
    75: "15 20 D20",
    76: "20 16 D20",
    77: "17 20 D20",
    78: "18 20 D20",
    79: "19 20 D20",
    80: "20 20 D20",
    81: "D19 3 D20",
    82: "D19 4 D20",
    83: "5 D20 D19",
    84: "6 D20 D19",
    85: "7 D19 D20",
    86: "D20 8 D19",
    87: "9 D19 D20",
    88: "D20 10 D19",
    89: "11 D19 D20",
    90: "12 D19 D20",
    91: "13 D19 D20",
    92: "D19 14 D20",
    93: "15 D19 D20",
    94: "16 D20 D19",
    95: "17 D20 D19",
    96: "D20 18 D19",
    97: "19 D20 D19",
    98: "D20 20 D19",
    99: "19 D20 D20",
    100: "20 D20 D20",
    101: "6 T19 D19",
    102: "D20 D12 D19",
    103: "5 T20 D19",
    104: "9 T19 D19",
    105: "T20 5 D20",
    106: "D14 D19 D20",
    107: "T19 12 D19",
    108: "D19 D20 D15",
    109: "T20 9 D20",
    110: "T19 13 D20",
    111: "16 T19 D19",
    112: "D19 D20 D17",
    113: "T19 18 D19",
    114: "T19 19 D19",
    115: "T19 18 D20",
    116: "16 T20 D20",
    117: "19 T20 D19",
    118: "18 T20 D20",
    119: "19 T20 D20",
    120: "T20 20 D20",
    121: "T19 D19 D13",
    122: "D20 T20 D11",
    123: "T19 D19 D14",
    124: "D20 T20 D12",
    125: "D15 T19 D19",
    126: "T20 D19 D14",
    127: "D15 T19 D20",
    128: "D15 T20 D19",
    129: "D17 T19 D19",
    130: "T20 D15 D20",
    131: "T19 D17 D20",
    132: "T20 D17 D19",
    133: "D18 T19 D20",
    134: "D18 T20 D19",
    135: "T19 D20 D19",
    136: "D18 T20 D20",
    137: "T19 D20 D20",
    138: "T20 D19 D20",
    139: "T19 T14 D20",
    140: "T20 D20 D20",
    141: "T19 T20 D12",
    142: "T20 T14 D20",
    143: "T15 T20 D19",
    144: "T20 T18 D15",
    145: "T15 T20 D20",
    146: "T16 T20 D19",
    147: "T20 T19 D15",
    148: "T20 T16 D20",
    149: "T20 T19 D16",
    150: "T20 T18 D18",
    151: "T20 T19 D17",
    152: "T20 T18 D19",
    153: "T20 T19 D18",
    154: "T20 T18 D20",
    155: "T20 T19 D19",
    156: "T20 T20 D18",
    157: "T20 T19 D20",
    158: "T20 T20 D19",
    159: "No checkout",
    160: "T20 T20 D20",
    161: "T20 T17 Bull",
    162: "No checkout",
    163: "No checkout",
    164: "T20 T18 Bull",
    165: "No checkout",
    166: "No checkout",
    167: "T20 T19 Bull",
    168: "No checkout",
    169: "No checkout",
    170: "T20 T20 Bull"
}

# STARTING_TOTAL = 501

class X01Match(MatchManager, MatchVisitTemplate):

    # def __init__(self, starting_total=501):
    def __init__(self, starting_total=501):
        super().__init__()
        # self._starting_total = starting_total
        self._starting_total = starting_total
        self.scores = []  # list of scores remaining parallel to players
        self.averages = []  # single-dart average (x 3 for 3-dart average)
        self.first9 = []  # average for first 9 darts

    # This has the potential to be buggy if the match is set first and players registered after
    def post_init(self):
        for i in range(0, len(self.match.players)):
            self.scores.append(self._starting_total)  # Might want to parameterize the starting total
            self.first9.append(None)
            self.averages.append(None)
        # match is in progress after initializing
        self.match.status = MatchStatus.IN_PROGRESS

    def validate_visit(self, player_index, visit):
        # if the last player is the same as the current player, visit isn't valid (out of turn)
        if self.match.last_player_index is player_index:  # Note: this won't work properly for 3 players...
            return False, "Player " + str(player_index + 1) + " is not in the correct sequence. Visit ignored."

        # if the match status is not active, visit isn't valid (inactive game)
        if self.match.status != MatchStatus.IN_PROGRESS:
            return False, "Game has ended."
        # print(str(self.match.last_Player_index) + "-" + str(player_index))
        # advance the last player index - player's turn will proceed
        self.match.last_player_index = player_index
        return True, None


    def check_winning_condition(self, player_index, visit):
        """returns 1, 2 or 3 for when a dart closes the game / leg (i.e. finishing double) or 0 if not closed out

        :param player_index: position of player details in various lists
        :param visit: a list of 3 Darts (each containing multiplier and segment)
        :return: 0, 1, 2 or 3
        """
        i = 0

        # loop over the darts in the visit
        for dart in visit.darts:
            i = i + 1
            # if the dart is a double and the score for the dart would make the score 0
            if dart.multiplier == DartMultiplier.DOUBLE and self.scores[player_index] - dart.get_score() == 0:
                # game, shot!
                self.scores[player_index] = 0  # set the player's score to 0
                self.match.status = MatchStatus.FINISHED  # game is no longer active
                return i  # return the dart number
            else:
                print("deducting for " + str(player_index))
                self.scores[player_index] -= dart.get_score()  # reduce the player's score

        return 0  # return 0 - game isn't done

    def record_statistics(self, player_index, visit, result):
        """Store stats both for in-memory immediate use and on disk for later recall

        :return:
        """
        if result != 0:
            # result was 1 2 or 3 (which dart ended the game)
            # so this removes the remaining darts from the visit
            visit.remove_trailing_darts(result)  # a double finished the game, so ignore any subsequent darts

        # adds the visit to the player's visits
        self.match.visits[player_index].append(visit)

        # Calculate first 9 if, and only if, this is the 3rd visit
        if len(self.match.visits[player_index]) == 3:
            # subtract the remaining score from starting score and / 3 to get average?
            # check logic, why /  3?
            self.first9[player_index] = (self._starting_total - self.scores[player_index]) / 3

        # Calculate single-dart average taking account of a double being hit with dart 1 or 2 when checking out
        # player threw 3 darts per visit unless on the winning one
        num_darts_thrown = (len(self.match.visits[player_index]) - 1) * 3
        num_darts_thrown += 3 if result == 0 else result  # add 3 or whatever the result was (# darts thrown)

        # if winning visit we can complete the stats for the visit/match
        if result != 0:
            self.match.winning_num_darts = num_darts_thrown
            self.match.winning_player_index = player_index

        # set averages for player
        self.averages[player_index] = (self._starting_total - self.scores[player_index]) / num_darts_thrown

        # send a message using RabbitMQ - note this is too implementation specific and should be abstracted, i.e. move
        # rabbitmq specific code to a separate service layer class
        # Let's do something simple - store the darts so a lifetime 3-dart average can be calculated; this is something
        # of a lower priority than the ongoing match, so can be backgrounded / temporally-decoupled somewhat with a
        # message queue (handle load better).
        # We will need to serialize the darts list - JSON is very suitable for this

        username = self.match.players[player_index]
        match_type = "X01"
        darts = []
        for dart in visit.darts:
            darts.append([dart.multiplier, dart.segment])
        message = [username, match_type, darts]
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # we could parameterize the host
        channel = connection.channel()
        channel.queue_declare(queue='player-stats')
        channel.basic_publish(exchange='',
                              routing_key='player-stats',
                              body=json.dumps(message))
        connection.close()

    def format_summary(self, player_index, visit):
        # Include suggested checkout if remaining score can be checked out in 3 darts
        summary = "Last visit was by " + self.match.players[player_index] + " with " + visit.to_string() + "\n"

        # if the game was won, can add winning portion to summary
        if self.match.winning_player_index != -1:
            summary += self.match.players[self.match.winning_player_index] + " wins in "\
                      + str(self.match.winning_num_darts) + " darts\n"

        # start at 0 for stats[i]
        i = 0
        for player in self.match.players:
            summary = summary + player + ": " + str(self.scores[i]) + " Remaining"
            if self.scores[i] in CHECKOUTS.keys():
                summary += " (" + CHECKOUTS.get(self.scores[i]) + ")"
            if self.first9[i]:
                summary += "\n - [First 9 Avg: " + '{0:.2f}'.format(self.first9[i]) + "] "
            if self.averages[i]:
                summary += "\n - [3-dart Avg: " + '{0:.2f}'.format(self.averages[i] * 3) + "] "
            i = i + 1
            summary += "\n"
        return summary


class X01MatchBuilder:
    """
    This could be extended to include dynamic key-value pair parameters (see object_factory.py),
    or make it a singleton, etc.
    """
    def __init__(self):
        pass

    # def __call__(self, starting_total):
    def __call__(self, **kwargs):

        # return X01Match(starting_total)
        return X01Match(**kwargs)