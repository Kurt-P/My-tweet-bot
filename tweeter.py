#!/usr/bin/python

from sys import argv
from twython import Twython
import commands
import logging

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# Setup the api object
api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# Logging DEBUG
logging.basicConfig(filename='tweeter.log', level=logging.DEBUG)

# See 'man fortune' for more info
cmd = '/usr/games/fortune -a -n 140 -s'

def quote():
    line = commands.getoutput(cmd)
#    print line # Used for testing; uncomment for testing
    api.update_status(status = line) # Comment out for testing
    logging.info("Tweeted: %r", line) # Log the line that was tweeted.

# Do it!
quote()
