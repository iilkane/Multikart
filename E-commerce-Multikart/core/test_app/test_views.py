from django.urls import reverse_lazy
from django.test import TestCase, Client


class HomeViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('home')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/home/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)


    @classmethod
    def tearDownClass(cls) -> None:
        pass


class SearchViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('search')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/search/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)


    @classmethod
    def tearDownClass(cls) -> None:
        pass


class NotFoundViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('notFound')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/notFound/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)


    @classmethod
    def tearDownClass(cls) -> None:
        pass