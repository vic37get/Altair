from django.urls import path,include
from . import views

app_name='verificador_fraude'
urlpatterns = [
    path('aud', views.homeAud, name='homeAud')
]
