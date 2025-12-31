from Promo import calculate_discount
from unittest import TestCase


class TestClass(TestCase):
    def test_promos_not_equal(self):
        price_after_discount = calculate_discount("Mentos", 200.00, "HALFOFF")

      
        self.assertNotEqual(price_after_discount, 400)

    def test_promos_equal(self):
        price_after_discount = calculate_discount("Mentos", 200.00, "HALFOFF")
        self.assertEqual(price_after_discount, 100.00)

