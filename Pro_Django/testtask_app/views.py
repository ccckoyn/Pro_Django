# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from testcase_app.models import TestCase
from module_app.models import Module
from project_app.models import Project
from testtask_app.models import TestTask
import requests,json

@login_required
@csrf_exempt
def TaskManage(request):

    """任务管理"""

    tasks = TestTask.objects.all()

    return render(request, "task_manage.html", {"type":"list", "tasks": tasks})

@login_required
@csrf_exempt
def createTask(request):

    """创建任务"""

    return render(request, "task_create.html", {"type":"create"})

@login_required
@csrf_exempt
def editTask(request, tid):

    """跳转到编辑页面"""
    return render(request, "task_edit.html", {"type":"edit"})

@login_required
@csrf_exempt
def deleteTask(request, tid):

    """跳转到编辑页面"""

    task = TestTask.objects.get(id=tid)
    task.delete()

    return HttpResponseRedirect("/TaskManage/")

@login_required
@csrf_exempt
def getCaseTree(request):

    """获取测试用例"""

    if request.method == "GET":

        projects = Project.objects.all()
        data_list = []
        for project in projects:
            project_dict = {
                "name": project.name,
                "isParent": True

            }


            module_list = []
            modules = Module.objects.filter(project_id = project.id)

            for module in modules:
                module_dict = {
                    "name": module.name,
                    "isParent": True
                }


                case_list = []
                cases = TestCase.objects.filter(module_id = module.id)
                for case in cases:
                    case_dict = {
                        "name": case.name,
                        "id": case.id,
                        "isParent": False
                    }
                    case_list.append(case_dict)
                module_dict["children"] = case_list
                module_list.append(module_dict)

            project_dict["children"] = module_list
            data_list.append(project_dict)

        return JsonResponse({"status": 10200, "message": "success", "data": data_list})

    # 编辑用例时，获取勾选的测试用例
    if request.method == "POST":

        tid = request.POST.get("tid", "")

        if tid == "":
            return JsonResponse({"status": 10102, "message": "测试任务ID不能为空"})


        task = TestTask.objects.get(id=tid)
        caseList = json.loads(task.cases)

        task_data = {
            "name": task.name,
            "desc": task.describle
        }


        projects = Project.objects.all()
        data_list = []
        for project in projects:
            project_dict = {
                "name": project.name,
                "isParent": True

            }

            module_list = []
            modules = Module.objects.filter(project_id=project.id)

            for module in modules:
                module_dict = {
                    "name": module.name,
                    "isParent": True
                }

                case_list = []
                cases = TestCase.objects.filter(module_id=module.id)
                for case in cases:
                    if case.id in caseList:
                        case_dict = {
                            "name": case.name,
                            "id": case.id,
                            "isParent": False,
                            "checked": True
                        }
                    else:
                        case_dict = {
                            "name": case.name,
                            "id": case.id,
                            "isParent": False,
                            "checked": False
                        }
                    case_list.append(case_dict)
                module_dict["children"] = case_list
                module_list.append(module_dict)

            project_dict["children"] = module_list
            data_list.append(project_dict)

        task_data["cases"] = data_list
        print("tid", tid)
        return JsonResponse({"status": 10200, "message": "success", "data": task_data})


@login_required
@csrf_exempt
def saveTask(request):
    """保存任务"""

    if request.method == "POST":
        task_id = request.POST.get("task_id","")
        task_name = request.POST.get("task_name","")
        task_desc = request.POST.get("task_desc","")
        cases = request.POST.get("cases","")

        if task_name == "":
            return JsonResponse({"status": 10102, "message": "任务名称不能为空"})
        if cases == "":
            return JsonResponse({"status": 10102, "message": "测试用例不能为空"})

        if task_id == "0":

            TestTask.objects.create(name=task_name, describle=task_desc, cases=cases)
            return JsonResponse({"status": 10020, "message": "创建任务成功"})

        else:

            task = TestTask.objects.get(id=task_id)
            task.name = task_name
            task.describle = task_desc
            task.cases = cases
            task.save()
            return JsonResponse({"status": 10020, "message": "更新任务成功"})

    else:
        return JsonResponse({"status": 10102, "message": "请求方法错误"})


