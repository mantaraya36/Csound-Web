#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Joachim Heintz and others'
SITENAME = u'Csound'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# avoid getting the "misc" menu 
HIDE_CATEGORIES_FROM_MENU = True

THEME = 'themes/fresh'

LINKS =  (('Download', 'http://sourceforge.net/projects/csound/files/csound6/'),
          ('Wiki', 'http://sourceforge.net/p/csound/wiki/Home/'),
          ('csounds.com', 'http://csounds.com/'),
          ('Journal', 'http://csounds.com/csound-journal/'),
          ('Manual', 'http://csounds.com/manual/html/index.html'),
          ('Textbook', 'http://en.flossmanuals.net/csound/index'), 
          ('CsoundQt', 'http://sourceforge.net/projects/qutecsound/'),
          ('Blue', 'http://sourceforge.net/projects/bluemusic/'),
          ('Cabbage', 'http://www.thecabbagefoundation.org'),
          ('McCurdy Collection', 'http://iainmccurdy.org/csound.html')
          )

DEFAULT_PAGINATION = False

