from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Food, Notifications, PrivateUserMessage, Reviews, FoodReviews
from django.conf import settings

from users.models import User

@receiver(post_save,sender=Food)
def alert_new_food(sender,created,instance,**kwargs):
    title = "Food Menu Updated"
    message = "Abi's Kitchen added to their food menu"
    users = User.objects.exclude(id=1)
    admin = User.objects.get(id=1)

    if created:
        for i in users:
            Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                          notification_message=message,notification_from=admin,notification_to=i,new_added_food_id=instance.id)

@receiver(post_save, sender=PrivateUserMessage)
def alert_private_message(sender, created, instance, **kwargs):
    title = f"New private message"

    if created:
        if instance.sender:
            message = f"{instance.sender.username} sent you a message"
            Notifications.objects.create(item_id=instance.id, notification_title=title,
                                         notification_message=message, notification_to=instance.receiver,private_message_id=instance.id)
        if instance.receiver:
            message = f"{instance.receiver.username} sent you a message"
            Notifications.objects.create(item_id=instance.id, notification_title=title,
                                         notification_message=message, notification_to=instance.sender,private_message_id=instance.id)


@receiver(post_save,sender=Reviews)
def alert_review(sender,created,instance,**kwargs):
    title = "New Review"
    message = f"You have a new review from  {instance.user.username}."
    admin = User.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.user, notification_to=admin,
                                     review_id=instance.id)


@receiver(post_save, sender=FoodReviews)
def alert_food_review(sender, created, instance, **kwargs):
    title = "New Food Review"
    message = f"{instance.food.name} got a new review from  {instance.user.username}."
    admin = User.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.user, notification_to=admin,
                                     food_review_id=instance.id)

