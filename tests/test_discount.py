
import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestDiscount(unittest.TestCase):

    def test_discount_20_percent(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Test DVD", "Movie", "Director", 120, 100.0)
        cart.add_dvd(dvd)

        self.assertEqual(cart.total_cost_with_discount(20), 80.0)

    def test_invalid_discount(self):
        cart = Cart()

        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()
