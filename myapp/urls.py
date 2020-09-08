from django.conf.urls import include, url
from myapp import views

urlpatterns = [
    url(r'^upload/$', views.ImageCreateAPIView.as_view()),
]