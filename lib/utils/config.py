import os
import sys
import configparser

from utils.log import Log
from utils.exceptions import ConfigSectionFoundError


class Config:
    """
    Configuration settings
    """

    def __init__(self, file=None):
        if not file:
            file = os.path.abspath(os.curdir) + "/config.ini"

        self.log = Log().handle(__name__)
        self.log.info(f"Config file: {file}")

        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config.read(file)

    def settings(self, section, field=None):
        settings = self.config.items(section)

        try:
            settings = self.config.items(section)
        except Exception as e:
            self.log.error(f"Script exited with error: [{e}]")
            sys.exit(1)

        if field:
            try:
                section_settings = dict(settings)[field.lower()]
            except Exception as e:
                self.log.error(f"Script exited with error: [{e}]")
                sys.exit(1)

        self.log.debug(f"Config settings for {section}:{field} is {section_settings}")

        return section_settings
