from django.db.models.signals import post_save
# decorador
from django.dispatch import receiver
from django.contrib.auth.models import User
from app_user.models import UserData


@receiver(post_save, sender=User)
def create_userdata(sender, instance, created, **kwargs):
    if created:
        UserData.objects.create(user=instance)
        print("Se ejecutó la creación del usuario")


@receiver(post_save, sender=User)
def update_userdata(sender, instance, created, **kwargs):
    if created == False:
        instance.userdata.save()
    print("Se actualizaron los datos del usuario")


"""pre_save
post_save
@receiver"""
