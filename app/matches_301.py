import pattern.object_factory as object_factory
import app.gameimpl.x01_match as x01_match
import domain.darts_match as darts_match
from datatype.enums import DartMultiplier
from domain import visit

# create the factory
factory = object_factory.ObjectFactory()
# register the builder for X01 game type
factory.register_builder('X01', x01_match.X01MatchBuilder())

config = {
    'starting_total': 301
}

# get a reference to the factory
x01 = factory.create('X01', **config)
# create a darts match
match = darts_match.DartsMatch()

# create players in the match
player1_index = match.register_player('Yellow')
player2_index = match.register_player('Blue')

x01.set_match(match)

# 30 - Yellow
my_visit = visit.Visit([(DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 5), (DartMultiplier.SINGLE, 5)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

# 26 - Blue
my_visit = visit.Visit([(DartMultiplier.SINGLE, 1), (DartMultiplier.SINGLE, 5), (DartMultiplier.SINGLE, 20)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)

# 135 - Yellow
my_visit = visit.Visit([(DartMultiplier.TREBLE, 20), (DartMultiplier.TREBLE, 20), (DartMultiplier.TREBLE, 5)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

# 46 - Blue
my_visit = visit.Visit([(DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 19), (DartMultiplier.SINGLE, 20)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)

# 81 - Yellow
my_visit = visit.Visit([(DartMultiplier.SINGLE, 20), (DartMultiplier.TREBLE, 20), (DartMultiplier.SINGLE, 1)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

# 123 - Blue
my_visit = visit.Visit([(DartMultiplier.TREBLE, 20), (DartMultiplier.TREBLE, 20), (DartMultiplier.TREBLE, 3)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)

# 30 - Yellow
my_visit = visit.Visit([(DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 10), (DartMultiplier.MISS, 0)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

# 58 - Blue
my_visit = visit.Visit([(DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 1)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)

# 25 - Yellow
my_visit = visit.Visit([(DartMultiplier.SINGLE, 9), (DartMultiplier.DOUBLE, 8), (DartMultiplier.SINGLE, 0)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

# This should trigger an error message and the visit ignored
my_visit = visit.Visit([(DartMultiplier.SINGLE, 10), (DartMultiplier.DOUBLE, 18), (DartMultiplier.SINGLE, 20)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)
