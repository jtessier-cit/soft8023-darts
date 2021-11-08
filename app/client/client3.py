import logging

import grpc

import darts_match_pb2 as darts_match_pb2
import darts_match_pb2_grpc as darts_match_pb2_grpc
from datatype.enums import DartMultiplier


def run():
    channel = grpc.insecure_channel('127.0.0.1:50055')
    stub = darts_match_pb2_grpc.DartsMatchStub(channel)

    # Let's create 2 501 darts matches

    match1 = stub.CreateMatch(darts_match_pb2.MatchRequest(userName='Alice', matchType='X01')).matchId
    m1_player1 = 0   # owning player always 0
    m1_player2 = stub.RegisterPlayer(darts_match_pb2.RegisterRequest(matchId=match1, userName='Jamal')).playerIndex
    # player3 = stub.RegisterPlayer(darts_match_pb2.RegisterRequest(matchId=match1, userName='Eddie')).playerIndex
    stub.FinalizeMatch(darts_match_pb2.FinalizeRequest(matchId=match1))

    match2 = stub.CreateMatch(darts_match_pb2.MatchRequest(userName='Bobby', matchType='X01')).matchId
    m2_player1 = 0   # owning player always 0
    m2_player2 = stub.RegisterPlayer(darts_match_pb2.RegisterRequest(matchId=match2, userName='Norris')).playerIndex
    # player3 = stub.RegisterPlayer(darts_match_pb2.RegisterRequest(matchId=match1, userName='Eddie')).playerIndex
    stub.FinalizeMatch(darts_match_pb2.FinalizeRequest(matchId=match2))

    match3 = stub.CreateMatch(darts_match_pb2.MatchRequest(userName='Yellow', matchType='X01')).matchId
    m3_player1 = 0   # owning player always 0
    m3_player2 = stub.RegisterPlayer(darts_match_pb2.RegisterRequest(matchId=match3, userName='Blue')).playerIndex
    stub.FinalizeMatch(darts_match_pb2.FinalizeRequest(matchId=match3))


    # Simultaneous matches - we are simulating 4 clients (2 matches by 2 players)

    # match 1 player 1
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player1, visit=my_visit))
    print(response.message)

    response = stub.WhatIsLeft(darts_match_pb2.LeftRequest(matchId=match1, playerIndex=m1_player1))
    print(response)


    # match 2 player 1
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=10),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=15),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match2, playerIndex=m2_player1, visit=my_visit))
    print(response.message)

    # match 3 player 1
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match3, playerIndex=m3_player1, visit=my_visit))
    print(response.message)

    # match 1 player 2
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=2)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player2, visit=my_visit))
    print(response.message)

    # match 1 player 1
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=10),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player1, visit=my_visit))
    print(response.message)

    # match 1 player 2
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player2, visit=my_visit))
    print(response.message)

    # match 2 player 2
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match2, playerIndex=m2_player2, visit=my_visit))
    print(response.message)

    # match 3 player 2
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match3, playerIndex=m3_player2, visit=my_visit))
    print(response.message)

    # match 3 player 1
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match3, playerIndex=m3_player1, visit=my_visit))
    print(response.message)

    # match 3 player 2
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match3, playerIndex=m3_player2, visit=my_visit))
    print(response.message)

    # match 1 player 1
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player1, visit=my_visit))
    print(response.message)

    # match 2 player 1
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=10),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=15),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match2, playerIndex=m2_player1, visit=my_visit))
    print(response.message)


    # match 1 player 2
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=2)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player2, visit=my_visit))
    print(response.message)


    # match 1 player 1
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=10),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player1, visit=my_visit))
    print(response.message)

    # match 1 player 2
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player2, visit=my_visit))
    print(response.message)

    # match 2 player 2
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match2, playerIndex=m2_player2, visit=my_visit))
    print(response.message)

    # match 3 player 1
    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=19),
                darts_match_pb2.Dart(multiplier=DartMultiplier.DOUBLE, segment=12)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match3, playerIndex=m3_player1, visit=my_visit))
    print(response.message)

if __name__ == '__main__':
    logging.basicConfig()
    run()
