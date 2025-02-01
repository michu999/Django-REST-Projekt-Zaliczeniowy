from rest_framework import serializers
from .models import Lek

class LekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lek
        fields = ['id', 'nazwa', 'kategoria']



