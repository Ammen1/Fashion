# Generated by Django 4.1.5 on 2023-01-10 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "user_type",
                    models.CharField(
                        choices=[(1, "SYADMIN"), (2, "Designer"), (3, "Customer")],
                        default=2,
                        max_length=10,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("mobile", models.CharField(blank=True, max_length=20)),
                ("is_active", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Accounts",
                "verbose_name_plural": "Accounts",
            },
        ),
        migrations.CreateModel(
            name="SYADMIN",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "admin",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Designer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Address"
                    ),
                ),
                (
                    "town",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Town/City"
                    ),
                ),
                (
                    "county",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="County"
                    ),
                ),
                (
                    "post_code",
                    models.CharField(
                        blank=True, max_length=8, null=True, verbose_name="Post Code"
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Country"
                    ),
                ),
                (
                    "longitude",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Longitude"
                    ),
                ),
                (
                    "latitude",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Latitude"
                    ),
                ),
                (
                    "delivery_instructions",
                    models.CharField(
                        max_length=255, verbose_name="Delivery Instructions"
                    ),
                ),
                ("gender", models.CharField(max_length=50)),
                ("profile_pic", models.FileField(upload_to="")),
                ("captcha_score", models.FloatField(default=0.0)),
                ("has_profile", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "admin",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("mobile", models.CharField(blank=True, max_length=20)),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Address"
                    ),
                ),
                (
                    "town",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Town/City"
                    ),
                ),
                (
                    "county",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="County"
                    ),
                ),
                (
                    "post_code",
                    models.CharField(
                        blank=True, max_length=8, null=True, verbose_name="Post Code"
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Country"
                    ),
                ),
                (
                    "longitude",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Longitude"
                    ),
                ),
                (
                    "latitude",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Latitude"
                    ),
                ),
                ("is_active", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "admin",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
        ),
    ]
