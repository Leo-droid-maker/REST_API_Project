from django.core.management.base import BaseCommand
from userapp.models import User
from todoapp.models import Project, ToDo


class Command(BaseCommand):
    help = 'create users to test and one superuser'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        User.objects.all().delete()
        Project.objects.all().delete()
        ToDo.objects.all().delete()
        count = options['count']
        user_idxs = [2, 3]
        for i in range(count):
            user = User.objects.create(username=f'django_username{i}',
                                       first_name=f'first_name{i}',
                                       last_name=f'last_name{i}',
                                       email=f'django{i}@local{i}.gb')
            print(f'user {user} created')
            if i in user_idxs:
                project = Project.objects.create(
                    name=f'Dev project_{i} ', repo_url='mail.ru')
                project.users.add(user)
                print(f'project {project} created')

                todo = ToDo.objects.create(
                    project=project, text=f'Some text_{i}', user=user)
                print(f'todo {todo} created')

        User.objects.create_superuser(
            'django', 'django@local.gb', 'geekbrains')

        print('done')
