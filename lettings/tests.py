from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from lettings.models import Address, Letting
from profiles.models import Profile



# Create your tests here.
""" Test Affichage:"""
class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'lettings/home.html')

""" Test logging: """
class UserCreationTest(TestCase):
    def test_user_creation(self):
        User.objects.create_user(username='testuser', password='test123')
        self.assertTrue(User.objects.filter(username='testuser').exists())

""" Test création d'une instance de l'adresse. """
class AddressModelTestCase(TestCase):
    def test_address_creation(self):
        address = Address.objects.create(number=123, street='Test Street', city='Test City', state='TS', zip_code=12345, country_iso_code='TST')
        self.assertEqual(str(address), '123 Test Street')


""" Test création d'une instance de Letting. """
class LettingModelTestCase(TestCase):
    def test_letting_creation(self):
        address = Address.objects.create(number=123, street='Test Street', city='Test City', state='TS', zip_code=12345, country_iso_code='TST')
        letting = Letting.objects.create(title='Test Letting', address=address)
        self.assertEqual(str(letting), 'Test Letting')


