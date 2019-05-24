from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def say_hello(request):
    input_name = request.GET.get("name","")
    if input_name == "":
        return HttpResponse("请求输入？name=name")
    return render(request, "index.html", {"name":input_name})


def index(request):
    """
    登录首页
    :param requet: 
    :return: 
    """
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        # print(username)
        # print(password)
        if username == "" and password != "":
            return render(request, "index.html", {"error": "用户名不能为空，请输入用户名"})
        if username != "" and password == "":
            return render(request, "index.html", {"error": "密码不能为空，请输入密码"})
        if username == "" and password == "":
            return render(request, "index.html", {"error": "用户名和密码不能为空，请输入用户名和密码"})
        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request, "index.html", {"error": "用户名或密码错误"})
        else:
            auth.login(request, user) #记录用户登录状态
            return HttpResponseRedirect("/ProManage/")
            # return render(request, "test_platform/project_manage.html")



#登录成功，用例管理
@login_required
def CaseManage(request):
    """
    登录成功，管理页面
    """
    return render(request, "case_debug.html")

#登录成功，任务管理
@login_required
def TaskManage(request):
    """
    登录成功，管理页面
    """
    return render(request, "task_manage.html")

#登录成功，MockServer管理
@login_required
def MockServer(request):
    """
    登录成功，管理页面
    """
    return render(request, "mock_server.html")

#登录成功，测试工具管理
@login_required
def TestTool(request):
    """
    登录成功，管理页面
    """
    return render(request, "test_tool.html")

@login_required
def logout(request):
    """
    处理用户退出
    :param request: 
    :return: 
    """
    auth.logout(request)
    return HttpResponseRedirect("/")

# Create your views here.
