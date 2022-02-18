from django.db import models
from common.models import TimeStampMixin


class Recipe(TimeStampMixin):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    preparation_mode = models.TextField()
    preparation_time = models.IntegerField()
    income = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
