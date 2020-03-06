from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello, world. You\'re at the keys index.')

def detail(request, key_id):
	return HttpResponse(f'You\'re looking at key {key_id}.')
