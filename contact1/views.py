from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . models import Contact1
from . serializer import Contact1Serializer
from rest_framework import viewsets
from django.db.models import Avg, Sum, Min, Max, Count


class Contact1View(viewsets.ModelViewSet):
    queryset = Contact1.objects.all()
    serializer_class = Contact1Serializer