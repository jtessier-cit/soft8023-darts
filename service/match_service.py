from abc import ABC, abstractmethod


class MatchManager(ABC):

    def __init__(self):
        self.match = None

    def set_match(self, match):
        self.match = match
        # self.post_init()    # initialise whatever is specific to the match type

    def end_match(self):
        self.match.status = False

    def finalize_setup(self):
        """When the last player has been registered and the match is ready to go, do some final initialisation
        Note: I'm still not happy the way this works (has to do with darts_match as a generic domain object versus match
        management here abstracted and then implemented in concrete match classes)
        :return:
        """
        self.post_init()

    @abstractmethod
    def post_init(self):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass


class MatchVisitTemplate(ABC):

    # the rules for a match visit
    def process_visit(self, player_index, visit):
        """returns result (0 meaning game goes on, >0 meaning a dart finished the game), response (info messages)
        Skeleton of operations to perform. DON'T override me.

        The Template Method defines a skeleton of an algorithm in an operation,
        and defers some steps to subclasses.
        """

        # player index is from the list of players
        # visit object includes darts

        # returns 0, with message if status is false
        status, message = self.validate_visit(player_index, visit)
        if status is False:
            return -1, message

        # performs these steps if the status is not False

        # checks the winning condition to see if the game is over
        # result stores which, if any, of the darts closed out the game
        result = self.check_winning_condition(player_index, visit)

        # records statistics for the visit
        self.record_statistics(player_index, visit, result)

        # Note: this violates the separation of concerns principle (we are mixing presentation logic in
        # with service / business logic - we should refactor, especially if we move to a GUI front-end
        return result, self.format_summary(player_index, visit)

    @abstractmethod
    def validate_visit(self, player_index, visit):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def check_winning_condition(self, player_index, visit):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def record_statistics(self, player_index, visit, result):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def format_summary(self, player_index, visit):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass
