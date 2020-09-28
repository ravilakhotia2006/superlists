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
