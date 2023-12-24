from rest_framework import serializers
from .models import Jhumka

class JhumkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jhumka
        fields = '__all__'