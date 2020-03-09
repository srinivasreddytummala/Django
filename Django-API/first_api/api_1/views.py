from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from first_api.serializers import CricketSerializer

from .models import Cricket



class CricketViewSet(viewsets.ModelViewSet):
	queryset =  Cricket.objects.all()
	serializer_class = CricketSerializer
