from rest_framework import serializers
from .models import UserModel

class UserModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = ['id', 'name', 'password', 'created_at']