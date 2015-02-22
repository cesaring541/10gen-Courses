from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

config = Configurator()

# from .db import Database
# from .apps.Views.views import *
# from .routes import Routes
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authn_policy = AuthTktAuthenticationPolicy('onetwothreefourfivesix', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    # import ipdb; ipdb.set_trace()
    # config.include('pyramidblog.routes')
    config.include('pyramidblog.db')
    config.include('pyramidblog.apps')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.add_static_view('static', 'static', cache_max_age=3600)
    # Routes(config)
    # Database(config)
    config.scan()

    return config.make_wsgi_app()
