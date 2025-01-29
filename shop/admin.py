from django.contrib import admin
from .models import Category, MenuItem

# Register your models here.

def set_status_false(modeladmin, request, queryset):
    rows_updated = queryset.update(status=False)
    modeladmin.message_user(request, f"{rows_updated} items status set to False")

def set_status_true(modeladmin, request, queryset):
    rows_updated = queryset.update(status=True)
    modeladmin.message_user(request, f"{rows_updated} items status set to True")

set_status_false.short_description = "set status to False"
set_status_true.short_description = "set status to True"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'items_count')
    search_fields = ('title', )
    actions = (set_status_false, set_status_true)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'status')
    search_fields = ('title', 'description')
    list_filter = ('price', 'categories')
    actions = (set_status_false, set_status_true)


admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
