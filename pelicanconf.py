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
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap', 'tag_cloud']
TYPOGRIFY = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('fadeit', 'http://fadeit.dk/en',),)


# Social widget
SOCIAL = (('github', 'https://github.com/reederz'),
          ('twitter', 'https://twitter.com/reederz'),
          ('reddit', 'https://reddit.com/u/reederz'),
          ('+justas', 'https://onename.com/justas'),
          ('keybase.io/reederz', 'https://keybase.io/reederz'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
