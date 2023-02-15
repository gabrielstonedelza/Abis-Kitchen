from rest_framework import serializers
from .models import Food, FoodImages, Notifications, Reviews, FoodReviews, PrivateUserMessage,Order, OrderItem

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id','name','category','price','image','views','ingredients','date_created', 'slug', 'dish_type','get_food_image']


class FoodImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImages
        fields = ['id','food','image','date_created','get_food_name','img_address']
        # read_only_fields = ['food']

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['id','notification_id','notification_title','notification_message','read','notification_trigger','notification_from','notification_to','new_added_food_id','new_order_id','completed_order_id','review_id','reply_id','rating_id','payment_confirmed_id','date_created']



class PrivateUserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateUserMessage
        fields = ['id', 'sender', 'receiver', 'private_chat_id', 'message', 'read', 'get_date',
                  'get_senders_username', 'get_receivers_username', 'timestamp', 'isSender', 'isReceiver']


class FoodReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodReviews
        fields = ['id','food','user','review','date_added','get_food_name','get_username']
        read_only_fields = ['user','food']


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id','user','review','date_added','get_username']
        read_only_fields = ['user']


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','user','food', 'date_ordered', 'get_order_item_price', 'get_order_item_category','get_order_item_image','quantity','get_usernames','ordered','get_total_order_price']
        read_only_fields = ['user','food']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user','ordered_foods','date_ordered','ordered','get_username','get_user_ordering_profile_picture']
        read_only_fields = ['user']