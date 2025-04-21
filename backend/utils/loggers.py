import logging
import sys

def setup_logger(name):
    """
    Sets up a logger with a specific format and handler.

    Args:
        name: The name of the logger.

    Returns:
        A logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set the lowest log level

    # Create a handler that writes to standard output
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger
