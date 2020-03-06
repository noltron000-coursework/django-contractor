from django.http import HttpResponse

from .models import Key

def index(request):
	latest_key_list = Key.objects.order_by('-date_added')[:5]
	output = ', '.join([k.name for k in latest_key_list])
	return HttpResponse(output)

def detail(request, key_id):
	return HttpResponse(f'You\'re looking at key {key_id}.')
