#!/usr/bin/python

from sys import argv
from twython import Twython
import commands

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

cmd = '/usr/games/fortune -a'

def quote():
    line = commands.getoutput(cmd)
    if len(line) > 140:
        quote()
    else:
        api.update_status(status = line)

quote()
