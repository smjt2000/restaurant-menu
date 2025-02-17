from django.contrib import admin
from .models import Category, MenuItem

# Register your models here.


def set_status_false(modeladmin, request, queryset):
    """
    changes status of objects to false
    """
    rows_updated = queryset.update(status=False)
    modeladmin.message_user(
        request, f"وضعیت {rows_updated} مورد به عدم نمایش تغییر کرد")


def set_status_true(modeladmin, request, queryset):
    """
    changes status of objects to true
    """
    rows_updated = queryset.update(status=True)
    modeladmin.message_user(
        request, f"وضعیت {rows_updated} مورد به نمایش دادن تغییر کرد")


set_status_false.short_description = "عدم نمایش"
set_status_true.short_description = "نمایش"


class CategoryAdmin(admin.ModelAdmin):
    """
    custom Admin for Category
    """
    list_display = ('title', 'status', 'items_count')
    search_fields = ('title', )
    actions = (set_status_false, set_status_true)


class MenuItemAdmin(admin.ModelAdmin):
    """
    custom Admin for MenuItem
    """
    list_display = ('title', 'description', 'price', 'status')
    search_fields = ('title', 'description')
    list_filter = ('price', 'categories')
    actions = (set_status_false, set_status_true)


admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
