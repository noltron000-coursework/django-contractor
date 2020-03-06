from django.urls import path

from . import views

app_name = 'keys'

urlpatterns = [
	# ex: /keys/
	path('', views.index, name='index'),
	# ex: /keys/5/
	path('<int:key_id>/', views.detail, name='detail'),
]
