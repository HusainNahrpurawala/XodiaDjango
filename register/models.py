from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    college = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=13, default="")

    # bot_path
    # bot_extension

    def get_absolute_url(self):
        return reverse('register/welcome.html')

    def __str__(self):
        return self.user.username
