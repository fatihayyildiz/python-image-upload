from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


def upload_to(instance, filename):
    return 'collectedImages/{filename}'.format(filename=filename)


class BaseImageModel(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='collectedImages/no_name300x300.jpg')
    width = models.FloatField(name='width', default=0)
    height = models.FloatField(name='height', default=0)
    url = models.CharField(max_length=255)
    alt = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        return super(BaseImageModel, self).save(*args, **kwargs)


class Image(BaseImageModel):
    pass
