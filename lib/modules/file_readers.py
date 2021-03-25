import abc
import sys
import json
from csv import DictReader

from utils.log import Log


class FileReader(metaclass=abc.ABCMeta):
    """
    File readers abstract class
    """

    def __init__(self):
        self.log = Log().handle(__name__)

    @abc.abstractmethod
    def get_data(self):
        pass

    def name():
        return self.__class__.__name__

    def __str__(self):
        return self.__class__.__name__


class CsvFileReader(FileReader):
    """
    CSV file reader
    """

    def get_data(self, file):
        self.log.info(f"Reading CSV input file: {file}")

        try:
            with open(file, "r") as fh:
                return list(DictReader(fh))
        except Exception as e:
            self.log.error(
                f"Failed to read data from the file [{file}] due to error {e}"
            )
            sys.exit(1)


class JsonFileReader(FileReader):
    """
    JSON file reader
    """

    def get_data(self, file):
        self.log.info(f"Reading JSON input file: {file}")
        try:
            with open(file, "r") as fh:
                return json.load(fh)
        except Exception as e:
            self.log.error(
                f"Failed to write data to the file [{file}] due to error {e}"
            )
            sys.exit(1)


class XmlFileReader(FileReader):
    """
    XML file reader
    """

    # TODO: needs to be implemented
    def get_data(self, file):
        self.log.info(f"Reading XML input file: {file}")
        raise "XML file reader is not yet implemented."
