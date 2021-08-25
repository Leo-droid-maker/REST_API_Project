from django.core.management.base import BaseCommand
from userapp.models import User


class Command(BaseCommand):
    help = 'create users to test and one superuser'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        User.objects.all().delete()
        count = options['count']
        for i in range(count):
            user = User.objects.create(username=f'django_username{i}',
                                       first_name=f'first_name{i}',
                                       last_name=f'last_name{i}',
                                       email=f'django{i}@local{i}.gb')
            print(f'user {user} created')

        User.objects.create_superuser(
            'django', 'django@local.gb', 'geekbrains')

        print('done')
