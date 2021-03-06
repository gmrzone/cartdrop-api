# Generated by Django 3.2.5 on 2021-08-05 21:40

import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models

import cartdrop.accounts.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CartDropUser",
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
                    "number",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        error_messages={
                            "unique": "This number is already registered with us please try logging in"
                        },
                        max_length=10,
                        unique=True,
                        verbose_name="Mobile Number",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "unique": "A user with this email already exist"
                        },
                        max_length=50,
                        unique=True,
                        verbose_name="Email address",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exist"
                        },
                        help_text="Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=50,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="Username",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        db_index=True,
                        default="CUSTOMER",
                        max_length=100,
                        verbose_name="user type",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=25, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=25, verbose_name="last name"
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date_joined"
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        default="default_profilepic.png",
                        upload_to=cartdrop.accounts.utils.user_photo_location,
                        verbose_name="profile picture",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin panel.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether this user should be treated as active. set this to false this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "is_email_verified",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user has verified their email",
                        verbose_name="email verified",
                    ),
                ),
                (
                    "is_number_verified",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user has verified their number",
                        verbose_name="email verified",
                    ),
                ),
                (
                    "is_disabled",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user account has been disabled",
                        verbose_name="disabled",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
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
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
        ),
        migrations.CreateModel(
            name="SellerUser",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("accounts.cartdropuser",),
        ),
    ]
