from django.urls import path
from testcase_app import views

app_name = 'testcase_app'
urlpatterns = [

    # 测试用例管理
    path('', views.CaseManage, name="CaseManage"),
    path('debug/',views.debug, name="debug"),


]