# How to use

## How to Use LoggingHelper Class

### 1. Import the LoggingHelper class

First, you need to import the `LoggingHelper` class into your Python script or module.

```python
from logging_helper import LoggingHelper
```

### 2. Configure Logging

Next, you can use the `get_logger` method of the `LoggingHelper` class to configure logging in your project. This method returns a logger object that you can use to log messages.

```python
logger = LoggingHelper.get_logger(logger_name='my_logger', logging_file=True, logging_file_name='my_logs')
```

- `logger_name`: Specify a name for your logger.
- `logging_file`: Set to `True` if you want to save logs to a file, `False` otherwise.
- `logging_file_name`: (Optional) Specify a custom name for the log file. By default, it uses the project folder name.
- `mode`: (Optional) Set the mode for opening the log file (`'w'` for write mode by default).

### 3. Log Messages

Once you have configured the logger, you can use it to log messages at different log levels.

```python
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

### 4. Customize Logging Format (Optional)
If you want to customize the logging format, you can modify the `__get_formats` method in the `LoggingHelper` class according to your preferences.

### 5. Review Logs
If you have enabled logging to a file, you can review the logs in the specified log file (default name is `<project_folder_name>.log`).

### Example

```python
from logging_helper import LoggingHelper

# Configure logger
logger = LoggingHelper.get_logger(logger_name='my_logger', logging_file=True, logging_file_name='my_logs')

# Log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

```

This is a basic guide on how to use the `LoggingHelper` class in your Python projects. Make sure to customize the configuration according to your specific requirements and review the documentation for advanced usage options.
