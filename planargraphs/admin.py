from django.contrib import admin
from .models import Users
from .models import Planargraph
from .models import Space

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    search_fields = ['email','username']
    list_display = ['email','username']

@admin.register(Planargraph)
class PlanargraphAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'users']

@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'planargraph']