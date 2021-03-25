import os, sys
import unittest

os.environ["DISABLE-LOGGING"] = "Y"

sys.path.append(f"../lib/")
from factories.banks import BanksFactory


class TestBanksFactory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_banks_factory(self):
        self.assertEqual(BanksFactory().get_bank("Bank1").name(), "Bank1")
        self.assertEqual(BanksFactory().get_bank("Bank2").name(), "Bank2")
        self.assertEqual(BanksFactory().get_bank("Bank3").name(), "Bank3")

    def test_banks_factory_exception(self):
        with self.assertRaises(NameError) as excp:
            BanksFactory().get_bank("Bank4")

        self.assertEqual("name 'Bank4' is not defined", str(excp.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)
