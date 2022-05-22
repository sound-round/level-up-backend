from django.test import TestCase
from .models import Parameters
from django.contrib.auth.models import User

class ParametersTestCase(TestCase):
	
	def setUp(self):
		User.objects.create(username='Chip', password='12345')
		User.objects.create(username='Dale', password='12345')

	def test_parameters_model_creates(self):
		chip = User.objects.get(username="Chip")
		dale = User.objects.get(username="Dale")

		self.assertEqual(Parameters.objects.count(), 2)

		chip_parameters = chip.params
		dale_parameters = dale.params

		self.assertEqual(chip_parameters.level, 1)
		self.assertEqual(chip_parameters.class_name, "Rookie")
		self.assertEqual(dale_parameters.experience, 0)
		self.assertEqual(dale_parameters.attributes, {})
