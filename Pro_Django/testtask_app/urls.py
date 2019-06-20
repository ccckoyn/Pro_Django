from django.urls import path
from testtask_app import views

app_name = 'testtask_app'
urlpatterns = [

    # 测试任务管理
    path('', views.TaskManage, name="TaskManage"),
    path('createTask/', views.createTask, name="createTask"),
    path('getCaseTree/', views.getCaseTree, name="getCaseTree"),
    path('saveTask/', views.saveTask, name="saveTask"),
    path('editTask/<int:tid>/', views.editTask, name="editTask"),
    path('deleteTask/<int:tid>/', views.deleteTask, name="deleteTask"),
    path('runTask/', views.runTask, name="runTask"),
    # path('deleteProject/<int:pid>/', views.deleteProject, name="deleteProject"),
    # path('getProjectList/', views.getProjectList, name="getProjectList"),


]