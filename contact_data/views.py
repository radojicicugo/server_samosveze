from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse
from . models import Contact
from . serializer import ContactSerializer
from rest_framework import viewsets
from django.db.models import Avg, Sum, Min, Max, Count


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer