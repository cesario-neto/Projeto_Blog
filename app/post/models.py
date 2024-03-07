from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User
from django_summernote.models import AbstractAttachment
from utils.image import resize_image


class Category(BaseModel):
    name = models.CharField(verbose_name='Nome',
                            max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name

        if self.file:
            resize_image(self.file, 900)

        return super().save(*args, **kwargs)


class Post(BaseModel):
    title = models.CharField(verbose_name='Título',
                             max_length=250, blank=False, null=False,)
    slug = models.SlugField(unique=True, blank=False, null=False,)
    banner = models.ImageField(
        verbose_name='Capa', upload_to='posts/%Y/%m/%d', blank=True, null=True)
    description = models.TextField(
        verbose_name='Descrição', blank=False, null=False,)
    content = models.TextField(verbose_name='Conteúdo',)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name='Categoria', null=False, blank=False)
    is_publishe = models.BooleanField(verbose_name='Publicado', default=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Autor')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super_save = super().save(*args, **kwargs)
        if self.banner:
            resize_image(self.banner, 1200)
        return super_save
