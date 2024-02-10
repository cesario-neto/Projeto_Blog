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


class SiteSetup(BaseModel):
    favicon = models.ImageField(
        verbose_name='Favicon',
        upload_to='favicon/%Y/%m/%d',
        blank=False,
        null=False
    )
    logo = models.ImageField(
        verbose_name='Logo',
        upload_to='logo/%Y/%m/%d',
        blank=False,
        null=False
    )

    links_groups = models.ManyToManyField('LinkGroup')

    class Meta:
        verbose_name = 'Configuração do Site'
        verbose_name_plural = 'Configurações do Site'

    def __str__(self) -> str:
        return 'Configuração do site'


class LinkGroup(BaseModel):
    title = models.CharField(
        verbose_name='Título',
        max_length=100,
        unique=True
    )

    links = models.ManyToManyField('Link')

    class Meta:
        verbose_name = 'Grupo de link'
        verbose_name_plural = 'Grupos de links'

    def __str__(self):
        return self.title


class Link(BaseModel):
    name = models.CharField(verbose_name='Nome',
                            blank=False, null=False, max_length=200)
    url = models.URLField(unique=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return self.name
