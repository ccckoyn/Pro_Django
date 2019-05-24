from django.urls import path
from testcase_app import views

app_name = 'testcase_app'
urlpatterns = [

    # 测试用例管理
    path('', views.CaseManage, name="CaseManage"),
    path('debugFun/',views.debugFun, name="debugFun"),
    path('assertFun/',views.assertFun, name="assertFun"),
    path('saveCase/',views.saveCase, name="saveCase"),
    path('debugCase/', views.debugCase, name="debugCase"),
    path('editCase/<int:cid>/',views.editCase, name="editCase"),
    path('getCaseInfo/',views.getCaseInfo, name="getCaseInfo"),
    path('deleteCase/<int:cid>/',views.deleteCase, name="deleteCase"),


]