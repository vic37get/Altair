from django.urls import include, path
from . import views

app_name='home_all'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login,name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('submeterCadastro/', views.submeterCadastro, name='submeterCadastro'),
    path('', views.redirectHome,name='home'),
]
