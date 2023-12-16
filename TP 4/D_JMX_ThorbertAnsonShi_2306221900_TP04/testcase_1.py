import unittest
from tp04 import BarcodeGenerator
from tkinter import Tk


class CodeValidation(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Tk()
        self.barcode_generator = BarcodeGenerator(self.root)

    def test_validate_code_valid(self):
        self.barcode_generator.code = "123456789012"

        result = self.barcode_generator.validate_code()
        self.assertEqual(result, 1, "Should be 1")

    def test_validate_code_invalid_non_numeric(self):
        self.barcode_generator.code = "hellobois"

        result = self.barcode_generator.validate_code()
        self.assertEqual(result, 0, "Should be 0")

    def test_validate_code_invalid_wrong_length(self):
        self.barcode_generator.code = "123"

        result = self.barcode_generator.validate_code()
        self.assertEqual(result, 0, "Should be 0")

    def tearDown(self) -> None:
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
