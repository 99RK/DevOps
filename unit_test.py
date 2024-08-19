import unittest
from currency_converter import currency_converter

class TestCurrencyConverter(unittest.TestCase):

    # Test USD to EUR conversion
    def test_usd_to_eur(self):
        self.assertAlmostEqual(currency_converter(100, 'USD', 'EUR'), 85.0)

    # Test EUR to USD conversion
    def test_eur_to_usd(self):
        self.assertAlmostEqual(currency_converter(100, 'EUR', 'USD'), 118.0)

    # Test GBP to NPR conversion
    def test_gbp_to_npr(self):
        self.assertAlmostEqual(currency_converter(100, 'GBP', 'NPR'), 9840.0)

    # Test NPR to USD conversion
    def test_npr_to_usd(self):
        self.assertAlmostEqual(currency_converter(1000, 'NPR', 'USD'), 14.0)

    # Test same currency conversion (should return the same amount)
    def test_same_currency(self):
        self.assertEqual(currency_converter(100, 'USD', 'USD'), 100)

    # Test invalid currency input (should return None or raise an appropriate error)
    def test_invalid_currency(self):
        self.assertIsNone(currency_converter(100, 'USD', 'ABC'))

if _name_ == '_main_':
    unittest.main()
