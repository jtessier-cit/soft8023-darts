#!/usr/bin/env python
"""
Simple 1-to-1 Producer-Consumer pattern. See the record_statistics function in x01_match.py from the producer.

There is also an opportunity to make use of a factory pattern here to process how dart stats are handled per game type.

What we will do is to use a simple DAO to store the running total of scores for all darts thrown and use this to
calculate an overall average. Very simple stat, but this could be expanded significantly to include all important stats.

Instructions: run the server, run client1.py and quickly run this script and see it wait for new messages. You will see
debug output to the console, but also watch the player_stats.json file in the same folder as this script - it will
continually update as new matches are started, new visits happen, ad infinitum (hopefully).
"""
import json
import os
import sys

import pika

from dao import player_stats_dao_thread_safe_singleton


def callback(ch, method, properties, body):
    dao = player_stats_dao_thread_safe_singleton.PlayerStatsDao.get_instance()
    print(" [x] Received %r" % json.loads(body))
    dao.add(json.loads(body))


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='player-stats')

    channel.basic_consume(queue='player-stats',
                          auto_ack=True,
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
