from modules.file_writers import *

from utils.log import Log
from utils.exceptions import FileTypeWriterkNotFoundError


class FileWritersFactory:
    """
    Returns file writer object
    """

    def __init__(self):
        self.log = Log().handle(__name__)

    def get_file_writer(self, file_type):
        self.log.debug(f"Returning [{file_type}] writer object")
        return eval(f"{file_type.title()}FileWriter")()
