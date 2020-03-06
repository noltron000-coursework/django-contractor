from django.http import Http404
from django.shortcuts import render
from django.template import loader

from .models import Key


def index(request):
	latest_key_list = Key.objects.order_by('-date_added')[:5]
	template = loader.get_template('keys/index.html')
	context = {
		'latest_key_list': latest_key_list,
	}
	return render(request, 'keys/index.html', context)

def detail(request, key_id):
	try:
		key = Key.objects.get(pk=key_id)
	except Key.DoesNotExist:
		raise Http404("Key does not exist")
	context = {
		'key': key,
	}
	return render(request, 'keys/detail.html', context)
