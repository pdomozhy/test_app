import uuid
from django.db import models


class Shop(models.Model):

    shop_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.shop_id}:{self.name}'
