import unittest
from currency_converter import CurrencyConverter  # Ensure correct import based on the actual module

class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        self.converter = CurrencyConverter()  # Initialize the CurrencyConverter object
    
    # Test USD to EUR conversion
    def test_usd_to_eur(self):
        self.assertAlmostEqual(self.converter.convert(100, 'USD', 'EUR'), 85.0, places=2)

    # Test EUR to USD conversion
    def test_eur_to_usd(self):
        self.assertAlmostEqual(self.converter.convert(100, 'EUR', 'USD'), 118.0, places=2)

    # Test GBP to NPR conversion
    def test_gbp_to_npr(self):
        self.assertAlmostEqual(self.converter.convert(100, 'GBP', 'NPR'), 9840.0, places=2)

    # Test NPR to USD conversion
    def test_npr_to_usd(self):
        self.assertAlmostEqual(self.converter.convert(1000, 'NPR', 'USD'), 14.0, places=2)

    # Test same currency conversion (should return the same amount)
    def test_same_currency(self):
        self.assertEqual(self.converter.convert(100, 'USD', 'USD'), 100)

    # Test invalid currency input (should raise an appropriate error or handle gracefully)
    def test_invalid_currency(self):
        with self.assertRaises(ValueError):  # Adjust if the method raises a different type of exception
            self.converter.convert(100, 'USD', 'ABC')

if __name__ == '__main__':
    unittest.main()
