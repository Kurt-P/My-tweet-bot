#!/usr/bin/python

from sys import argv
from twython import Twython
import commands

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# See 'man fortune' for more info
cmd = '/usr/games/fortune -a -n 140 -s'

def quote():
    line = commands.getoutput(cmd)
#    print line # Used for testing
    api.update_status(status = line)

# Do it!
quote()
