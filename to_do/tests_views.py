from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'to_do/todo_list.html')

    def test_get_additem_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'to_do/add_item.html')

    def test_get_edititem_page(self):
        item = Item.objects.create(name='Test Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'to_do/edit_item.html')

    def test_add_item(self):
        response = self.client.post('/add', {'name': 'Test Add Item'})
        self.assertRedirects(response, '/')

    def test_toggle_item(self):
        item = Item.objects.create(name='Toggle Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_delete_item(self):
        item = Item.objects.create(name='Delete Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)
