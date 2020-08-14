#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lorena Mesa'
SITENAME = 'What To Do Today USA Election 2020'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Theme Settings
THEME = 'pelican-mg'
ALT_NAME = 'WHAT TO DO TODAY USA ELECTION 2020'
DESCRIPTION = """2020 has been a year. From COVID19 to the resurgence of the struggle for racial equity and Black Lives Matter to calling for greater collecive accountability, we're all likely barely surviving. However, it's time to do more. We have less than 100 days until the United States of America 2020 Election. Now is the time to show up, engage, & take action. Daily you can find a list of events, actions, & news to help.
"""
FAVICON = ''
FOOTER = ("&copy; 2020 Lorena. Mesa. All rights reserved.<br>" +
              "If somehow there are any code snippets shared, they are all released under " +
              "<a href=\"http://opensource.org/licenses/MIT\" target=\"_blank\">" +
              "The MIT License</a>, unless otherwise specified.")
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
SHARE = True

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

TWITTER_USERNAME = 'loooorenanicle'
SOCIAL = (('twitter', 'https://twitter.com/loooorenanicle'),
		  ('github', 'https://github.com/lorenanicole/wtdtodayelection2020us'),)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True