import os, sys
import unittest

os.environ["DISABLE-LOGGING"] = "Y"

sys.path.append(f"../lib/")
from factories.banks import BanksFactory


class TestBankInstance(unittest.TestCase):
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

    def test_bank1_csv_output_line(self):
        data = {
            "timestamp": "Oct 1 2019",
            "type": "remove",
            "amount": 99.20,
            "from": 198,
            "to": 182,
        }

        bank = BanksFactory().get_bank("Bank1")
        actual = bank.output_csv_line(data)

        expected = ["Bank1", "01 Oct 2019", "remove", "99.20", 198, 182]
        self.assertEqual(actual, expected)

    def test_bank2_csv_output_line(self):
        data = {
            "date": "03-10-2019",
            "transaction": "remove",
            "amounts": 99.40,
            "from": 198,
            "to": 182,
        }

        expected = ["Bank2", "03 Oct 2019", "remove", "99.40", 198, 182]

        bank = BanksFactory().get_bank("Bank2")
        actual = bank.output_csv_line(data)

        self.assertEqual(actual, expected)

    def test_bank3_csv_output_line(self):
        data = {
            "date_readable": "5 Oct 2019",
            "type": "remove",
            "euro": 5,
            "cents": 7,
            "from": 198,
            "to": 182,
        }

        expected = ["Bank3", "05 Oct 2019", "remove", "5.70", 198, 182]

        bank = BanksFactory().get_bank("Bank3")
        actual = bank.output_csv_line(data)

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
