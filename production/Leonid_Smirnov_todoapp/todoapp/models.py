from django.db import models
from userapp.models import User

# Create your models here.


class Project(models.Model):
    name = models.CharField(verbose_name='название проекта', max_length=64)
    repo_url = models.URLField(verbose_name='ссылка на репозиторий', blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'


class ToDo(models.Model):
    project = models.ForeignKey(Project, models.CASCADE, verbose_name='связанный проект', related_name='project')
    text = models.TextField(verbose_name='текст заметки')
    created = models.DateTimeField(verbose_name='создана', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлена', auto_now=True)
    user = models.ForeignKey(User, models.PROTECT, verbose_name='создал пользователь', related_name='creator')
    is_active = models.BooleanField(db_index=True, default=True)
