# Application exceptions are defined here


class ConfigSectionFoundError(Exception):
    """Exception when bank class is not defined"""

    pass


class BankNotFoundError(Exception):
    """Exception when bank class is not defined"""

    pass


class FileTypeReaderkNotFoundError(Exception):
    """Exception when file type reader is not yet implemented"""

    pass


class FileTypeWriterkNotFoundError(Exception):
    """Exception when file type writer is not yet implemented"""

    pass
