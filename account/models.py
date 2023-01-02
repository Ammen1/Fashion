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


class CustomAccountManager(BaseUserManager):
    user_type_data = ((1, "Manager"), (2, "Designer"), (3,"Customer"))
    user_type = models.CharField(default=3, choices=user_type_data, max_length=10)


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

    def create_user(self, user_type, email, name, password, **other_fields):
        if user_type == 1:
            if not email:
                raise ValueError(_('You must provide an email address'))
            email = self.normalize_email(email)
            manager = self.model(email=email,name=name, **other_fields) 
            manager.set_password(password)
            manager.save()
            return manager   

        if user_type == 2:
            if not email:
                raise ValueError(_('You must provide an email address'))
            email = self.normalize_email(email)
            designer = self.model(email=email, name=name,
                          **other_fields)
            designer.set_password(password)
            designer.save()
            return designer
        if user_type == 3:
            if not email:
                raise ValueError(_('Yuo muset provide ana emai and address'))
            email = self.normalize_email(email)
            customer = self.model(email=email, name=name,
                          **other_fields)
            customer.set_password(password)
            customer.save()
            return customer

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # email = models.EmailField(_('email address'), unique=True)
    firist_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # objects = CustomAccountManager()

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    # class Meta:
    #     verbose_name = "User"
    #     verbose_name_plural = "Users"

    # def email_user(self, subject, message):
    #     send_mail(
    #         subject,
    #         message,
    #         'abushguda214@gmail.com',
    #         [self.email],
    #         fail_silently=False,
    #     )

    # def __str__(self):
    #     return self.name

class Address(models.Model):
    """
    Address
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    full_name = models.CharField(_("Full Name"), max_length=150)
    phone = models.CharField(_("Phone Number"), max_length=50)
    postcode = models.CharField(_("Postcode"), max_length=50)
    address_line = models.CharField(_("Address Line 1"), max_length=255)
    address_line2 = models.CharField(_("Address Line 2"), max_length=255)
    town_city = models.CharField(_("Town/City/State"), max_length=150)
    delivery_instructions = models.CharField(_("Delivery Instructions"), max_length=255)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    default = models.BooleanField(_("Default"), default=False)
    objects = CustomAccountManager()

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return "Address"



class Manager(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CustomAccountManager()



class Designer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE, verbose_name="Address",max_length=100, null=True, blank=True)
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




class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, verbose_name="Address", related_name="address" , max_length=100, null=True, blank=True)
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




#Creating Django Signals


@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        if instance.user_type == 1:
            Manager.objects.create(admin=instance)
        if instance.user_type == 2:
            Designer.objects.create(admin=instance,addres_id=Address.objects.get(id=1),address="", profile_pic="",gender="")
        if instance.user_type == 3:
            Customer.objects.create(admin=instance,addres_id=Address.objects.get(id=1),address="", profile_pic="",gender="")


def save_user_profile(sender , instance , **kwargs):
    if instance.user_type == 1:
        instance.manager.save()

    if instance.user_type == 2:
        instance.designer.save()

    if instance.user_type == 3:
        instance.custpmer.save()