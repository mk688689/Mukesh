from django.db import models
from datetime import date
# Create your models here.


class Blog(models.Model):
    title = models.CharField('post title', max_length=200)
    image = models.ImageField (upload_to='images/')
    message = models.TextField(default="")
    description = models.TextField()
    posted_date = models.DateField(default=date.today)
