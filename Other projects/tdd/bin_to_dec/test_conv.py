from bin_to_dec import convert
import unittest

class TestConv(unittest.TestCase):
    def test_conv_all_numbers(self):
        self.assertEqual(convert("1101"), 13, "Should be 13")
        self.assertEqual(convert("0000"), 0, "Should be 0")

    def test_conv_errors(self):
        pass