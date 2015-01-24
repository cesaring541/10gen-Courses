from pyramid.config import Configurator
import mongoengine
from mongoengine import connect
from . import configs

def factory_db():
    if not configs.CONN:
        configs.CONN = connect(configs.MONGO['DB'])
    return configs.CONN

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    f = factory_db()
    return config.make_wsgi_app()
