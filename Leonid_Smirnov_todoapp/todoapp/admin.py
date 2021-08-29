from django.contrib import admin
from todoapp.models import Project, ToDo

# Register your models here.

admin.site.register(Project)
admin.site.register(ToDo)
