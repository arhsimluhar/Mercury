# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Solution


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ("id",)
    date_hierarchy = "created"
    ordering = ("-created",)
