from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from to_do_app.models import Task, User

class TaskViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        Task.objects.create(title='Task 1', status='New', user_id=self.user)
        Task.objects.create(title='Task 2', status='Completed', user_id=self.user)

    def test_task_list(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_task_filter_status(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('task-list') + '?status=New'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['status'], 'New')

    def test_mark_completed(self):
        self.client.force_authenticate(user=self.user)
        task = Task.objects.first()
        url = reverse('task-mark-completed', args=[task.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.status, 'Completed')
