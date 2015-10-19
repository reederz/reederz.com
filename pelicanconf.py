#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Justas Ažna'
SITENAME = 'reederz'
SITEURL = 'http://reederz.com'

PATH = 'content'

TIMEZONE = 'Europe/Copenhagen'

DEFAULT_LANG = 'en'

THEME = '../pelican-themes/voidy-bootstrap'
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap', 'tag_cloud']

STATIC_PATHS = ['images', 'extra', 'docs']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/keybase.txt': {'path': 'keybase.txt'}}


# voidy-bootstrap specific
# SITESUBTITLE ='Sub-title that goes underneath site name in jumbotron.'
SITETAG = "homepage"
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)
CUSTOM_ARTICLE_FOOTERS = ("taglist.html",)
# Using cosmo theme from bootswatch
BOOTSTRAP_STYLESHEET = 'bootstrap.min.css'
# CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"
SIDEBAR = "sidebar.html"
SIDEBAR_HIDE_CATEGORIES = True
# end of voidy-bootstrap specific

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
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('freedom.press', 'https://freedom.press/'),
         ('CyanogenMod', 'http://www.cyanogenmod.org/'),
         ('Tor Browser', 'https://www.torproject.org'),
         ('Open Whisper Systems', 'https://whispersystems.org/'),
         ('Project Danube', 'http://projectdanube.org/'),
         ('Arch Linux', 'https://www.archlinux.org/'),
         ('BlockchainHub', 'http://blockchainhub.net/'),
         ('fadeit', 'http://fadeit.dk/en',),)


# Social widget
SOCIAL = (('keybase.io/reederz', 'https://keybase.io/reederz',
           'fa fa-lock fa-fw fa-lg'),
          ('github', 'https://github.com/reederz',
           'fa fa-github-square fa-fw fa-lg'),
          ('twitter', 'https://twitter.com/reederz',
           'fa fa-twitter-square fa-fw fa-lg'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
