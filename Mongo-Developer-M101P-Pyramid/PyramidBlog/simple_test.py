from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='hello')
def hello_world(request):
	print request.matchdict
	return Response('Hello %(name)s!' % request.matchdict)

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    # import ipdb; ipdb.set_trace()
    print 'server run at %s' % server.server_address[1]
    # server.application.logger.debug('server run at %s' % server.server_address[1])
    server.serve_forever()

