# Generated by Django 2.1.5 on 2019-05-09 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, verbose_name='项目名称'),
        ),
    ]