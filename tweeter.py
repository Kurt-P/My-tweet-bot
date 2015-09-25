#!/usr/bin/python

from sys import argv
from twython import Twython
import subprocess
import logging

API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Setup the api object
api = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Logging DEBUG
logging.basicConfig(filename='tweeter.log', level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%Y-%m-%d %H:%M:%S')

# See 'man fortune' for more info
cmd = 'fortune -n 140 -s'

def tweet(_string, length):
    logging.info("Tweeted: %r", _string) # Log the line that was tweeted
    logging.info("Tweet length: %d", length) # Log the tweet length
    api.update_status(status=_string) # comment out for testing
#   print (_string) # Uncomment for testing

def quote():
    line = subprocess.getoutput(cmd)
    line_length = len(line)

    if line_length >= 141: # Anything under 140 is valid
        quote()
    else:
        tweet(line, line_length)

# Do it!
quote()

