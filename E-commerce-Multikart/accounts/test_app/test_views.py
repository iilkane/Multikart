from django.urls import reverse_lazy
from django.test import TestCase, Client


class RegisterViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('register')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/register/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)


    @classmethod
    def tearDownClass(cls) -> None:
        pass


class LoginViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('login')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/login/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)


    @classmethod
    def tearDownClass(cls) -> None:
        pass


class LogoutViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('logout')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/logout/')

    # def test_response_url(self):
    #     self.assertEqual(self.response.status_code, 200)


    @classmethod
    def tearDownClass(cls) -> None:
        pass



class Vendor_profileViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('vendor_profile')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/vendor_profile/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)


    @classmethod
    def tearDownClass(cls) -> None:
        pass


class ForgetViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('forget')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/forget/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)


    @classmethod
    def tearDownClass(cls) -> None:
        pass


class WishlistViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('wishlist')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url, '/en/wishlist/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 302)


    @classmethod
    def tearDownClass(cls) -> None:
        pass