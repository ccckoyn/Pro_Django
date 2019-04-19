from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from ..models.project import Project
from module_app.models import Module
from project_app.models import Project
from module_app.forms import ModuleForm


@login_required
def MolManage(request):
    """
    模块管理
    """
    if request.method == "GET":
        modules_all = Module.objects.all()
        return render(request, "module_manage.html", {"modules":modules_all, "type": "list"})

# 创建模块
@login_required
def createModule(request):
    """
    创建模块
    :param request: 
    :return: 
    """
    if request.method == "GET":
        module_form = ModuleForm()
        return render(request, "module_manage.html", {"form":module_form, "type": "create"})
    elif request.method == "POST":

        # '''实现方式一'''
        # name = request.POST.get("name", "")
        # describle = request.POST.get("describle", "")
        # project_id = request.POST.get("project", "")
        # project = Project.objects.get(id=project_id)
        # Module.objects.create(name=name, describle=describle, project=project)
        # # project_all = Project.objects.all()
        # return HttpResponseRedirect("/test_platform/MolManage/")

        """实现方式二"""
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describle = form.cleaned_data['describle']
            project = form.cleaned_data['project']
            Module.objects.create(name=name, describle=describle, project=project)
            return HttpResponseRedirect("/MolManage/")


# 编辑模块
@login_required
def editModule(request,pid):
    """
    编辑项目
    :param request: 
    :return: 
    """
    if request.method == "GET":
        mol = Module.objects.get(id=pid)
        form = ModuleForm(instance=mol)
        return render(request, "module_manage.html", {"type": "edit", "form":form, "id":pid, "pro":mol})
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describle = form.cleaned_data['describle']
            project = form.cleaned_data['project']
            mol_update = Module.objects.get(id=pid)
            mol_update.name = name
            mol_update.describle = describle
            mol_update.project = project
            mol_update.save()
            return HttpResponseRedirect("/MolManage/")

# 删除模块
@login_required
def deleteModule(request,pid):
    """
    删除项目
    :param request: 
    :return: 
    """
    pro = Module.objects.get(id=pid)
    pro.delete()
    return HttpResponseRedirect("/MolManage/")
# Create your views here.

