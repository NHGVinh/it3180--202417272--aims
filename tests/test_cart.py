
import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        for i in range(20):
            dvd = DigitalVideoDisc(
                f"DVD {i}", "Movie", "Director", 120, 10.0
            )
            self.assertTrue(cart.add_dvd(dvd))

        extra_dvd = DigitalVideoDisc(
            "DVD 21", "Movie", "Director", 120, 10.0
        )

        self.assertFalse(cart.add_dvd(extra_dvd))
        self.assertEqual(len(cart.items), 20)


if __name__ == "__main__":
    unittest.main()
