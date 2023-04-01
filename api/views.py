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
from django.http import Http404
from .models import Food, FoodImages, Reviews, FoodReviews, PrivateUserMessage, Order, OrderItem, AddToFavorites, Notifications
from .serializers import FoodSerializer, FoodImagesSerializer,ReviewsSerializer,FoodReviewsSerializer,PrivateUserMessageSerializer, OrderItemsSerializer, OrderSerializer,AddToFavoriteSerializer,NotificationsSerializer

class AllFoodView(generics.ListCreateAPIView):
    queryset =  Food.objects.exclude(category="Side").order_by('-date_created')
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)

class AllReviews(generics.ListCreateAPIView):
    queryset =  Reviews.objects.all().order_by('-date_added')
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ReviewsSerializer(queryset, many=True)
        return Response(serializer.data)

class AllFoodReviews(generics.ListCreateAPIView):
    queryset =  FoodReviews.objects.all().order_by('-date_added')
    serializer_class = FoodReviewsSerializer
    permission_classes = [IsAuthenticated]

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
@permission_classes([permissions.IsAuthenticated])
def food_detail(request,slug):
    food = get_object_or_404(Food,slug=slug)
    serializer = FoodSerializer(food,many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
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

# for order and order items
@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_cart(request,slug):
    food = get_object_or_404(Food, slug=slug)
    serializer = OrderItemsSerializer(data=request.data)
    if serializer.is_valid():
        if not OrderItem.objects.filter(food=food).filter(user=request.user).exists():
            serializer.save(user=request.user,food=food)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def remove_from_cart(request, pk):
    try:
        item = OrderItem.objects.get(pk=pk)
        item.delete()
    except OrderItem.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def clear_cart(request):
    items = OrderItem.objects.filter(user=request.user)
    for item in items:
        item.delete()
    serializer = OrderItemsSerializer(items,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_cart_items(request):
    my_cart = OrderItem.objects.filter(user=request.user).order_by('-date_ordered')
    serializer = OrderItemsSerializer(my_cart,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def cart_item_count(request):
    items = Order.objects.filter(user=request.user,ordered=False)
    serializer = OrderSerializer(items, many=True)
    return Response(serializer.data)

# favorites
@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_favorites(request,slug):
    food = get_object_or_404(Food, slug=slug)
    serializer = AddToFavoriteSerializer(data=request.data)
    if serializer.is_valid():
        if not AddToFavorites.objects.filter(food=food).filter(user=request.user).exists():
            serializer.save(user=request.user,food=food)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_favorites(request):
    favorites = AddToFavorites.objects.filter(user=request.user).order_by('-date_added')
    serializer = AddToFavoriteSerializer(favorites, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def remove_from_favorites(request, pk):
    try:
        favorite = AddToFavorites.objects.get(pk=pk)
        favorite.delete()
    except AddToFavorites.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def clear_favorites(request):
    items = AddToFavorites.objects.filter(user=request.user)
    for item in items:
        item.delete()
    serializer = AddToFavoriteSerializer(items,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_notifications(request):
    notifications = Notifications.objects.filter(notification_to=request.user).order_by('date_created')[:50]
    serializer = NotificationsSerializer(notifications,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_unread_notifications(request):
    notifications = Notifications.objects.filter(notification_to=request.user).filter(read="Not Read").order_by('date_created')
    serializer = NotificationsSerializer(notifications,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def read_notification(request):
    notifications = Notifications.objects.filter(notification_to=request.user).filter(
        read="Not Read").order_by('-date_created')
    for i in notifications:
        i.read = "Read"
        i.save()

    serializer = NotificationsSerializer(notifications, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def increase_item_quantity(request,id,slug):
    food = get_object_or_404(Food, slug=slug)
    order = get_object_or_404(OrderItem, id=id)
    serializer = OrderItemsSerializer(data=request.data)
    if serializer.is_valid():
        order.quantity += 1
        order.save()
        # serializer.save(user=request.user, food=food)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def decrease_item_quantity(request,id,slug):
    food = get_object_or_404(Food, slug=slug)
    order = get_object_or_404(OrderItem, id=id)
    serializer = OrderItemsSerializer(data=request.data)
    if serializer.is_valid():
        order.quantity -= 1
        order.save()
        # serializer.save(user=request.user, food=food)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllSidesFoodView(generics.ListCreateAPIView):
    queryset =  Food.objects.filter(category="Side").order_by('-date_created')
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_food_reviews(request,slug):
    food = get_object_or_404(Food,slug=slug)
    review = FoodReviews.objects.filter(food=food).order_by('-date_added')
    serializer = FoodReviewsSerializer(review,many=True)
    return Response(serializer.data)

# reviews
@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_food_review(request,slug):
    food = get_object_or_404(Food, slug=slug)
    serializer = FoodReviewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, food=food)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_review(request,slug):
    serializer = ReviewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
