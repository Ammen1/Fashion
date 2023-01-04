import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.utils.translation import gettext_lazy as _
# from customer.models import UserProfile


class CustomAccountManager(BaseUserManager):


    def create_superuser(self, email, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, name, password, **other_fields)

    def create_user(self, email, name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user
   

class User(AbstractBaseUser, PermissionsMixin):
    user_type_data = ( (1, "Designer"), (2,"UserProfile"))
    user_type = models.CharField(default=2, choices=user_type_data, max_length=10)
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'abushguda214@gmail.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.name




# class Manager(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     address = models.CharField(verbose_name="Address",max_length=100, null=True, blank=True)   
#     town = models.CharField(verbose_name="Town/City",max_length=100, null=True, blank=True)
#     county = models.CharField(verbose_name="County",max_length=100, null=True, blank=True)
#     post_code = models.CharField(verbose_name="Post Code",max_length=8, null=True, blank=True)
#     country = models.CharField(verbose_name="Country",max_length=100, null=True, blank=True)
#     longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
#     latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)
#     delivery_instructions = models.CharField(_("Delivery Instructions"), max_length=255)
#     gender = models.CharField(max_length=50)
#     profile_pic = models.FileField()
#     captcha_score = models.FloatField(default = 0.0)
#     has_profile = models.BooleanField(default = False)
#     is_active = models.BooleanField(default = True)

#     objects = CustomAccountManager()


#     def __str__(self):
#         return f'{self.user}'



class Designer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(verbose_name="Address",max_length=100, null=True, blank=True)   
    town = models.CharField(verbose_name="Town/City",max_length=100, null=True, blank=True)
    county = models.CharField(verbose_name="County",max_length=100, null=True, blank=True)
    post_code = models.CharField(verbose_name="Post Code",max_length=8, null=True, blank=True)
    country = models.CharField(verbose_name="Country",max_length=100, null=True, blank=True)
    longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
    latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)
    delivery_instructions = models.CharField(_("Delivery Instructions"), max_length=255)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    captcha_score = models.FloatField(default = 0.0)
    has_profile = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    objects = CustomAccountManager()


    def __str__(self):
        return f'{self.user}'



class UserProfile(models.Model):
    

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(verbose_name="Address",max_length=100, null=True, blank=True)   
    town = models.CharField(verbose_name="Town/City",max_length=100, null=True, blank=True)
    county = models.CharField(verbose_name="County",max_length=100, null=True, blank=True)
    post_code = models.CharField(verbose_name="Post Code",max_length=8, null=True, blank=True)
    country = models.CharField(verbose_name="Country",max_length=100, null=True, blank=True)
    longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
    latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)
    delivery_instructions = models.CharField(_("Delivery Instructions"), max_length=255)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    captcha_score = models.FloatField(default = 0.0)
    has_profile = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)




    def __str__(self):
        return f'{self.user}'











#Creating Django Signals


@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        # if instance.user_type == 1:
        #     Manager.objects.create(admin=instance)
        if instance.user_type == 1:
            Designer.objects.create(admin=instance)
        if instance.user_type == 2:
            UserProfile.objects.create(admin=instance)


def save_user_profile(sender , instance , **kwargs):
    # if instance.user_type == 1:
    #     instance.manager.save()

    if instance.user_type == 1:
        instance.designer.save()
    if instance.user_type == 2:
        instance.userProfile.save()
