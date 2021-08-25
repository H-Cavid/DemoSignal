from django.contrib.auth.models import User
from.models import *
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,*args,**kwargs):
    if created is True:
        Profile.objects.create(user=instance)
        print("Profile is created")

# post_save.connect(create_profile,sender=User)#her ikisi eyni seydi

@receiver(post_save,sender=User)
def uptade_profile(sender,instance,created,*args,**kwargs):
    if created is False:
        instance.profile.save()
        print('Profile is updated')

# post_save.connect(uptade_profile,sender=User)