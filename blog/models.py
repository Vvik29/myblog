from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Post(models.Model):
    # аттрибут в классе = колонка в таблице
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.URLField(default="http://placehold.it/900x300")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Автор')

    def __str__(self):
        return self.title








# Create your models here.
