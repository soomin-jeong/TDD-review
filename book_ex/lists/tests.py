from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import HomePageView

from django.http import HttpRequest


# Create your tests here.

class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(2**3, 8, msg='the equation fails')


class HomePageTest(TestCase):
    def test_the_root_url_finds_the_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, HomePageView, msg='Cannot find a view for homepage')

    def test_homepage_returns_correct_html(self):

        # HttpRequest object is what Django gets when a user asks for a page
        request = HttpRequest()
        response = HomePageView(request)

        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-do list</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

