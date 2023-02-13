from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework.views import APIView
from datetime import datetime, date, time, timedelta
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Food, FoodImages, Reviews, FoodReviews, PrivateUserMessage
from .serializers import FoodSerializer, FoodImagesSerializer,ReviewsSerializer,FoodReviewsSerializer,PrivateUserMessageSerializer

class AllFoodView(generics.ListCreateAPIView):
    queryset =  Food.objects.all().order_by('-date_created')
    serializer_class = FoodSerializer
    permission_classes = [AllowAny]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)

class AllReviews(generics.ListCreateAPIView):
    queryset =  Reviews.objects.all().order_by('-date_added')
    serializer_class = ReviewsSerializer
    permission_classes = [AllowAny]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ReviewsSerializer(queryset, many=True)
        return Response(serializer.data)

class AllFoodReviews(generics.ListCreateAPIView):
    queryset =  FoodReviews.objects.all().order_by('-date_added')
    serializer_class = FoodReviewsSerializer
    permission_classes = [AllowAny]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = FoodReviewsSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_food_menu(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_food_detail(request):
    serializer = FoodImagesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def food_detail(request,slug):
    food = get_object_or_404(Food,slug=slug)
    serializer = FoodSerializer(food,many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def food_detail_images(request,food):
    food = FoodImages.objects.filter(food=food)
    serializer = FoodSerializer(food,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_review(request):
    serializer = Reviews(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_food_review(request,slug):
    food = get_object_or_404(Food,slug=slug)
    serializer = Reviews(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user,food=food)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)