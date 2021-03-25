from factories.banks import BanksFactory
from factories.file_readers import FileReadersFactory
from factories.file_writers import FileWritersFactory

from utils.log import Log
from utils.config import Config


class Accounting:
    """
    Collate banks data
    """

    def __init__(self):
        self.log = Log().handle(__name__)
        self._load_config()

    def _load_config(self):
        """
        Read config
        """
        self.config = Config()
        self.input_data_dir = self.config.settings("INPUT", "DATA-DIR")
        self.output_data_file = self.config.settings("OUTPUT", "DATA-FILE")
        self.output_file_format = self.config.settings("OUTPUT", "FILE-FORMAT")
        self.banks_list = self.config.settings("ACCOUNTING", "BANKS-LIST").split(",")

    def collate_bank_data(self):
        """
        This function does following things -
        1. For each bank
        2. Get bank instance
        3. Get bank input data filename
        4. Get input data file format and based on the file format instantiate correct file reader object
        5. Read file data and generate output data
        6. Instantiate output file writer based on the required output file format in config settings
        7. Write data to the output file
        """
        output_data = []

        self.log.info("Collating bank data")

        for bank in self.banks_list:

            # Get bank instance
            bank = BanksFactory().get_bank(bank)

            # Bank input data filename
            input_filename = (
                self.input_data_dir
                + "/"
                + self.config.settings("INPUT DATA FILENAME", bank.name().title())
            )
            self.log.info(
                f"Processing [{bank.name()}] input data file [{input_filename}]"
            )

            # Get file reader object
            reader = FileReadersFactory().get_file_reader(bank.data_file_type())

            # Read data
            rows = reader.get_data(input_filename)

            # Process data line
            for row in rows:
                output_data.append(bank.output_csv_line(row))

        # Get write file object
        writer = FileWritersFactory().get_file_writer(self.output_file_format)

        # Write data to file
        writer.write_data(
            self.output_data_file,
            output_data,
            headers=["Bank", "Date", "Type", "Amount", "From", "To"],
        )

        self.log.info("Process over")
