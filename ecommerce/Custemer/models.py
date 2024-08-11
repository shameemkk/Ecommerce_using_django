from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Custemer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    Name=models.CharField(max_length=250)
    Phone=models.CharField(max_length=10)
    Address=models.TextField()
    User=models.OneToOneField(User,on_delete=models.CASCADE,related_name='custemer_profile')
    Created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)
    Delete_status=models.IntegerField(choices=DELETE_CHOICE, default=LIVE)

    def __str__ (self) -> str:
        return self.Name