from rest_framework import serializers
from django.contrib.auth.models import User

class UserModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','username', 'password', 'last_login', 'is_superuser', 'date_joined']