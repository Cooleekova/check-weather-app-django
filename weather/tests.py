from django.test import TestCase, Client
from django.urls import reverse, resolve
from weather.views import index

# Create your tests here.


class TestUrls(TestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(url, '/')
        self.assertEquals(resolve(url).func, index)
        

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_GET(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('weather/weather.html')

    def test_index_POST(self):
        response = self.client.post(reverse('index'), {'city': "New York"})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['weather_data'][0]['city'], "New York")
        self.assertTemplateUsed('weather/weather.html')
        
