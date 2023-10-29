from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_item_model(self):
        item = Item.objects.create(name='Test Item', amount=10, description='Test Description')
        retrieved_item = Item.objects.get(pk=item.pk)
        self.assertEqual(item, retrieved_item)