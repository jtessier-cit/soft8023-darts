from tinydb import TinyDB, Query

import random
import threading
import time


class DartsMatchDao:
    __instance = None

    # factory method to create an instance if there is none
    @staticmethod
    def get_instance():
        # check if there is an instance
        if DartsMatchDao.__instance is None:
            # using locking
            with threading.Lock():
                # check again if there is an instance
                if DartsMatchDao.__instance is None:  # Double locking mechanism
                    # create only if there is no instance
                    DartsMatchDao()
        # return the instance
        return DartsMatchDao.__instance

    def __init__(self):
        # should never be creating an instance if there is one
        if DartsMatchDao.__instance is not None:
            raise Exception("This is a singleton!")
        else:
            # set the class/instance variable __instance to the new object
            DartsMatchDao.__instance = self
        self.db = TinyDB('db.json')
        self.lock = threading.Lock()
        self.rand = random.random()

    def add(self, match):
        self.lock.acquire()
        print("locked in add")
        time.sleep(4)

        Match = Query()
        if not self.db.contains(Match.player1 == match.player1):
            self.db.insert({'type': match.type, 'player1': match.player1, 'player2': match.player2})

        print('Insert attempted on ' + match.player1 + '    ' + str(self.rand))

        self.lock.release()
        print("unlocked in add")
