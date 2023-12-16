import unittest
from tp04 import BarcodeGenerator
from tkinter import Tk


class ChecksumTest(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Tk()
        self.barcode_generator = BarcodeGenerator(self.root)

    def test_validate_checkdigit_valid(self):
        self.barcode_generator.code = "123456789012"

        self.barcode_generator.validate_code()
        result = self.barcode_generator.checkdigit
        self.assertEqual(result, 8, "Should be 8")

    def test_validate_checkdigit_invalid(self):
        self.barcode_generator.code = "hellobois"

        self.barcode_generator.validate_code()

        with self.assertRaises(AttributeError):
            result = self.barcode_generator.checkdigit

    # No need for code length check; handled in test1 already

    def tearDown(self) -> None:
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
