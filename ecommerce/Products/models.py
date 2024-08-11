from django.db import models

# Create your models here.
class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    Tittle=models.CharField(max_length=250)
    Price=models.FloatField()
    Description=models.TextField()
    Image=models.ImageField(upload_to=r'\meadia')
    Priority=models.IntegerField(default=0)
    Created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)
    Delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)

    def __str__ (self) -> str:
        return self.tittle  