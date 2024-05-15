from django.urls import reverse_lazy
from django.test import TestCase, Client


class ContactViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('contact')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/contact/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)


    @classmethod
    def tearDownClass(cls) -> None:
        pass


class About_pageViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('about_page')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/about_page/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)


    @classmethod
    def tearDownClass(cls) -> None:
        pass


class FaqViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('faq')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/faq/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)


    @classmethod
    def tearDownClass(cls) -> None:
        pass