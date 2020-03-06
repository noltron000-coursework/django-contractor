from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Key


class IndexView(generic.ListView):
	def get_queryset(self):
		'''Return the last five published keys.'''
		return Key.objects.order_by('-date_added')

	template_name = 'keys/index.html'
	context_object_name = 'latest_key_list'


class DetailView(generic.DetailView):
	model = Key
	template_name = 'keys/detail.html'
