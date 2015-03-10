#!/usr/bin/env python
# coding: utf-8
import os
from bottle import route, static_file, default_app


DEVELOPMENT = not os.environ.get('CBA_PRODUCTION')


# The entire website is static files.
@route('/:path#.*#')
def serve(path):
  path = path or 'index.html' # / -> /index.html
  return static_file(path, root='./')


if __name__ == '__main__':
  from bottle import run
  application = default_app()
  run(application,
      server='paste',
      host='127.0.0.1',
      port=8081,
      reloader=DEVELOPMENT,
      debug=DEVELOPMENT)
