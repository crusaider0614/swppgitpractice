from django.forms.models import model_to_dict
from django.test import TestCase, Client
from .models import Hero
import json


class HeroTestCase(TestCase):
	def setUp(self):
		Hero.objects.create(name='Superman')
		Hero.objects.create(name='Batman')
		Hero.objects.create(name='Joker')
		self.client = Client()
		
	def test_hero_str(self):
		batman = Hero.objects.get(name='Batman')
		self.assertEqual(str(batman), 'Batman')
	
	def test_hero_detail_get(self):
		response = self.client.get('/api/hero/1')
		print(response.content)
		data = json.loads(response.content.decode())
		self.assertEqual(data['name'], 'Superman')
		self.assertEqual(response.status_code, 200)

	def test_hero_detail_get_fail(self):
		response = self.client.get('/api/hero/4')
		print(response.content)
		self.assertEqual(response.status_code, 404)

	def test_hero_detail_put(self):
		response = self.client.put('/api/hero/1', json.dumps({'name': 'Spiderman'}), content_type='applications/json')
		print(response.content)
		data = json.loads(response.content.decode())
		self.assertEqual(response.status_code, 204)

