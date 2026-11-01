
import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestSortCart(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("Star Wars", "Sci-Fi", "Lucas", 120, 24.95))
        self.cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", "Director", 90, 18.99))
        self.cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", "Director", 90, 19.95))

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        self.assertEqual(
            [dvd.title for dvd in self.cart.items],
            ["Aladdin", "Star Wars", "The Lion King"]
        )

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()
        self.assertEqual(
            [dvd.cost for dvd in self.cart.items],
            [18.99, 19.95, 24.95]
        )


if __name__ == "__main__":
    unittest.main()
