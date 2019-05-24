from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from module_app.models import Module
from module_app.forms import ModuleForm
from django.views.decorators.csrf import csrf_exempt


@login_required
def MolManage(request):
    """
    模块管理
    """
    if request.method == "GET":
        modules_all = Module.objects.all()
        paginator = Paginator(modules_all, 10)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        return render(request, "module_manage.html", {"modules":modules_all, "type": "list", "contacts": contacts, "paginator": paginator})

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
    编辑模块
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
    删除模块
    :param request: 
    :return: 
    """
    pro = Module.objects.get(id=pid)
    pro.delete()
    return HttpResponseRedirect("/MolManage/")


#在创建测试用例中,根据项目ID返回对应的模块列表
@csrf_exempt
@login_required
def getModuleList(request):
    if request.method == "POST":
        pid = request.POST.get("pid","")
        if pid == "":
            return JsonResponse({"status":10202,"message":"项目为空，请创建项目"})
        modules = Module.objects.filter(project=int(pid))
        modules_list = []
        for mod in modules:
            modules_dict = {
                "id": mod.id,
                "name": mod.name
            }
            modules_list.append(modules_dict)
        return JsonResponse({"status":10200,"message":"请求成功","data": modules_list})
    else:
        return JsonResponse({"status":10201,"message":"请求失败"})
# Create your views here.

