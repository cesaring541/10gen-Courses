from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter(name='joint',is_safe=True)
@stringfilter
def joint(value):
	return ', '.join(map(lambda x:x.name,value))
