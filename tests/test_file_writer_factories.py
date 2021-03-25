import os, sys
import unittest

os.environ["DISABLE-LOGGING"] = "Y"

sys.path.append(f"../lib/")
from factories.file_writers import FileWritersFactory


class TestFileWritersFactory(unittest.TestCase):
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

    def test_file_writers_factory(self):
        self.assertEqual(
            str(FileWritersFactory().get_file_writer("csv")), "CsvFileWriter"
        )
        self.assertEqual(
            str(FileWritersFactory().get_file_writer("json")), "JsonFileWriter"
        )
        self.assertEqual(
            str(FileWritersFactory().get_file_writer("xml")), "XmlFileWriter"
        )

    def test_file_writers_factory_exception(self):
        with self.assertRaises(NameError) as excp:
            FileWritersFactory().get_file_writer("unknown")

        self.assertEqual("name 'UnknownFileWriter' is not defined", str(excp.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)
