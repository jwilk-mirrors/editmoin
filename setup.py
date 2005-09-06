#!/usr/bin/python
from distutils.core import setup

setup(name="editmoin",
      version = "1.2",
      description = "Edit Moin pages remotely with your preferred editor",
      author = "Gustavo Niemeyer",
      author_email = "niemeyer@conectiva.com",
      url = "https://moin.conectiva.com.br/EditMoin",
      license = "GPL",
      long_description = 
"""\
This program allows you to edit moin (see http://moin.sourceforge.net)
pages with your preferred editor. It means you can easily edit your
pages, without the usual limitations of most web browsers' text areas.
""",
      scripts = ["editmoin"],
      )
