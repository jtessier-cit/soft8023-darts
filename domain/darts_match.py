class DartsMatch:

    # constructor to create a typical darts match
    def __init__(self):
        self.active = True
        self.players = []
        self.last_player_index = -1
        self.visits = []
        self.winning_num_darts = -1
        self.winning_player_index = -1

    def register_player(self, username):
        # add if player not in list
        if username not in self.players:
            # player index will be same as the length of the list
            index = len(self.players)
            # append the player to the list of players
            self.players.append(username)
            return index
        else:
            # if player already in list, return -1 - error?
            return -1
