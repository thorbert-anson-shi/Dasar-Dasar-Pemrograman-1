import unittest
from tkinter import Tk
from tp04 import BarcodeGenerator


class FileNameValidation(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Tk()
        self.barcode_generator = BarcodeGenerator(self.root)

    def test_file_name_valid(self):
        self.barcode_generator.file_name = "evian.eps"

        result = self.barcode_generator.validate_file()
        self.assertEqual(result, 1, "Should be 1")

    def test_file_name_invalid_wrong_extension(self):
        self.barcode_generator.file_name = "evian.lmao"

        result = self.barcode_generator.validate_file()
        self.assertEqual(result, 0, "Should be 0")

    def test_file_name_invalid_repeated_extensions(self):
        self.barcode_generator.file_name = "evian.eps.epsi"

        result = self.barcode_generator.validate_file()
        self.assertEqual(result, 0, "Should be 0")

    def test_file_name_invalid_empty_field(self):
        self.barcode_generator.file_name = ""

        result = self.barcode_generator.validate_file()
        self.assertEqual(result, 0, "Should be 0")

    def tearDown(self) -> None:
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
