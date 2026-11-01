
import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearchByTitle(unittest.TestCase):

    def test_search_without_vietnamese_accents(self):
        dvd = DigitalVideoDisc("\u0110i\u1ec7n tho\u1ea1i")
        result = search_by_title([dvd], "dien")

        self.assertEqual(
            [item.title for item in result],
            ["\u0110i\u1ec7n tho\u1ea1i"]
        )

    def test_search_case_insensitive(self):
        dvd = DigitalVideoDisc("The Lion King")
        result = search_by_title([dvd], "LION")

        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
