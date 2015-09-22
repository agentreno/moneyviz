from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class GoogleInfo(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar_url = models.CharField(max_length=100)
