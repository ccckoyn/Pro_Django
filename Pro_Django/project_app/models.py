from django.db import models

# Create your models here.

class Project(models.Model):

    """项目表"""
    CHECK_CHOICE = (
        ('0',"禁止"),
        ('1',"启用"),
    )

    name = models.CharField("项目名称",max_length=100, null=False)
    describle = models.TextField("项目描述",default="")
    status = models.BooleanField("项目状态",default=1)
    # status = models.RadioSelect(max_length=25,choices=CHECK_CHOICE)
    create_time = models.DateTimeField("创建时间",auto_now_add=True)
    update_time = models.DateTimeField("更新时间",auto_now=True)


    def __str__(self):
        return self.name
