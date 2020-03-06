from django.urls import path

from . import views

app_name = 'switches'

urlpatterns = [
	# ex: /switches/
	path('', views.IndexView.as_view(), name='index'),
	# # ex: /switches/new/
	# path('new/', views.CreateView.as_view, name='new'),
	# ex: /switches/5/
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
