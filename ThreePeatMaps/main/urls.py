from django.urls import path, include
from . import views


app_name = "main"

urlpatterns = [
	
		path('home/', views.home, name="home"),
		path('', views.home, name="home"),
		# path('/', views.route, name="home"),
		path('route/', views.route, name="route"),
		path('map/', views.map, name="map"),
		path('contact/', views.contact, name="contact"),
	# path('', views.route, name="home"),

	# path('', include('main.urls')),

	]