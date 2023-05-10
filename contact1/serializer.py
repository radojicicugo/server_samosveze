from rest_framework import serializers
from . models import Contact1

class Contact1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact1
        fields = '__all__'