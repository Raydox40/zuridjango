from turtle import title
from django.db import models

# Create your models here.
class post(models,Model):
    title = models.CharField(max_length:200)
    Text = models TextField()
    Author = models.get_user_model function()
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()