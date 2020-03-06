from django.urls import path

from . import views

app_name = 'keyboards'

urlpatterns = [
	# ex: /keyboards/
	path('', views.IndexView.as_view(), name='index'),
	# # ex: /keyboards/new/
	# path('new/', views.CreateView.as_view, name='new'),
	# ex: /keyboards/5/
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
