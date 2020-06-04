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


class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    name = models.CharField(max_length = 100, blank = True, null = True)
    caption = models.TextField(blank = True, null = True)
    likes = models.PositiveIntegerField(default = 0, null = True)
    date_posted = models.DateTimeField(auto_now_add = True, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    @classmethod
    def get_images(cls):
        images = cls.objects.order_by('date_posted')
        return images
    
    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id = id)
        return image
    
    def __str__(self):
        return self.name

    # @classmethod
    # def search_by_name(cls,search_term):
    #     photos = cls.objects.filter(name__icontains=search_term)
    #     return photos


class Comment(models.Model):
    comment = models.CharField(max_length = 150, blank = True, null = True)
    date_commented = models.DateTimeField(auto_now_add = True, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    image = models.ForeignKey(Image, null = True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
    
    def __str__(self):
        return self.comment


class Like(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null = True)
    user = models.ForeignKey(User, related_name='liker', null = True)    
    image = models.ForeignKey(Image, related_name='liked_post', null = True)

    def __str__(self):
        return '{} : {}'.format(self.user, self.image)
