from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additonal
    # password1 = models.CharField(max_length=256)
    portfolio_site = models.URLField(blank=True)
    Profile_Picture = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
