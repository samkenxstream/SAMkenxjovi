from django.db import models
from myapp.storage import OverwriteStorage

class MyImage(models.Model):
    model_pic = models.ImageField(max_length=4096,upload_to='', default='none/no-img.jpg',storage=OverwriteStorage())


class products(models.Model):
    obj_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name
