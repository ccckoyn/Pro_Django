from django.contrib import admin
from module_app.models import Module


class ModuleAdmin(admin.ModelAdmin):

    list_display = ['name','describle','project','create_time']
    search_fields = ['name']
    list_filter = ['project']

admin.site.register(Module, ModuleAdmin)
