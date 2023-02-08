from django.db import models
#
from django.contrib.auth.models import User
# Create your models here.


class UserData(models.Model):
    user = models.OneToOneField(
        User, blank=False, null=True, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to="producto/%Y/%m/%d",
                                 default='default/default_img_user.png', blank=True, null=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    state = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=80, blank=True)
    code_post = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    dni = models.CharField(max_length=30, blank=True)
    cuit = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username
