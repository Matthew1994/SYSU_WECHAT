#coding=utf-8
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import sys,os
import py.Sysulib

from tornado.options import define, options
define("port", default=8689, help="run on the given port", type=int)


#MainHandler
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write(py.Sysulib.mylib(1,2))
        self.render('index.html')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
