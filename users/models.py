from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.conf import settings


DeUser = settings.AUTH_USER_MODEL
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30, unique=True)


    REQUIRED_FIELDS = ['username', 'full_name', 'phone_number']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="p_profile")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")


    def get_username(self):
        return self.user.username

    def __str__(self):
        return self.user.username


    def get_profile_pic(self):
        if self.profile_pic:
            return "http://127.0.0.1:8000" + self.profile_pic.url
        return ''

    def get_email(self):
        return self.user.email

    def get_phone_number(self):
        return self.user.phone_number

    def get_full_name(self):
        return self.user.full_name

