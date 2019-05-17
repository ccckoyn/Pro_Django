from django.urls import path
from testcase_app import views

app_name = 'testcase_app'
urlpatterns = [

    # 测试用例管理
    path('', views.CaseManage, name="CaseManage"),
    path('debugFun/',views.debugFun, name="debugFun"),
    path('assertFun/',views.assertFun, name="assertFun")


]