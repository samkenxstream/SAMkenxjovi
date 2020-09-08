from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^image/', include('myapp.urls')),
    url(r'^product/', views.productslist.as_view()),
	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)