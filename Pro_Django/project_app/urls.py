from django.urls import path
from project_app import views

app_name = 'project_app'
urlpatterns = [

    # 项目管理
    path('', views.ProManage, name="ProManage"),
    path('createProject/', views.createProject, name="createProject"),
    path('editProject/<int:pid>/', views.editProject, name="editProject"),
    path('deleteProject/<int:pid>/', views.deleteProject, name="deleteProject"),

]