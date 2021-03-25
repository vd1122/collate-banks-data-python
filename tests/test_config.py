import os, sys
import unittest

os.environ["DISABLE-LOGGING"] = "Y"

sys.path.append(f"../lib/")
from utils.config import Config


class TestConig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.config = Config("../config.ini")

    def tearDown(self):
        pass

    def test_banks_list(self):
        self.assertEqual(
            self.config.settings("ACCOUNTING", "BANKS-LIST"), "Bank1,Bank2,Bank3"
        )

    @unittest.skip("TODO")
    def test_input_file_dir_exists(self):
        """
        Steps:
        Get dir path from config settings
        Check if dir exists
        Check if dir readable
        """
        pass

    @unittest.skip("TODO")
    def test_output_file_dir_exists(self):
        """
        Steps:
        Get dir path from config settings
        Check if dir exists
        Check if dir writable
        """
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
