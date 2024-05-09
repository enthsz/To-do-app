from django.contrib import admin
from .models import Tarefa, CustomUser
# Register your models here.
admin.site.register(Tarefa)
admin.site.register(CustomUser)