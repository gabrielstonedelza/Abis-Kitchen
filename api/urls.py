from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('all-food/', views.AllFoodView.as_view()),
    path('reviews/', views.AllReviews.as_view()),
    path('food-reviews/', views.AllFoodReviews.as_view()),
    path('food-detail<int:food>/', views.food_detail_images),
    path('add_to_cart/<str:slug>/', views.add_to_cart),
    path('remove_from_cart/<int:pk>/', views.remove_from_cart),
    path('clear_car/', views.clear_cart),
    path('cart_item_count/', views.cart_item_count),
    path('get_my_cart_items/', views.get_my_cart_items),
#     favorites
    path('add_to_favorites/',views.add_to_favorites),
    path('get_my_favorites/',views.get_my_favorites),

]