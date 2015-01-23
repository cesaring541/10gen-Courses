
from django.shortcuts import render

def error404(request):
    respon = render(request,'errors/404error.tpl')
    respon.status_code = 404
    return respon


def error500(request):
    respon = render(request,'errors/500error.tpl')
    respon.status_code = 500
    return respon
