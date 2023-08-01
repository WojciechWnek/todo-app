from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.


class AppUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.create_user(
            email=email, username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()

    def __str__(self):
        return self.username


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(null=True, blank=True, editable=False)
    owner = models.ForeignKey(
        "AppUser", related_name='task', on_delete=models.CASCADE, default=None)

    # Override modles save method with my own
    def save(self, *args, **kwargs):
        if not self._state.adding:
            from datetime import datetime
            self.edited_at = datetime.now()

        super().save(*args, **kwargs)
