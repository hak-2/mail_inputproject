from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "upload"

urlpatterns = [
    path('', views.index, name='index'),
    path('csvToModel/', views.csvToModel, name='csvtomodel'),
    path("upload/", views.uploadFile, name = "uploadFile"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )