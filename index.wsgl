#coding=utf-8
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import sys,os

from tornado.options import define, options

#MainHandler
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')



application = tornado.web.Application(
    handlers=[(r'/', IndexHandler)],
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)
