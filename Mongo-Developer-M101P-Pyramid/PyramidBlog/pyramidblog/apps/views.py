from pyramid.view import view_config
from pyramid.renderers import get_renderer
from .models import *
# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'PyramidBlog'}
from deform import *
from .forms import *
@view_config(route_name='home',renderer='pyramidblog:templates/index.pt')
def my_view(request):
    main = get_renderer('pyramidblog:templates/master.pt').implementation()
    return {'main':main}

@view_config(route_name='login',renderer='pyramidblog:templates/login.pt')
def my_view(request):
	print request.method
	schema = Person()
	form = Form(schema, buttons=('submit',))
	if request.method == 'POST':
		try:
			if form.validate(request.POST.items()):
				import ipdb; ipdb.set_trace()
		except deform.ValidationFailure as e:
			pass

	return {'form':form}
# @view_config(route_name='/',renderer='templates/index.pt')
# def my_view(request):
#     main = get_renderer('templates/master.pt').implementation()
#     return {'main':main}
