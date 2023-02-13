from django.contrib import admin

from .models import Food, FoodImages, Notifications

admin.site.register(Food)
admin.site.register(FoodImages)
admin.site.register(Notifications)
