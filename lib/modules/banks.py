import abc
import datetime as dt


class Bank(metaclass=abc.ABCMeta):
    """
    Banks abstract class
    """

    @abc.abstractmethod
    def data_file_type(self):
        """
        file types could be csv, json
        """
        pass

    def name(self):
        return self.__class__.__name__

    def output_csv_line(self, row):
        self.row = row
        return [
            self.name(),
            self._timestamp,
            self._type,
            "{:.2f}".format(float(self._amount)),
            row["from"],
            row["to"],
        ]

    def __str__(self):
        return self.__class__.__name__


class Bank1(Bank):
    """
    Bank1 class
    """

    @property
    def _timestamp(self):
        return dt.datetime.strptime(self.row["timestamp"], "%b %d %Y").strftime(
            "%d %b %Y"
        )

    @property
    def _type(self):
        return self.row["type"]

    @property
    def _amount(self):
        return self.row["amount"]

    def data_file_type(self):
        return "csv"


class Bank2(Bank):
    """
    Bank2 class
    """

    @property
    def _timestamp(self):
        return dt.datetime.strptime(self.row["date"], "%d-%m-%Y").strftime("%d %b %Y")

    @property
    def _type(self):
        return self.row["transaction"]

    @property
    def _amount(self):
        return self.row["amounts"]

    def data_file_type(self):
        return "csv"


class Bank3(Bank):
    """
    Bank3 class
    """

    @property
    def _timestamp(self):
        return dt.datetime.strptime(self.row["date_readable"], "%d %b %Y").strftime(
            "%d %b %Y"
        )

        return self.row["date_readable"]

    @property
    def _type(self):
        return self.row["type"]

    @property
    def _amount(self):
        return f'{self.row["euro"]}.{self.row["cents"]}'

    def data_file_type(self):
        return "csv"
