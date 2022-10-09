from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import *

class CountriesSerializer(ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'