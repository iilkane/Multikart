from django.urls import reverse_lazy
from django.test import TestCase, Client


class CategoryViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('category')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/category/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)


    @classmethod
    def tearDownClass(cls) -> None:
        pass


    