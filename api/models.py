from django.db import models

class UserModel(models.Model):
    
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
