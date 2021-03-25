from modules.file_readers import *

from utils.log import Log
from utils.exceptions import FileTypeReaderkNotFoundError


class FileReadersFactory:
    """
    Returns file reader object
    """

    def __init__(self):
        self.log = Log().handle(__name__)

    def get_file_reader(self, file_type):
        self.log.debug(f"Returning [{file_type}] reader object")
        return eval(f"{file_type.title()}FileReader")()
