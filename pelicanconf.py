#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Justas Ažna'
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

LINKS = (('fadeit', 'http://fadeit.dk/en',),)


# Social widget
SOCIAL = (('github', 'https://github.com/reederz'),
          ('twitter', 'https://twitter.com/reederz'),
          ('+justas', 'https://onename.com/justas'),
          ('keybase.io/reederz', 'https://keybase.io/reederz'),)

# Comments
DISQUS_SITENAME = "reederz"

# Analytics
GOOGLE_ANALYTICS = "UA-56922833-2"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
