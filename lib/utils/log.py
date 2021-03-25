import os, sys
import logging


class Log:
    """
    Logs message and send it to stdout
    """

    def __init__(self):
        pass

    def handle(self, caller: str) -> object:
        """
        :param caller: name of the script which is logging message
        :return: log object
        """
        log = logging.getLogger(caller)

        if not len(log.handlers):
            log.setLevel(logging.DEBUG)
            if os.environ.get("DISABLE-LOGGING"):
                log.setLevel(logging.CRITICAL)

            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)23s - %(levelname)7s - %(message)s"
            )
            handler.setFormatter(formatter)
            log.addHandler(handler)

        return log
