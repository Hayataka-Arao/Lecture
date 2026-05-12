import unittest
from lecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):

    # テストケース1
    def test_read_lines(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        self.assertEqual(3, len(line))

    # テストケース2
    def test_read_columns(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()

        self.assertEqual(4, len(line[0]))

    # テストケース3
    def test_read_file(self):
        printer = CSVPrinter("dummy.csv")

        with self.assertRaises(FileNotFoundError):
            printer.read()