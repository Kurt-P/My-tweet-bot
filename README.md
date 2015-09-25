# My Tweet Bot

A Twitter bot a made for the fun of it.
It uses BSD Fortune to tweet a random fortune to my time line.

It was a fun afternoon project.

## Requirements
* `Python 3.4+`
* `pip`

## Setup

### Twython
Install Twython with `sudo pip install twython`

### Twitter API Setup
Go to [new app](https://apps.twitter.com/app/new) and fill out the required information.
Next, give the application read and write access. Finally, locate the API keys
and access tokens. They can be found under the tab named "Keys and Access Tokens"
under the application's settings. Copy those keys into the script and assign them
to the correct variable.
```python
API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
```
See [this page for more help](http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/)

### Server Setup
If you want the script to run automatically every hour you can
run `crontab -e` as a normal user and add the following line:  
`0 * * * * /path/to/tweeter.py`

## Resources
* [MakeUseOf](http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/)
* [BSD Fortune](http://www.bsdfortune.com)
* [Twython](http://twython.readthedocs.org/en/latest/)
* [DuckDuckGo](https://duckduckgo.com)
* [pip](https://pypi.python.org/pypi/pip/)
