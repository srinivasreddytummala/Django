from django.urls import path

from .views import Geeks

urlpatterns = [

path('',Geeks.geeks_view, name = 'geek')

]