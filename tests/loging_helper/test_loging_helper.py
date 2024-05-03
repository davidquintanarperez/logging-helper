#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import unittest
from logging_helper.logging_helper import LoggingHelper


class TestLoggingHelper(unittest.TestCase):
    """
    Class to test logging_helper.py.
    """

    def test_get_logger(self) -> None:
        """
        Test creating a logger.

        This test checks whether the get_logger method can create a logger object correctly.
        :return: Nothing.
        :rtype: None
        """
        logger = LoggingHelper.get_logger(
            logger_name='test_logger', logging_file=False, logging_file_name='test_logging', mode='w'
        )

        self.assertIsInstance(logger, logging.Logger)

    def test_logging_output(self):
        """
        Test the log output.

        This test verifies if the logger created by LoggingHelper prints the logs correctly.
        """
        logger = LoggingHelper.get_logger('test_logger', logging_file=False)
        logger.setLevel(logging.DEBUG)

        with self.assertLogs(level=logging.DEBUG) as logs:
            logger.debug('Mensaje de debug')
            logger.info('Mensaje de información')
            logger.warning('Mensaje de advertencia')
            logger.error('Mensaje de error')
            logger.critical('Mensaje crítico')

        self.assertIn('Mensaje de debug', logs.output[0])
        self.assertIn('Mensaje de información', logs.output[1])
        self.assertIn('Mensaje de advertencia', logs.output[2])
        self.assertIn('Mensaje de error', logs.output[3])
        self.assertIn('Mensaje crítico', logs.output[4])


if __name__ == '__main__':
    unittest.main()
