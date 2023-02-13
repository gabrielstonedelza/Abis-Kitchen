from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('all-food/', views.AllFoodView.as_view()),
    path('reviews/', views.AllReviews.as_view()),
    path('food-reviews/', views.AllFoodReviews.as_view()),
    path('food-detail<int:food>/', views.food_detail_images)
]