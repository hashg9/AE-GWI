"""Storing the information about scripts with the help of the python 'logging' module"""

import logging
import os
import sys
from pathlib import Path
import platform


class LoggingUtils:
    def __init__(self, driver, shadow):
        self.driver = driver
        self.shadow = shadow

    def custom_logger(self, log_level):
        parent_folder = Path(__file__).parents[1]
        print(parent_folder, " this is the parent folder path in sanity_logs.log")

        file_path = os.path.join(parent_folder, "logs", "sanity_logs.log")
        print(file_path, " this is the file path of sanity_logs.log")

        # Create logger. Logger is used to set logging level like debug, info,..
        logger = logging.getLogger(__name__)
        logger.setLevel(log_level)

        # Create handler - File handler/Console handler
        fh = logging.FileHandler(file_path, mode="a")

        # Create formatter (how you want logs to be formatted)
        formatter_fh = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s - %(filename)s"
        )

        # Adding the formatter to console/file handler
        fh.setFormatter(formatter_fh)

        # Adding handlers to logger
        logger.addHandler(fh)

        return logger

    def take_a_screenshot(self):
        print(platform.system(), " this is the os name in take_a_screenshot method")
        parent_folder = Path(__file__).parents[1]
        print(parent_folder, " this is the parent folder path")
        screenshot_path = os.path.isdir(os.path.join(parent_folder, "screenshots"))
        print(screenshot_path, " this is the bool value of screenshot path")
        method_name = sys._getframe(1).f_code.co_name
        print(method_name, " this is the method name")
        if screenshot_path == True:
            pass
        else:
            os.makedirs(os.path.join(parent_folder, "screenshots"))
        file_name = method_name + ".png"
        print(
            os.path.join(parent_folder, "screenshots"),
            " this is the folder path from root",
        )
        self.driver.save_screenshot(
            os.path.join(parent_folder, "screenshots", file_name)
        )
        Filelists = os.listdir(os.path.join(parent_folder, "screenshots"))
        print(Filelists, " these files are present in screenshots folder")
