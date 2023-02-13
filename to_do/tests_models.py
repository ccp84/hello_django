from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_default_done(self):
        item = Item.objects.create(name='Test Item')
        self.assertFalse(item.done)
