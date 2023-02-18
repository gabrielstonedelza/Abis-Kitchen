from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.humanize.templatetags import humanize

from users.models import User, Profile

DeUser = settings.AUTH_USER_MODEL

FOOD_CATEGORY = (
    ("Local", "Local"),
    ("Continental", "Continental"),
    ("Sea Food", "Sea Food"),
    ("Breakfast", "Breakfast"),
    ("Vegetarian", "Vegetarian"),
)

READ_STATUS = (
    ("Read", "Read"),
    ("Not Read", "Not Read"),
)

NOTIFICATIONS_STATUS = (
    ("Read", "Read"),
    ("Not Read", "Not Read"),
)

NOTIFICATIONS_TRIGGERS = (
    ("Triggered", "Triggered"),
    ("Not Triggered", "Not Triggered"),
)

ORDER_STATUS = (
    ("Preparing", "Preparing"),
    ("Finished", "Finished"),
)

DISH_CATEGORY = (
    ("Special", "Special"),
    ("Regular", "Regular"),
)

class Food(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=FOOD_CATEGORY, default="Local")
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    image = models.ImageField(upload_to='images/food', blank=True,)
    views = models.IntegerField(default=0)
    dish_type = models.CharField(max_length=255,default="Special",choices=DISH_CATEGORY)
    ingredients = models.CharField(max_length=200, blank=True,)
    slug = models.SlugField(max_length=100, default='', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_food_image(self):
        if self.image:
            return "https://abiskitchen.xyz/"+self.image.url
        return ""

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class FoodImages(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/food/detail', blank=True)
    img_address = models.CharField(max_length=255,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.food.name

    def get_detail_food_image(self):
        if self.image:
            return "http://127.0.0.1:8000"+self.image.url
        return ""

    def get_food_name(self):
        return self.food.name

class OrderItem(models.Model):
    user = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name='UserOrdering')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.food.name

    def get_total_order_price(self):
        return self.quantity * self.food.price

    def get_total_price(self):
        return self.get_total_order_price()

    def get_usernames(self):
        return self.user.username

    def get_order_item_price(self):
        return self.food.price

    def get_order_item_category(self):
        return self.food.category

    def get_order_item_image(self):
        if self.food.image:
            return "http://127.0.0.1:8000" + self.food.image.url
        return ""


class Order(models.Model):
    user = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    ordered_foods = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.ordered_foods.all():
            total += order_item.get_total_price()
        return total

    def get_username(self):
        return self.user.username

    def get_user_ordering_profile_picture(self):
        user = User.object.get(username=self.user.username)
        u_profile = Profile.objects.get(user=user)
        if u_profile:
            return "http://127.0.0.1:8000" + u_profile.profile_pic.url
        return ""


class Reviews(models.Model):
    user = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    review = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

class FoodReviews(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="food_reviews")
    user = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    review = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.food.name

    def get_food_name(self):
        return self.food.name

    def get_username(self):
        return self.user.username

class PrivateUserMessage(models.Model):
    sender = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    receiver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="chatter2")
    private_chat_id = models.CharField(max_length=400, blank=True)
    message = models.TextField()
    read = models.BooleanField(default=False)
    isSender = models.BooleanField(default=False)
    isReceiver = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.private_chat_id

    def get_senders_username(self):
        return self.sender.username

    def get_receivers_username(self):
        return self.receiver.username

    def get_date(self):
        return humanize.naturaltime(self.timestamp)

    def save(self, *args, **kwargs):
        senders_username = self.sender.username
        receiver_username = self.receiver.username
        sender_receiver = str(senders_username) + str(receiver_username)
        receiver_sender = str(receiver_username) + str(senders_username)

        self.private_chat_id = sender_receiver

        super().save(*args, **kwargs)

class Notifications(models.Model):
    notification_id = models.CharField(max_length=100, blank=True, default="")
    notification_title = models.CharField(max_length=255, blank=True)
    notification_message = models.TextField(blank=True)
    read = models.CharField(max_length=20, choices=NOTIFICATIONS_STATUS, default="Not Read")
    notification_trigger = models.CharField(max_length=255, choices=NOTIFICATIONS_TRIGGERS, default="Triggered",
                                            blank=True)
    notification_from = models.ForeignKey(DeUser, on_delete=models.CASCADE, null=True)
    notification_to = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="DeUser_receiving_notification", null=True)
    new_added_food_id = models.CharField(max_length=255, blank=True)
    new_order_id = models.CharField(max_length=255, blank=True)
    completed_order_id = models.CharField(max_length=255, blank=True)
    review_id = models.CharField(max_length=255, blank=True, default='')
    food_review_id = models.CharField(max_length=255, blank=True, default='')
    private_message_id = models.CharField(max_length=255, blank=True, default='')
    reply_id = models.CharField(max_length=255, blank=True)
    rating_id = models.CharField(max_length=255, blank=True)
    payment_confirmed_id = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_title

    def get_notification_from_username(self):
        return self.notification_from.username

    def get_notification_to_username(self):
        return self.notification_to.username

    def get_notification_from_profile_pic(self):
        user = User.object.get(username=self.notification_from.username)
        u_profile = Profile.objects.get(user=user)
        if u_profile:
            return "http://127.0.0.1:8000"+u_profile.profile_pic.url
        return ""

    def get_notification_to_profile_pic(self):
        user = User.object.get(username=self.notification_to.username)
        u_profile = Profile.objects.get(user=user)
        if u_profile:
            return "http://127.0.0.1:8000"+u_profile.profile_pic.url
        return ""