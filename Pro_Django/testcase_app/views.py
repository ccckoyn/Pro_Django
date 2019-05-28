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
import requests,json

@csrf_exempt
@login_required
def CaseManage(request):
    """用例列表"""
    # return render(request, "test.html")
    # return render(request, "case_manage_postman.html", {"type": "debug"})

    case_all = TestCase.objects.all()
    paginator = Paginator(case_all, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, "case_manage.html", {"testcases": case_all, "contacts": contacts, "paginator": paginator})



@csrf_exempt
@login_required
def debugCase(request):

    """添加用例"""

    return render(request, "case_debug.html")

@csrf_exempt
@login_required
def editCase(request, cid):

    """编辑用例"""

    return render(request,"case_edit.html")

@csrf_exempt
@login_required
def deleteCase(request, cid):
    """删除测试用例"""
    case = TestCase.objects.get(id=cid)
    case.delete()
    return HttpResponseRedirect("/CaseManage/")

@csrf_exempt
@login_required
def debugFun(request):
    if request.method == "POST":
        del_parameter = ""
        del_headers = ""
        url = request.POST.get("url")
        method = request.POST.get("method")
        headers = request.POST.get("headers","")
        req_type = request.POST.get("type")
        parameter = request.POST.get("parameter","")

        #处理parameter
        if parameter != "":
            del_parameter = parameter.replace("'", '"')
            try:
                parameter = json.loads(del_parameter)
            except json.decoder.JSONDecodeError:
                return JsonResponse({"result": "参数类型错误"})


        #处理headers
        if headers != "":
            del_headers = headers.replace("'", '"')
            try:
                headers = json.loads(del_headers)
            except json.decoder.JSONDecodeError:
                return JsonResponse({"result": "header类型错误"})

        if method == "get":
            if headers == "":
                if parameter != "":
                    r = requests.get(url, params=parameter)
                else:
                    r = requests.get(url)
            else:
                if parameter != "":
                    r = requests.get(url, params=parameter, headers=headers)
                else:
                    r = requests.get(url,headers=headers)
        if method == "post":
            if req_type == "form-data":
                if headers == "":
                    r = requests.post(url, data=parameter)
                else:
                    r = requests.post(url, data=parameter, headers=headers)
            if req_type == "json":
                if headers == "":
                    r = requests.post(url, json=parameter)
                else:
                    r = requests.post(url, json=parameter, headers=headers)
        return JsonResponse({"result":r.text})
    else:
        return JsonResponse({"result":"请求方法错误"})

@csrf_exempt
@login_required
def assertFun(request):
    if request.method == "POST":
       result = request.POST.get("result","")
       assert_content = request.POST.get("assert_res","")
       assert_type = request.POST.get("assert_type","")
       if result == "" or assert_content == "":
           return JsonResponse({"result":"返回结果或断言内容为空，不符合断言要求，请调整"})
       if assert_type == "include":
           if assert_content.strip() in result.strip():
               return JsonResponse({"result":"断言成功"})
           else:
               return JsonResponse({"result": "断言失败"})
       if assert_type == "equal":
           if assert_content.strip() == result.strip():
               return JsonResponse({"result":"断言成功"})
           else:
               return JsonResponse({"result": "断言失败"})

    else:
        return JsonResponse({"result":"请求方法错误"})


@csrf_exempt
@login_required
def saveCase(request):


    if request.method == "POST":

        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        headers = request.POST.get("header", "")
        parameter_type = request.POST.get("type", "")
        parameter_data = request.POST.get("parameter", "")

        assert_type = request.POST.get("assert_type", "")
        assert_res = request.POST.get("assert_res", "")

        name = request.POST.get("case_name", "")
        module_id = request.POST.get("module_id", "")

        cid = request.POST.get("cid", "")
        # print("xxxxxxxxxxxxx",cid)

        if name == "":
            return JsonResponse({"status":10101, "message":"用例名称不能为空"})
        if assert_res == "":
            return JsonResponse({"status":10102, "message":"断言内容不能为空"})
        if module_id == "" or module_id == "0":
            return JsonResponse({"status":10103, "message":"请选择模块"})

        module = Module.objects.get(id=module_id)

        if cid == "":
            TestCase.objects.create(name=name, url=url, method=method, headers=headers, parameter_type=parameter_type,
                                    parameter_data=parameter_data, assert_type=assert_type, assert_res=assert_res, module=module)
            return JsonResponse({"status": 10200, "message": "创建用例成功"})

        else:
            case = TestCase.objects.get(id=cid)
            case.name = name
            case.url = url
            case.method = method
            case.headers = headers
            case.parameter_type = parameter_type
            case.parameter_data = parameter_data
            case.assert_type = assert_type
            case.assert_res = assert_res
            case.module = module
            case.save()
            return JsonResponse({"status":10200, "message":"更新用例成功"})

    else:
        return JsonResponse({"status": 10100, "message": "请求方式错误"})



@csrf_exempt
@login_required
def getCaseInfo(request):
    """获取用例详细数据"""
    if request.method == "POST":
        cid = request.POST.get("cid","")
        case = TestCase.objects.get(id=cid)

        mid = case.module_id
        # print(mid)
        # module = Module.objects.get(id=mid).name
        pid = Module.objects.get(id=mid).project_id
        # project = Project.objects.get(id=pid).name

        case_dict = {
            "id": case.id,
            "url": case.url,
            "name": case.name,
            "method": case.method,
            "headers": case.headers,
            "parameter_type": case.parameter_type,
            "parameter_data": case.parameter_data,
            "assert_type": case.assert_type,
            "assert_res": case.assert_res,
            "project_id":pid,
            "module_id":mid,
        }
        return JsonResponse({"status":10200,"message":"请求成功","data":case_dict})
