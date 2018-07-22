#!/usr/bin/env python
# coding=utf8


class LoggerMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print("--------------")
        print("Functioncalled", environ)
        print("----------------")
        return self.app(environ, start_response)
