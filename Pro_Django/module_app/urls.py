from django.urls import path
from module_app import views

app_name = 'module_app'
urlpatterns = [

    # 模块管理
    path('', views.MolManage, name="MolManage"),
    path('createModule/', views.createModule, name="createModule"),
    path('editModule/<int:pid>/', views.editModule, name="editModule"),
    path('deleteModule/<int:pid>/', views.deleteModule, name="deleteModule"),
    path('getModuleList/', views.getModuleList, name="getModuleList"),

]