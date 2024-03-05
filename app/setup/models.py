from django.db import models
from core.models import BaseModel


class SiteSetup(BaseModel):
    favicon = models.ImageField(
        verbose_name='Favicon', upload_to='favicon/%Y/%m/%d',
        blank=False, null=False)
    logo = models.ImageField(verbose_name='Logo', upload_to='logo/%Y/%m/%d',
                             blank=False, null=False)
    footer_text = models.CharField(
        verbose_name='Texto do footer', max_length=200)

    class Meta:
        verbose_name = 'Configuração do Site'
        verbose_name_plural = 'Configurações do Site'

    def __str__(self) -> str:
        return 'Configuração do site'
