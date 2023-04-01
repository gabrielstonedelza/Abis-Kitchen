from django.contrib import admin

from .models import Food, FoodImages, Notifications, Order, OrderItem, AddToFavorites, Reviews, FoodReviews

admin.site.register(Food)
admin.site.register(Reviews)
admin.site.register(FoodReviews)
admin.site.register(AddToFavorites)
admin.site.register(FoodImages)
admin.site.register(Notifications)
admin.site.register(Order)
admin.site.register(OrderItem)
