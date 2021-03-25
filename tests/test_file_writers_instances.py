import os, sys
import unittest

os.environ["DISABLE-LOGGING"] = "Y"

sys.path.append(f"../lib/")
from modules.file_writers import *


class TestFileWriters(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        """
        Create test data
        """
        pass

    def tearDown(self):
        # Remove created for test file
        pass

    @unittest.skip("TODO")
    def test_csv_file_writer(self):
        """
        Steps:
        Define exepected data
        Write test data to output file
        Read data from file
        Match data with expected
        """
        pass

    @unittest.skip("TODO")
    def test_json_file_writer(self):
        """
        Steps:
        Define exepected data
        Write test data to output file
        Read data from file
        Match data with expected
        """
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
