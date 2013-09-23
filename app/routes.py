# -*- coding: utf-8 -*-

import webapp2, handlers

# Map url's to handlers
urls = [
    webapp2.Route(r'/', handler=handlers.Main, name="home"),
    webapp2.Route(r'/login', handler=handlers.LogIn, name="login"),
    webapp2.Route(r'/_ah/login_required', handler=handlers.LogIn),
    webapp2.Route(r'/logout', handler=handlers.LogOut, name="logout"),
    webapp2.Route(r'/account', handler=handlers.Account, name="account"),
    webapp2.Route(r'/account/setup', handler=handlers.AccountSetup, name="setup"),

    webapp2.Route(r'/collections', handler=handlers.Collections, name="collections"),
    webapp2.Route(r'/collections/new', handler=handlers.NewCollection, name="new-collection"),
    webapp2.Route(r'/contacts', handler=handlers.Contacts, name="contacts"),
    webapp2.Route(r'/messages', handler=handlers.Messages, name="messages"),
    webapp2.Route(r'/metrics', handler=handlers.Metrics, name="metrics"),

    (r'.*', handlers.NotFound)
]
