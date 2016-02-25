from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from opportunities.views import home

class ViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_view(self):
        request = self.factory.get(reverse('home'))
        response = home(request)
        self.assertEqual(response.status_code, 200)
