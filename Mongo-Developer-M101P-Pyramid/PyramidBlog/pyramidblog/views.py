from pyramid.view import view_config
from pyramid.renderers import get_renderer

# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'PyramidBlog'}

@view_config(route_name='home',renderer='templates/index.pt')
def my_view(request):
    main = get_renderer('templates/master.pt').implementation()
    return {'main':main}
