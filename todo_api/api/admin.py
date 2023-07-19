from django.contrib import admin
from .models import Task
# Register your models here.

# custom admin panel


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


admin.site.register(Task, TaskAdmin)
