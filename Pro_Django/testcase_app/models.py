from django.db import models
from module_app.models import Module

class TestCase(models.Model):
    """
    测试用例表
    """
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.TextField("名称", null=False)
    url = models.TextField("URL", null=False)
    method = models.CharField("请求方法", max_length=50, null=False)
    headers = models.TextField("请求头", null=False)
    parameter_type = models.CharField("参数类型", max_length=50, null=False)
    parameter_data = models.TextField("参数内容", null=False)
    # res_result = models.TextField("请求结果", null=False)
    assert_type = models.CharField("断言类型", max_length=50, null=False)
    assert_res =  models.TextField("断言内容", null=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name
