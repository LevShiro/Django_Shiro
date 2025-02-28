from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    score_likes = models.IntegerField(default=0,blank=True)
    score_publications = models.IntegerField(default=0,blank=True)
    photo = models.ImageField(null=True,blank=True,upload_to="users/avatars")



