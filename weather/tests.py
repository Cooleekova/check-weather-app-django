from django.test import TestCase
from django.urls import reverse, resolve
from views import index

# Create your tests here.


class TestUrls(TestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(url, '/')
        self.assertEquals(resolve(url).func, index)
        
