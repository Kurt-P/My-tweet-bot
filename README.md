My Tweet Bot
============

A Twitter bot a made for the fun of it.
It uses BSD Fortune to tweet a random fortune to my time line.

It was a fun afternoon project.

###API Setup
Go to [new app](https://apps.twitter.com/app/new) and put in the required info.
Next, make sure that the app has read and write access. Finally, locate the 
API keys and access tokens. They can be found under the tab named
"Keys and Access Tokens" under the app settings. Copy those keys into the script
and assin them to the correct variable. 
See [this page for more help](http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/)

###Server Setup
Run `crontab -e` as a normal user and add the following line:  
`0 * * * * /home/$USER/path/to/tweeter.py`

Note: I do not know if useing the `$USER` variable will work, so to be safe
you may want to use your username or home dir name instead.

###Resources
* [MakeUseOf](http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/)
* [BSD Fortune](http://www.bsdfortune.com)
* [Twython](http://twython.readthedocs.org/en/latest/)
* [Google](https://google.com)
