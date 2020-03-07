from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Keyboard


class IndexView(generic.ListView):
	def get_queryset(self):
		'''Return the last five published keyboards.'''
		return Keyboard.objects.order_by('-date_added')

	template_name = 'keyboards/index.html'


class DetailView(generic.DetailView):
	model = Keyboard
	template_name = 'keyboards/detail.html'
