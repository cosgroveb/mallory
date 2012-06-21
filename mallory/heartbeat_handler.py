import tornado.web

class HeartbeatHandler(tornado.web.RequestHandler):
    def initialize(self, circuit_breaker):
        print "initializing"
        self.circuit_breaker = circuit_breaker

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        if self.circuit_breaker.is_tripped():
            self.set_status(503)
        else:
            self.set_status(200)

        self.write("HI")
        self.finish()
