from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(
        verbose_name='Identificador',
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid4
    )

    created_at = models.DateTimeField(
        verbose_name='Criado ás',
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        verbose_name='Editado ás',
        auto_now=True,
    )

    class Meta:
        abstract = True
        ordering = ['-created_at']
