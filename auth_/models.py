from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import OneToOneField


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, login, password, first_name='', last_name='', **extra_fields):
        user = self.model(login=login, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, password, first_name, last_name):
        user = self._create_user(login, password, first_name, last_name)
        profile = Profile.objects.get_or_create(user=user)
        print(profile)
        return user

    def create_superuser(self, login, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(login, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=100, unique=True, verbose_name='Логин')
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'login'

    objects = UserManager()


class Profile(models.Model):
    ROLES_CHOICES = (('S', 'SuperAdmin'), ('G', 'Guest'))

    user = OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(choices=ROLES_CHOICES, max_length=1, default='G')
    avatar = models.ImageField(upload_to='user_images', null=True, blank=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=150, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    family_status = models.CharField(max_length=250, null=True, blank=True)
    school = models.CharField(max_length=250, null=True, blank=True)
    university = models.CharField(max_length=250, null=True, blank=True)
    job = models.CharField(max_length=250, null=True, blank=True)
    fav_music = models.CharField(max_length=250, null=True, blank=True)
    fav_movies = models.CharField(max_length=250, null=True, blank=True)
    fav_books = models.CharField(max_length=250, null=True, blank=True)
