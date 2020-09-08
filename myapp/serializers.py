from rest_framework import serializers

from rest_framework.serializers import (
      ModelSerializer,
)

from myapp.models import MyImage

from myapp.models import products
class productsSerializer(ModelSerializer):
   class Meta:
      model=products
      fields='__all__'
class imageSerializer(ModelSerializer):
   class Meta:
      model = MyImage
      fields = [
         'model_pic'
      ]