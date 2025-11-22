# todos/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Todo
import datetime

class TodoModelTest(TestCase):

    def test_todo_creation(self):
        todo = Todo.objects.create(
            title="Buy groceries",
            description="Milk, eggs, bread",
            due_date=datetime.date.today() + datetime.timedelta(days=7),
            resolved=False
        )
        self.assertEqual(todo.title, "Buy groceries")
        self.assertEqual(todo.description, "Milk, eggs, bread")
        self.assertEqual(todo.due_date, datetime.date.today() + datetime.timedelta(days=7))
        self.assertFalse(todo.resolved)
        self.assertIsNotNone(todo.created_at)

    def test_todo_str_method(self):
        todo = Todo.objects.create(title="Walk the dog")
        self.assertEqual(str(todo), "Walk the dog")

    def test_todo_default_resolved(self):
        todo = Todo.objects.create(title="Default check")
        self.assertFalse(todo.resolved)
        

class TodoViewTest(TestCase):

    def setUp(self):
        self.todo1 = Todo.objects.create(
            title="Task 1",
            description="Description 1",
            due_date=datetime.date.today(),
            resolved=False
        )
        self.todo2 = Todo.objects.create(
            title="Task 2",
            description="Description 2",
            due_date=datetime.date.today() + datetime.timedelta(days=1),
            resolved=True
        )

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.todo1.title)
        self.assertContains(response, self.todo2.title)
        self.assertTemplateUsed(response, 'todos/todo_list.html')
        # Changed assertion to check for items in context more directly
        self.assertEqual(len(response.context['todos']), 2)
        self.assertIn(self.todo1, response.context['todos'])
        self.assertIn(self.todo2, response.context['todos'])

    def test_todo_detail_view(self):
        response = self.client.get(reverse('todo_detail', args=[self.todo1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.todo1.title)
        self.assertContains(response, self.todo1.description)
        self.assertTemplateUsed(response, 'todos/todo_detail.html')

    def test_todo_detail_view_404(self):
        response = self.client.get(reverse('todo_detail', args=[999])) # Non-existent PK
        self.assertEqual(response.status_code, 404)

    def test_todo_create_view_get(self):
        response = self.client.get(reverse('todo_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/todo_form.html')

    def test_todo_create_view_post_valid(self):
        response = self.client.post(reverse('todo_create'), {
            'title': 'New Task',
            'description': 'New Description',
            'due_date': '2025-12-31',
            'resolved': 'off' # Checkbox value for unchecked
        }, follow=True)
        self.assertEqual(response.status_code, 200) # Should redirect to list view
        self.assertContains(response, 'New Task')
        self.assertTrue(Todo.objects.filter(title='New Task').exists())

    def test_todo_create_view_post_invalid(self):
        response = self.client.post(reverse('todo_create'), {
            'description': 'Missing Title'
        })
        self.assertEqual(response.status_code, 200) # Form redisplayed with errors
        self.assertContains(response, 'This field is required.')
        self.assertFalse(Todo.objects.filter(description='Missing Title').exists())


    def test_todo_update_view_get(self):
        response = self.client.get(reverse('todo_update', args=[self.todo1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.todo1.title)
        self.assertTemplateUsed(response, 'todos/todo_form.html')

    def test_todo_update_view_post_valid(self):
        response = self.client.post(reverse('todo_update', args=[self.todo1.pk]), {
            'title': 'Updated Task 1',
            'description': 'Updated Description 1',
            'due_date': '2025-11-20',
            'resolved': 'on' # Checkbox value for checked
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Updated Task 1')
        self.todo1.refresh_from_db()
        self.assertEqual(self.todo1.title, 'Updated Task 1')
        self.assertTrue(self.todo1.resolved)

    def test_todo_delete_view_get(self):
        response = self.client.get(reverse('todo_delete', args=[self.todo1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'Are you sure you want to delete "{self.todo1.title}"?')
        self.assertTemplateUsed(response, 'todos/todo_confirm_delete.html')

    def test_todo_delete_view_post(self):
        # Delete todo1
        response = self.client.post(reverse('todo_delete', args=[self.todo1.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Todo.objects.filter(pk=self.todo1.pk).exists())
        # todo2 should still be present, so we assert its presence
        self.assertTrue(Todo.objects.filter(pk=self.todo2.pk).exists())
        self.assertContains(response, self.todo2.title) # Ensure todo2 is still displayed

    def test_todo_toggle_resolved_view(self):
        # Initial state: todo1 is not resolved
        self.assertFalse(self.todo1.resolved)

        response = self.client.post(reverse('todo_toggle_resolved', args=[self.todo1.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.todo1.refresh_from_db()
        self.assertTrue(self.todo1.resolved)

        # Toggle again: todo1 should become unresolved
        response = self.client.post(reverse('todo_toggle_resolved', args=[self.todo1.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.todo1.refresh_from_db()
        self.assertFalse(self.todo1.resolved)