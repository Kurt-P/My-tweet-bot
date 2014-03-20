My-tweet-bot
============

A Twitter bot a made for the fun of it.
It uses BSD Fortune to tweet a random fortune to my time line.

It was a fun afternoon project.

###Setup
Run `crontab -e` as a normal user and add the following line:
`0 * * * * /home/$USER/path/to/tweeter.py`

Note: I do not know if useing the `$USER` variable will work, so to be safe
you may want to use your username or home dir name instead.

###Resources
* [MakeUseOf](http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/)
* [BSD Fortune](http://www.bsdfortune.com)
* [Twython](http://twython.readthedocs.org/en/latest/)
* [Google](https://google.com)
