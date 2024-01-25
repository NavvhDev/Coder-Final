from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('index/', index, name = 'index'),
    path('noticias/', noticias, name = 'noticias'),
    path('tecnologia/', tecnologia, name = 'tecnologia'),
    path('videojuegos/', videojuegos, name = 'videojuegos'),
    path('acerca_de/', acerca_de, name = 'acerca_de'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='logout'),
    path('signin/', signin, name='signin'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),

]