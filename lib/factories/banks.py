from modules.banks import *

from utils.log import Log
from utils.exceptions import BankNotFoundError


class BanksFactory:
    """
    Returns bank object
    """

    def __init__(self):
        self.log = Log().handle(__name__)

    def get_bank(self, bank):
        self.log.debug(f"Returning bank [{bank}] object")
        return eval(bank)()
