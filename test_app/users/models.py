import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


from shop.models import Shop
from .constants import ROLE_CHOICES, USER


class User(AbstractUser):

    app_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    role = models.IntegerField(choices=ROLE_CHOICES, default=USER)
    is_confirmed = models.BooleanField(default=False)
    shop = models.ForeignKey(Shop, blank=True, null=True, related_name='user',
                             on_delete=models.SET_NULL)

    def confirm_registration(self, token):

        if self.app_id != token:
            return False
        self.is_confirmed = True
        self.save()
        return True

    def __str__(self):
        return f'{self.app_id}:{self.username}'
