from django.db import models

# Create your models here.
class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    tittle=models.CharField(max_length=250)
    old_price=models.FloatField()
    new_price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='meadia/')
    priority=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)

    def __str__ (self) -> str:
        return self.tittle  