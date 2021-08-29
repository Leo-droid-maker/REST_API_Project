from django.db import models
from userapp.models import User

# Create your models here.


class Project(models.Model):
    name = models.CharField(verbose_name='название проекта', max_length=64)
    repo_url = models.URLField(
        verbose_name='ссылка на репозиторий', blank=True)
    users = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.name


class ToDo(models.Model):
    project = models.ForeignKey(
        Project, models.PROTECT, verbose_name='связанный проект')
    text = models.TextField(verbose_name='текст заметки',
                            max_length=400, blank=True)
    created = models.DateTimeField(
        verbose_name='создана', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлена', auto_now=True)
    user = models.ForeignKey(User, models.PROTECT,
                             verbose_name='создал пользователь', primary_key=True)
    is_active = models.BooleanField(db_index=True, default=True)
