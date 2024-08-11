from django.db import models

# Create your models here.
class Ad_Banner (models.Model):
    Image=models.ImageField(upload_to=r'\media\poster')
    description=models.TextField()