from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    username = models.CharField(default='User',max_length=50)
    profile_pic = models.ImageField(upload_to = 'profile_pic/', null = True)
    bio = models.TextField(max_length = 500, blank = True, null = True)
    first_name = models.CharField(max_length =20, null = True)
	

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_profiles(cls, search_term):
        profile = cls.objects.filter(first_name__icontains=search_term)
        return profile

    def __str__(self):
        return self.user.username
