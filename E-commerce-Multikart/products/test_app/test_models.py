from products.models import Category
from django.test import TestCase


class CategoryModelTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data = {
            'title' : 'dress',
        }
        cls.category = Category.objects.create(**cls.data)

    def test_create_model(self):
        category = Category.objects.first()
        self.assertEqual(self.category, category)
    
    @classmethod
    def tearDownClass(cls) -> None:
        pass

