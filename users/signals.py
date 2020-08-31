from django.db.models.signals import post_save #signal that get fired after an object is saved
from django.contrib.auth.models import User #User model is here what we call the sender(what is sending signal)
from django.dispatch import receiver #reciever is a function gets that signals and perform some task
from .models import Profile #We need to import profiles from models since we are creating profile in our function
#Now we have all imported we can tie them all togather reason we are doing this because we want a user profile to be created for each new user.
@receiver(post_save, sender=User) #We want to run create_profile function every time when user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#this function will be called when user is saved
@receiver(post_save, sender=User) #We want to run create_profile function every time when user is created
def save_profile(sender, instance, **kwargs): # **kwargs just accept any additional keyword argument in the function
    instance.profile.save()
