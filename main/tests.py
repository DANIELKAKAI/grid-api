from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Grid


class GridAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_calculate_closest_points(self):
        url = reverse('calculate_closest_points')
        data = {'points': '2,2;-1,30;20,11;4,5'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('closest_points', response.data)

        closest_points = response.data['closest_points']
        self.assertEqual(closest_points, '2,2;4,5')

        grid = Grid.objects.first()
        self.assertEqual(grid.points, '2,2;-1,30;20,11;4,5')
        self.assertEqual(grid.closest_points, '2,2;4,5')

