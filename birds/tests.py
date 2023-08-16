from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import BirdModel
from .forms import BirdForm
from .services import _validate_form


class BirdFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass')
        cls.bird = BirdModel.objects.create(name='Test Bird')

    def test_validate_form_and_save_valid_form(self):
        form_data = {'name': 'New Bird', 'image': ''}
        form = BirdForm(data=form_data)
        self.assertTrue(_validate_form(form))
        self.assertEqual(BirdModel.objects.count(), 2)

    def test_validate_form_and_save_invalid_form(self):
        form_data = {'name': '', 'image': ''}
        form = BirdForm(data=form_data)
        self.assertFalse(_validate_form(form))
        self.assertEqual(BirdModel.objects.count(), 1)


class BirdsListTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass')
        cls.bird = BirdModel.objects.create(name='Test Bird')

    def test_birds_list(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('birds_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        birds = response.context['birds']
        self.assertEqual(len(birds), 1)

        bird = birds[0]
        self.assertEqual(bird, self.bird)

