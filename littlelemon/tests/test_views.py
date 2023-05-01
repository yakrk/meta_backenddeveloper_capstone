from django.test import TestCase
from ...restaurant.models import MenuItem, Booking
from ...restaurant.serializer import MenuItemSerializer, BookingSerializer
from rest_framework.test import APIClient
from rest_framework import status


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = MenuItem.objects.create(name='Pizza', price=10)
        self.menu2 = MenuItem.objects.create(name='Burger', price=8)

    def test_getall(self):
        response = self.client.get('/menu/')
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
