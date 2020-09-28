from django.http import HttpRequest
from django.test import TestCase
from django.urls.resolvers import get_resolver

from lists.views import home_page


class SmokeTest(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_root_url_resolves_to_home_page_view(self) -> None:
        found = get_resolver().resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self) -> None:
        request = HttpRequest()
        response = home_page(request)

        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

