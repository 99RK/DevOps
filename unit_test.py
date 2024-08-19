import unittest
from currency_converter import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        self.converter = CurrencyConverter()  # Initialize the CurrencyConverter object

    def test_usd_to_eur(self):
        # Update this value based on current conversion rates
        self.assertAlmostEqual(self.converter.convert(100, 'USD', 'EUR'), 91.53, places=2)

    def test_eur_to_usd(self):
        # Update this value based on current conversion rates
        self.assertAlmostEqual(self.converter.convert(100, 'EUR', 'USD'), 109.25, places=2)

    def test_gbp_to_npr(self):
        # Check if 'NPR' is supported
        if 'NPR' in self.converter.currencies:
            self.assertAlmostEqual(self.converter.convert(100, 'GBP', 'NPR'), 9840.0, places=2)
        else:
            self.skipTest("NPR is not supported by the currency converter")

    def test_npr_to_usd(self):
        # Check if 'NPR' is supported
        if 'NPR' in self.converter.currencies:
            self.assertAlmostEqual(self.converter.convert(1000, 'NPR', 'USD'), 14.0, places=2)
        else:
            self.skipTest("NPR is not supported by the currency converter")

    def test_same_currency(self):
        self.assertEqual(self.converter.convert(100, 'USD', 'USD'), 100)

    def test_invalid_currency(self):
        with self.assertRaises(ValueError):
            self.converter.convert(100, 'USD', 'ABC')

if __name__ == '__main__':
    unittest.main()
