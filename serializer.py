from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model=User
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model=Book
        fields='__all__'
