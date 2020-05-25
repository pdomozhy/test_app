import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


from .constants import ROLE_CHOICES, USER


class User(AbstractUser):

    app_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    role = models.IntegerField(choices=ROLE_CHOICES, default=USER)
    is_confirmed = models.BooleanField(default=False)

    def confirm_registration(self, token):

        if self.app_id != token:
            return False
        self.is_confirmed = True
        self.save()
        return True
