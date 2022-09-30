from django.urls import include, path

from . import views

app_name='home_all'
urlpatterns = [
    path('login/', views.login,name='login'),
    path('loginAuth/',views.loginAuth,name='loginAuth'),
    path('logout/',views.logout,name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('submeterCadastro/', views.submeterCadastro, name='submeterCadastro'),
]
