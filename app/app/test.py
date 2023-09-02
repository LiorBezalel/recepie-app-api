"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """" Tests the calc module"""

    def test_add_numbers(self):
        res = calc.add(8,4)
        self.assertEqual(res,12)

    def test_subtract(self):
        res = calc.sub(10,15)
        self.assertEqual(res, -5)