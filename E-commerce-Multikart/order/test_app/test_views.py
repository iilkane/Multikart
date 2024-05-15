from django.urls import reverse_lazy
from django.test import TestCase, Client


class CartViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('cart_page')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/cart_page/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 302)


    @classmethod
    def tearDownClass(cls) -> None:
        pass



