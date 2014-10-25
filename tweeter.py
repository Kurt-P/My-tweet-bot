#!/usr/bin/python

from sys import argv
from twython import Twython
import commands
import logging

API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Setup the api object
api = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Logging DEBUG
logging.basicConfig(filename='tweeter.log', level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %H:%M:%S')

# See 'man fortune' for more info
cmd = 'fortune -a -n 140 -s'

def tweet(_string, length):
    logging.info("Tweeted: %r", _string) # Log the line that was tweeted
    logging.info("Tweet length: %d", length) # Log the tweet length
    api.update_status(status=_string) # comment out for testing
#    print _string # Uncomment for testing


## NOTE ##
## Leave this sectino for now, I will delete it later;
## After more testing has been done.
#def quote():
#    line = commands.getoutput(cmd)
#    print line # Used for testing; uncomment for testing
#    api.update_status(status = line) # Comment out for testing
#    logging.info("Tweeted: %r", line) # Log the line that was tweeted.

def quote():
    line = commands.getoutput(cmd)
    line_length = len(line)

    if line_length > 140:
        quote()
    else:
        tweet(line, line_length)

# Do it!
quote()

