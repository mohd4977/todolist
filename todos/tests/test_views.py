from django.test import TestCase, RequestFactory
from django.urls import reverse
from todos.views import TaskList, TaskDetail
from todos.models import Task
from django.contrib.auth.models import AnonymousUser, User
from django.test import Client

class TestTaskListViews(TestCase):
        
    def setUp(self):
        self.request = RequestFactory().get(reverse('tasks'))
        self.view = TaskList()
        self.view.setup(self.request)
    
    def test_view_guest(self):
        self.request.user = AnonymousUser()
        self.view.setup(self.request)
        response = TaskList.as_view()(self.request)
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.headers.get('Location'))
    
    def test_view_authenticated(self):
        self.request.user = User.objects.create(username='test', is_active=True, email='a@b.com')
        self.view.setup(self.request)
        response = TaskList.as_view()(self.request)
        self.assertEqual(response.status_code, 200)
    
    def test_view_contains_data(self):
        self.request.user = User.objects.create(username='test', is_active=True, email='a@b.com')
        self.view.setup(self.request)

        Task.objects.create(name='Test', description='It is a long established \
                            fact that a reader will be distracted by the readable \
                            content of a page when looking at its layout. The pointm \
                             of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, \
                            as opposed to using', status="NA", user=self.request.user)

        response = TaskList.as_view()(self.request)
        task = Task.objects.get(id=1)
        self.assertContains(response, task.name)

class TestTaskDetailViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test1', email='test1@test.com', is_active=True, password='Test12345678')

    def test_view_contains_data(self):
        self.client.login(username="test1", password="Test12345678")
        Task.objects.create(name='Test', description='It is a long established \
                            fact that a reader will be distracted by the readable \
                            content of a page when looking at its layout. The pointm \
                             of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, \
                            as opposed to using', status="NA", user=self.user)
        response = self.client.get(reverse("task", args=(1,)))
        task = Task.objects.get(id=1)
        self.assertContains(response, task.name)
        self.assertEqual(response.status_code, 200)

class TestTaskCreateViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test1', email='test1@test.com', is_active=True, password='Test12345678')

    def test_view_contains_data(self):
        self.client.login(username="test1", password="Test12345678")
        response = self.client.post('/task/create/', {'name':'Test', 'description': 'Test', 'status': 'NA'})
        task = Task.objects.get(id=1)
        self.assertEqual(response.status_code, 302)

class TestTaskUpdateViews(TestCase):
    def test_update(self):
        task = Task.objects.create(name='Test', description='Test', status='NA')

        response = self.client.post(
            reverse('task_update', kwargs={'pk': task.id}), 
            {'name': 'Test2', 'description': 'Test', 'status': 'NA'})

        self.assertEqual(response.status_code, 302)

class TestTaskDeleteViews(TestCase):
    def test_delete(self):
        task = Task.objects.create(name='Test', description='Test', status='NA')

        response = self.client.post(
            reverse('task_delete', kwargs={'pk': task.id}))

        self.assertEqual(response.status_code, 302)