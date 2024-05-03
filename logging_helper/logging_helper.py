#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module provides a class to assist in logging configuration.
"""

__author__ = 'David Quintanar Pérez'
__authors__ = ['David Quintanar Pérez']
__contact__ = 'davidquintanarperez@gmail.com'
__copyright__ = 'Copyright 2024, David Quintanar Pérez'
__credits__ = ['David Quintanar Pérez']
__date__ = '2024/05/02'
__deprecated__ = False
__email__ = 'davidquintanarperez@gmail.com'
__license__ = 'MIT'
__maintainer__ = 'David Quintanar Pérez'
__status__ = 'Production'
__version__ = '0.1.0'

import os
import logging


class LoggingHelper(logging.Formatter):
    """
    Class to help configure logging.
    """

    @classmethod
    def __get_formats(cls) -> dict:
        """
        Gets the log formats.

        :return: Logging formats
        :rtype: dict
        """
        white: str = '\x1b[38;5;7m'
        green = '\x1B[32m'
        yellow = '\x1B[33m'
        red = '\x1B[31m'
        bold_red = '\x1B[31;1m'
        logging_format = '[{asctime}] [{name}] [{filename}:{lineno}] [{levelname}]: {message}'

        formats = {
            logging.DEBUG: green + logging_format,
            logging.INFO: white + logging_format,
            logging.WARNING: yellow + logging_format,
            logging.ERROR: red + logging_format,
            logging.CRITICAL: bold_red + logging_format
        }

        return formats

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the registry.

        :param record: Record.
        :return: str
        """
        formats: dict = LoggingHelper.__get_formats()
        log_fmt = formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt, style='{')

        return formatter.format(record)

    @classmethod
    def __get_logging_file_path(cls, logging_file_name: str) -> str:
        """
        Gets the path of the log file.

        :param logging_file_name: Logging file name. Project folder name as default value.
        :type logging_file_name: str
        :return: Logging file path.
        :rtype: str
        """
        current_directory = os.path.dirname(os.path.realpath(__file__))
        project_name = os.path.basename(os.path.normpath(current_directory))
        project_path: str = os.path.dirname(os.path.dirname(__file__)).split(f'/{project_name}/')[0]
        logging_file_name = logging_file_name if logging_file_name else project_name
        logging_file_path: str = f'{project_path}/{logging_file_name}.log'

        return logging_file_path

    @classmethod
    def __create_logger(cls, logger_name: str, logging_file: bool, logging_file_name: str, mode: str
                        ) -> logging.getLogger():
        """
        Create the logger object.

        :param logger_name: Logger name.
        :type logger_name: str
        :param logging_file: Logging file. True if you want to save the logging, False otherwise.
        :type logging_file: bool
        :param logging_file_name: Logging file name. Project folder name as default value.
        :type logging_file_name: str
        :param mode: Logging file mode.
        :type mode: str
        :return: Logger.
        :rtype: logging.getLogger()
        """
        project_logger = logging.getLogger(logger_name)
        project_logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        ch.setFormatter(LoggingHelper())

        project_logger.addHandler(ch)

        if logging_file:
            logging_file_path: str = LoggingHelper.__get_logging_file_path(logging_file_name=logging_file_name)
            fh = logging.FileHandler(filename=logging_file_path, mode=mode)

            fh.setLevel(logging.DEBUG)
            fh.setFormatter(LoggingHelper())
            project_logger.addHandler(fh)

        return project_logger

    @staticmethod
    def get_logger(logger_name: str, logging_file: bool = True, logging_file_name: str = '', mode='w'
                   ) -> logging.getLogger():
        """
        Gets the logger object.

        :param logger_name: Logger name.
        :type logger_name: str
        :param logging_file: Logging file. True if you want to save the logging, False otherwise .
        :type logging_file: bool
        :param logging_file_name: Logging file name. Project folder name as default value.
        :type logging_file_name: str
        :param mode: Logging file mode.
        :type mode: str
        :return: Logger.
        :rtype: logging.getLogger()
        """
        if logger_name in logging.Logger.manager.loggerDict.keys():
            project_logger = logging.getLogger(logger_name)
        else:
            project_logger = LoggingHelper.__create_logger(
                logger_name=logger_name, logging_file=logging_file, logging_file_name=logging_file_name, mode=mode
            )

        return project_logger
