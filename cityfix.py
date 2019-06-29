import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
import sys
import os
import os.path
from client.router import urls

application = tornado.web.Application()

class ConsoleApplication(tornado.web.Application):
    def __init__(self):
        setting = dict(
            template_path=os.path.join(os.path.dirname(__file__), "client/templates"),
            static_path=os.path.join(os.path.dirname(__file__), "client/static"),
            appversion="1.0.0")
        tornado.web.Application.__init__(self, urls, **setting)

def main():
    args = sys.argv
    tornado.options.parse_command_line(args)
    console_server = tornado.httpserver.HTTPServer(ConsoleApplication())
    console_server.listen(80, '*')
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()a
