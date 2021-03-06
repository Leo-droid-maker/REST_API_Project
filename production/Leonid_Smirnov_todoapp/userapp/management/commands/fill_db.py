from django.core.management.base import BaseCommand
from userapp.models import User
from todoapp.models import Project, ToDo
from random import choice
from django.contrib.auth.hashers import make_password
from mixer.backend.django import mixer


class Command(BaseCommand):
    help = 'create users to test and one superuser'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        User.objects.all().delete()
        Project.objects.all().delete()
        ToDo.objects.all().delete()
        count = options['count']

        users = mixer.cycle(count).blend(User, password=make_password(f'{mixer.FAKE}'))

        print(f'user {users} created')

        for _ in range(10):
            user = choice(users)
            project = mixer.blend(Project, users=[user])

        print(f'projects created')

        todos = mixer.cycle(5).blend(ToDo)

        print(f'todos created')

        User.objects.create_superuser('django', 'django@local.gb', 'geekbrains')

        print('done')


# class Command(BaseCommand):
#     help = 'create users to test and one superuser'

#     def add_arguments(self, parser):
#         parser.add_argument('count', type=int)

#     def handle(self, *args, **options):
#         User.objects.all().delete()
#         Project.objects.all().delete()
#         ToDo.objects.all().delete()
#         count = options['count']
#         # user_idxs = [2, 3, 5, 8, 10, 12]
#         user_idxs = [randint(0, count) for _ in range(count)]
#         for i in range(count):
#             user = User.objects.create(username=f'django_username{i}',
#                                        first_name=f'first_name{i}',
#                                        last_name=f'last_name{i}',
#                                        email=f'django{i}@local{i}.gb',
#                                        password=make_password(f'geekbrains{i}')
#                                        )
#             print(f'user {user} created')
#             if i in user_idxs:
#                 project = Project.objects.create(name=f'Dev project_{i} ', repo_url='mail.ru')
#                 project.users.add(user)
#                 print(f'project {project} created')

#                 todo = ToDo.objects.create(
#                     project=project, text=f'Some text_{i}', user=user)
#                 print(f'todo created')

#         User.objects.create_superuser(
#             'django', 'django@local.gb', 'geekbrains')

#         print('done')
