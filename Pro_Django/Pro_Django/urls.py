"""Pro_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 用户管理
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('hello/', views.say_hello, name="say_hello"),
    path('logout/', views.logout, name="logout"),
    path('accounts/login/', views.index, name="index"),

    #项目管理
    path('ProManage/',include("project_app.urls")),

    #模块管理
    path('MolManage/',include("module_app.urls")),

    #用例管理
    path('CaseManage/',include("testcase_app.urls")),

    #任务管理
    path('TaskManage/',include("testtask_app.urls")),


]
