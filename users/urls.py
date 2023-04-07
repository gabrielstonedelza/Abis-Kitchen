from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name="index.html")),
    path('activate/<uid>/<token>/',TemplateView.as_view(template_name="index.html")),
    path('password/reset/confirm/<uid>/<token>/',TemplateView.as_view(template_name="index.html")),
    path('email/reset/confirm/<uid>/<token>/',TemplateView.as_view(template_name="index.html")),
    path('get_user_details/', views.get_user),
    path('get_user_profile/', views.user_profile),
    path('profile/update/', views.update_profile),
    path('user_details/update/', views.update_user_details),
]