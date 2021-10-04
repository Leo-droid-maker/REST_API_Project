from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase, CoreAPIClient
import coreapi
from mixer.backend.django import mixer
from userapp.views import UserCustomViewSet
from userapp.models import User
from todoapp.models import ToDo, Project


class TestUserViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserCustomViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'username': 'Пушкин', 'email': 'local222@gmail.com'}, format='json')
        view = UserCustomViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'username': 'Пушкин', 'email': 'my1799@mail.ru'}, format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = UserCustomViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = User.objects.create(username='Пушкин', first_name='Alex', email='my1799@mail.ru')
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        user = User.objects.create(username='Пушкин', first_name='Alex', email='my1799@mail.ru')
        client = APIClient()
        response = client.put(f'/api/users/{user.id}/', {'username': 'Грин', 'email': 'local222@gmail.com'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        user = User.objects.create(username='Пушкин', email='my1799@mail.ru')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        # client.force_login(user=self.admin)
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/users/{user.id}/', {'username': 'Грин', 'email': 'local222@gmail.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(id=user.id)
        self.assertEqual(user.username, 'Грин')
        self.assertEqual(user.email, 'local222@gmail.com')
        client.logout()

    def test_get_detail_live(self):
        user = User.objects.create(username='Пушкин', first_name='Alex', email='my1799@mail.ru')
        client = CoreAPIClient()
        document = client.get('http://localhost:8000/api/users')
        print(f'THIS IS document: {document}')
        print(document['results'][0]['username'])

    def test_live_get_list(self):
        client = coreapi.Client()
        schema = client.get('http://localhost:8000/schema')
        print(schema)
        action = ['token-auth', 'create']
        params = {'username': 'django', 'password': 'geekbrains'}
        result = client.action(schema, action, params, validate=True)
        print(result)

        auth = coreapi.auth.TokenAuthentication(
            scheme='Token',
            token=result['token']
        )

        client = coreapi.Client(auth=auth)
        schema = client.get('http://localhost:8000/schema')
        action = ['projects', 'list']
        data = client.action(schema, action)
        assert (len(data) == 4)


class TestToDoViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        user = User.objects.create(username='Пушкин', first_name='Alex', email='my1799@mail.ru')
        project = Project.objects.create(name='Dev project_1 ', repo_url='mail.ru')
        project.users.add(user)
        todo = ToDo.objects.create(project=project, text='Some text_1', user=user)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/todos/{todo.id}/', {
            'text': 'Руслан и Людмила',
            'project': todo.project.id,
            'user': todo.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = ToDo.objects.get(id=todo.id)
        self.assertEqual(todo.text, 'Руслан и Людмила')

    def test_edit_mixer(self):
        todo = mixer.blend(ToDo)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username=admin.username, password='admin123456')
        response = self.client.put(f'/api/todos/{todo.id}/', {
            'text': 'Руслан и Людмила',
            'project': todo.project.id,
            'user': todo.user.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = ToDo.objects.get(id=todo.id)
        self.assertEqual(todo.text, 'Руслан и Людмила')

    def test_get_detail(self):
        todo = mixer.blend(ToDo, text='Алые паруса')
        response = self.client.get(f'/api/todos/{todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_todo = json.loads(response.content)
        self.assertEqual(response_todo['text'], 'Алые паруса')
        # print(response_todo)

    def test_get_detail_user(self):
        todo = mixer.blend(ToDo, user__user=1)
        response = self.client.get(f'/api/todos/{todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_todo = json.loads(response.content)
        self.assertEqual(response_todo['user'], 1)
        print(response_todo)
