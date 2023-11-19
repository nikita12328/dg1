from django.contrib import admin
from .models import Product, Order, User


@admin.action(description="Сбросить количество в ноль")
def reset_price(modeladmin, request, queryset):
    queryset.update(price=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image']
    list_editable = ['price', 'description']
    list_filter = ['price']
    search_fields = ['name', 'description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    ordering = ['price']
    actions = [reset_price]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered']
    list_filter = ['date_ordered']
    search_fields = ['customer__name', 'customer__email']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
