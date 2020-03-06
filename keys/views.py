from django.http import Http404
from django.shortcuts import get_object_or_404, render
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
	key = get_object_or_404(Key, pk=key_id)
	context = {
		'key': key,
	}
	return render(request, 'keys/detail.html', context)
