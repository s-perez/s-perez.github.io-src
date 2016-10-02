#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Salvador Pérez'
SITENAME = 'No place like ~'
SITEURL = ''
SITETITLE = SITENAME

PATH = 'content'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('The Git Adventure', '/the-git-adventure.html'),
)

# Social widget
SOCIAL = (
    ('linkedin',  'https://www.linkedin.com/in/sprezmar'),
    ('github', 	'https://github.com/s-perez'),
    ('rss', '/feeds/all.atom.xml'),
)
# THEME SPECIFIC SETTINGS

PYGMENTS_STYLE = "github"

SITELOGO = ("https://scontent-lhr3-1.xx.fbcdn.net/v/t1.0-9/14470485_1020714312"
            "8201490_3161606201255281270_n.jpg?oh=5035d104a522e9b56763d1446478"
            "3ac8&oe=5864D258")

COPYRIGHT_YEAR = "2016"

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "Flex"

DISQUS_SITENAME = "noplacelikehome-1"
USE_FOLDER_AS_CATEGORY = True

STATIC_PATHS = ['images']
