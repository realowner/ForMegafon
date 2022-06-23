from django.db import models


class Authors(models.Model):
    full_name = models.CharField(max_length=100, unique=True, verbose_name='ФИО')
    country = models.CharField(max_length=30, verbose_name='Страна')
    books = models.ManyToManyField('Books', blank=True, related_name='authors')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлена')
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['full_name']
        

class Books(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название')
    desc = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлена')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']