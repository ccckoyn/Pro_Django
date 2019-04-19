from django.urls import  path
from users_app import views

app_name = 'users_app'
urlpatterns = [
    path('', views.index, name="index"),
    path('hello/', views.say_hello, name="say_hello"),
    path('logout/', views.logout, name="logout"),

]