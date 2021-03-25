import abc
import csv
import sys
import json

from utils.log import Log


class FileWriter(metaclass=abc.ABCMeta):
    """
    File writers abstract class
    """

    def __init__(self):
        self.log = Log().handle(__name__)

    @abc.abstractmethod
    def write_data(self, file, data, headers):
        pass

    def output_file(self, file):
        self.output_file = file

    def name():
        return self.__class__.__name__

    def __str__(self):
        return self.__class__.__name__


class CsvFileWriter(FileWriter):
    """
    CSV file writer
    """

    def write_data(self, file, data, headers):
        self.log.info(f"Writing to CSV file: {file}")

        with open(file, "w") as fh:
            try:
                writer = csv.writer(fh)
                writer.writerow(headers)
                [writer.writerow(_) for _ in data]
            except Exception as e:
                self.log.error(
                    f"Failed to write data to the file [{file}] due to error {e}"
                )
                sys.exit(1)


class JsonFileWriter(FileWriter):
    """
    JSON file writer
    """

    def write_data(self, file, data, headers):
        self.log.info(f"Writing to JSON file: {file}")

        try:
            with open(file, "r") as fh:
                json.dump(data, fh)
        except Exception as e:
            self.log.error(
                f"Failed to write data to the file [{file}] due to error {e}"
            )
            sys.exit(1)


class XmlFileWriter(FileWriter):
    """
    XML file writer
    """

    # TODO: needs to be implemented
    def write_data(self, file, data, headers):
        self.log.info(f"Writing to XML file: {file}")
        raise "XML file writer is not yet implemented."
