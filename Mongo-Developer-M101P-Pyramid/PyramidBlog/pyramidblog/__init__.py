from pyramid.config import Configurator

# from .db import Database
# from .apps.Views.views import *
# from .routes import Routes
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    # import ipdb; ipdb.set_trace()
    # config.include('pyramidblog.routes')
    config.include('pyramidblog.db')
    config.include('pyramidblog.apps')

    config.add_static_view('static', 'static', cache_max_age=3600)
    # Routes(config)
    # Database(config)
    config.scan()

    return config.make_wsgi_app()
