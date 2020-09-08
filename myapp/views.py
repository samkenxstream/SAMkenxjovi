from .serializers import imageSerializer
from rest_framework.generics import (CreateAPIView)
from myapp.models import MyImage
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import products
from .serializers import productsSerializer

import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity

import os
import numpy as np
from scipy.ndimage import rotate
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.applications.vgg19 import VGG19
from tensorflow.python.keras.applications.vgg19 import preprocess_input as ppVGG19
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.layers import GlobalAveragePooling2D
class productslist(APIView):
    def get(self,request):
        id=request.query_params['id']
        image_path = 'media/'+id
        print(image_path)
        # load VGG19 model
        print("Loading VGG19 pre-trained model...")
        base_model = VGG19(weights='imagenet')
        base_model = Model(inputs=base_model.input, outputs=base_model.get_layer('block4_pool').output)
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        VGG_model = Model(inputs=base_model.input, outputs=x)
        img_VGG = image.load_img(image_path, target_size=(224, 224))

        img = image.img_to_array(img_VGG)  # convert to array

        img = np.expand_dims(img, axis=0)
        img = ppVGG19(img)

        features = VGG_model.predict(img).flatten()
        point_a = features.reshape(1, 512)
        filename = []
        score = []
        for i in os.listdir('data/features'):
            point_b = np.load('data/features/' + i).reshape(1, 512)
            filename.append(i)
            distance = np.linalg.norm(point_a - point_b)

            cos_lib = cosine_similarity(point_a, point_b)
            score.append(cos_lib[0][0])

        ind = score.index((max(score)))
        print(ind)
        print(filename[ind])
        product=products.objects.get(obj_id=filename[ind])

        serialier=productsSerializer(product)
        return Response(serialier.data)

    def post(self):
        pass

class ImageCreateAPIView(CreateAPIView):
    serializer_class = imageSerializer
    queryset = MyImage.objects.all()
