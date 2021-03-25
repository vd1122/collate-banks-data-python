import os, sys
import unittest

os.environ["DISABLE-LOGGING"] = "Y"

sys.path.append(f"../lib/")
from factories.file_readers import FileReadersFactory


class TestFileReadersFactory(unittest.TestCase):
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

    def test_file_readers_factory(self):
        self.assertEqual(
            str(FileReadersFactory().get_file_reader("Csv")), "CsvFileReader"
        )
        self.assertEqual(
            str(FileReadersFactory().get_file_reader("Json")), "JsonFileReader"
        )
        self.assertEqual(
            str(FileReadersFactory().get_file_reader("Xml")), "XmlFileReader"
        )

    def test_file_readers_factory_exception(self):
        with self.assertRaises(NameError) as excp:
            FileReadersFactory().get_file_reader("Unknown")

        self.assertEqual("name 'UnknownFileReader' is not defined", str(excp.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)
