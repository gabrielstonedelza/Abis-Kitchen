from django.shortcuts import render,get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import User, Profile
from .serializers import UsersSerializer, ProfileSerializer