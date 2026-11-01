
import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchByCategory(unittest.TestCase):

    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Aladdin", "Animation"),
            DigitalVideoDisc("Star Wars", "Sci-Fi")
        ]

    def test_search_by_category(self):
        result = search_by_category(self.dvds, "Animation")
        self.assertEqual(
            [dvd.title for dvd in result],
            ["The Lion King", "Aladdin"]
        )

    def test_search_case_insensitive(self):
        result = search_by_category(self.dvds, "animation")
        self.assertEqual(len(result), 2)

    def test_search_no_results(self):
        result = search_by_category(self.dvds, "Horror")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
