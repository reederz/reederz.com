#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'reederz'
SITENAME = 'reederz'
SITEURL = 'http://reederz.com'

PATH = 'content'

TIMEZONE = 'Europe/Copenhagen'

DEFAULT_LANG = 'en'

THEME = '../pelican-themes/pelican-bootstrap3'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/reederz'),
          ('twitter', 'https://twitter.com/reederz'),)

# Comments
DISQUS_SITENAME = "reederz"

# Analytics
GOOGLE_ANALYTICS = "UA-56922833-2"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
