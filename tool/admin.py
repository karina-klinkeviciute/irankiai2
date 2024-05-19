from django.contrib import admin

from tool.models import Category, Tool

admin.site.register(Category)


class ToolAdmin(admin.ModelAdmin):
    list_display = ["name", "rent_price"]


admin.site.register(Tool, ToolAdmin)
