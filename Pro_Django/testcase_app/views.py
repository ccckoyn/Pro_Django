from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

import requests,json

@login_required
def CaseManage(request):
    # return render(request, "test.html")
    # return render(request, "case_manage_postman.html", {"type": "debug"})
    return render(request,"case_manage.html",{"type":"debug"})

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
       if assert_type == "equals":
           if assert_content.strip() == result.strip():
               return JsonResponse({"result":"断言成功"})
           else:
               return JsonResponse({"result": "断言失败"})

    else:
        return JsonResponse({"result":"请求方法错误"})
# Create your views here.

