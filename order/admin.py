from django.contrib import admin

from order.models import Order, OrderItem

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['id', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['first_name', 'last_name', 'address']
