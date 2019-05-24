# Generated by Django 2.1.5 on 2019-05-20 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='名称')),
                ('url', models.TextField(verbose_name='URL')),
                ('method', models.CharField(max_length=50, verbose_name='请求方法')),
                ('headers', models.TextField(verbose_name='请求头')),
                ('parameter_type', models.CharField(max_length=50, verbose_name='参数类型')),
                ('parameter_data', models.TextField(verbose_name='参数内容')),
                ('res_result', models.TextField(verbose_name='请求结果')),
                ('assert_type', models.CharField(max_length=50, verbose_name='断言类型')),
                ('assert_res', models.TextField(verbose_name='断言内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_app.Module')),
            ],
        ),
    ]
