#!/usr/bin/python

from sys import argv
from twython import Twython
import commands
import logging

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# Do some lgging
logging.basicConfig(filename='tweeter.log', level=logging.DEBUG)

# See 'man fortune' for more info
cmd = '/usr/games/fortune -a -n 140 -s'

def quote():
    line = commands.getoutput(cmd)
#    print line
    api.update_status(status = line)
    logging.debug('line %s twetted', line)
    logging.info('line len: %i', len(line))

# Do it!
quote()
