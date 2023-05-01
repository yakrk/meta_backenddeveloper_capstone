from django.test import TestCase
from ...restaurant.models import MenuItem, Booking

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="salad", price=10, inventory=100)
        self.assertEqual(item, "salad:10")