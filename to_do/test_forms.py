from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())

    def test_done_not_required(self):
        form = ItemForm({'name': 'test todo'})
        self.assertTrue(form.is_valid())

    def test_fields_set_in_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
