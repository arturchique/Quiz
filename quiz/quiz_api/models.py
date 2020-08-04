from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Participant(models.Model):
    name = models.CharField(verbose_name='username', max_length=30)
    rating = models.FloatField(verbose_name='rating', default=0.0)
    bio = models.CharField(verbose_name='about', max_length=256, blank=True)
    avatar = models.ImageField(null=True, blank=True, verbose_name='avatar')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
