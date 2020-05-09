from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    dni = models.IntegerField(verbose_name=_("Número de identificación"),
                            blank=False, null=False, unique=True)
    phone = models.PositiveIntegerField(verbose_name=_("Número telefonico"),
                            unique=True, blank=True, null=True)
    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.dni