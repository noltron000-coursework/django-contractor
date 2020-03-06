from django.http import HttpResponse
from django.template import loader

from .models import Key


def index(request):
	latest_key_list = Key.objects.order_by('-date_added')[:5]
	template = loader.get_template('keys/index.html')
	context = {
		'latest_key_list': latest_key_list,
	}
	return HttpResponse(template.render(context, request))


def detail(request, key_id):
	return HttpResponse(f'You\'re looking at key {key_id}.')
