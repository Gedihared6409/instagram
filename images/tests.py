from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Image, Comment, Like

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(name = 'Singer', caption = 'Gospel singer in Rwanda')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_saving_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.delete_image()
        images = Image.objects.all()

    def test_update_caption(self):
        self.new_image.save_image()
        self.new_image = Image.objects.get(pk = 1)
        self.new_image.update_caption('changed Image caption')
        self.updated_image = Image.objects.get(id = 1)
        self.assertEqual(self.updated_image.image_caption,"changed Image caption")

class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_profile = Profile(id=1,user=self.new_user,profile_pic='photos/photo',bio='user bio')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

