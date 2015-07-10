#!/usr/bin/env python

from flask import Flask
import tornado.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.autoreload

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
  return "Hello, world!"

def run_server():
  http_server = tornado.httpserver.HTTPServer(
    tornado.wsgi.WSGIContainer(app)
    )
  http_server.listen(8000)

  tornado.options.parse_command_line()

  io_loop = tornado.ioloop.IOLoop.instance()
  tornado.autoreload.start(io_loop)
  try:
    io_loop.start()
  except KeyboardInterrupt:
    pass

if __name__ = "__main__":
  run_server()