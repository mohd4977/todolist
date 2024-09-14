from django.test import TestCase

from todos.models import Task

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(name='Test', description='It is a long established \
                            fact that a reader will be distracted by the readable \
                            content of a page when looking at its layout. The pointm \
                             of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, \
                            as opposed to using', status="NA")

    def test_name_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    
    def test_description_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')
    
    def test_status_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')
    
    def test_name_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_get_name(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.name, 'Test')
    
    def test_status_complete(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.get_status_display(), 'Not Active')