from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from ..models.project import Project
from project_app.models import Project
from project_app.forms import ProjectForm
from comm.paginator_disp_nums import get_pages


#登录成功，默认项目管理页面
@login_required
def ProManage(request):
    """
    登录成功，项目管理页面
    """
    project_all = Project.objects.all()
    paginator = Paginator(project_all,10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "project_manage.html", {"projects":project_all, "type": "list", "contacts":contacts, "paginator":paginator})


#创建项目
@login_required
def createProject(request):
    """
    创建项目
    :param request: 
    :return: 
    """
    if request.method == "GET":
        return render(request, "project_manage.html", {"type": "create"})
    elif request.method == "POST":
        name = request.POST.get("name","")
        describle = request.POST.get("describle","")
        status = request.POST.get("status","")
        Project.objects.create(name=name, describle=describle, status=status)
        # project_all = Project.objects.all()
        return HttpResponseRedirect("/ProManage/")

# 编辑项目
@login_required
def editProject(request,pid):
    """
    编辑项目
    :param request: 
    :return: 
    """
    if request.method == "GET":
        pro = Project.objects.get(id=pid)
        print(pro.status)
        form = ProjectForm(instance=pro)
        return render(request, "project_manage.html", {"type": "edit", "form":form, "id":pid, "pro":pro})
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describle = form.cleaned_data['describle']
            status = form.cleaned_data['status']
            print(status)
            pro_update = Project.objects.get(id=pid)
            pro_update.name = name
            pro_update.describle = describle
            pro_update.status = status
            pro_update.save()
            return HttpResponseRedirect("/ProManage/")

# 删除项目
@login_required
def deleteProject(request,pid):
    """
    删除项目
    :param request: 
    :return: 
    """
    pro = Project.objects.get(id=pid)
    pro.delete()
    return HttpResponseRedirect("/ProManage/")

#在创建测试用例中获取项目列表
@login_required
def getProjectList(request):
    if request.method == "GET":
        projects = Project.objects.all()
        projects_list = []
        for pro in projects:
            project_dict = {
                "id": pro.id,
                "name": pro.name
            }
            projects_list.append(project_dict)
        return JsonResponse({"status":10200,"message":"请求成功","data": projects_list})
    else:
        return JsonResponse({"status":10201,"message":"请求失败"})
# Create your views here.
