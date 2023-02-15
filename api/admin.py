from django.contrib import admin

from .models import Food, FoodImages, Notifications, Order, OrderItem

admin.site.register(Food)
admin.site.register(FoodImages)
admin.site.register(Notifications)
admin.site.register(Order)
admin.site.register(OrderItem)
