from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Switch


class IndexView(generic.ListView):
	def get_queryset(self):
		'''Return the last five published keys.'''
		return Switch.objects.order_by('-date_added')

	template_name = 'switches/index.html'
	context_object_name = 'latest_key_list'


class DetailView(generic.DetailView):
	model = Switch
	template_name = 'switches/detail.html'
