from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """
    Define a custom UserManager for this project.
    """
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        """Creates and saves a user with the given email and password."""
        if not email:
            raise ValueError('Users must provide an email.')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):
        """Create and save a regular User."""
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        """Creates and saves a new superuser User."""
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superusers must have \'is_staff\' set to True')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superusers must have \'is_superuser\' set to True')

        return self._create_user(email, password, **kwargs)


class User(AbstractUser):
    """
    Define a custom User model for this project.
    """
    # We don't need a username.
    username = None
    # We prefer a single name field over potentially discriminatory
    # first / last name fields.
    name = models.CharField(_('name'), max_length=255)
    short_name = models.CharField(_('short name'), max_length=255, blank=True, null=True)
    first_name = None
    last_name = None
    # Use email as the unique id for a user.
    email = models.EmailField(_('email'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Use our UserManager.
    objects = UserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.short_name or self.name
