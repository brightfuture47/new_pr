import email
from email.policy import default
from pyexpat import model
import uuid

from django.db import models
from django.core import validators


class Author(models.Model):

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering =['id']
        unique_together = ('name','age')

    TYPES = (
        ('a','foreign'),
        ('b','domestic'),
        ('c','other'),
    )

    id = models.UUIDField (primary_key = True, db_index=True, default=uuid.uuid4)

    name = models.CharField (
        verbose_name='Имя автора',
        max_length=200,
        validators=[validators.RegexValidator(regex='^.*er$', message='Wrong')]
        )

    age = models.PositiveIntegerField (verbose_name='Возраст автора') 
    email = models.EmailField (verbose_name='Почта автора')
    lit_type = models.CharField (max_length=1, verbose_name= 'Тип литературы', choices=TYPES, default='a')

    def __str__(self):
        return self.name


class Book(models.Model):

    class Meta:
        get_latest_by='published'

    title = models.CharField (max_length=200)
    description = models.TextField ()
    page_num = models.PositiveIntegerField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
