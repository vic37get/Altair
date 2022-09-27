from django.urls import include, path
from . import views

app_name='homeAll'
urlpatterns = [
    path('home/', views.home,name='home'),
    path('', views.redirectHome,name='home'),
]
