"""This is the app demonstrates logging configuration and unit testing"""

import logging
import logging.config
import os


class Config(object):
    """This provides configuration information"""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOG_DIR = os.path.join(BASE_DIR, '..\\logs')


def main():
    """This is the main function that is run"""
    print_hello_name()
    info_logger = logging.getLogger("information")

    test_array = [1, 2, 3, 4, 5, 6, 7]

    info_logger.info(test_array)
    info_logger.info("Check this message with a test")
    logging_levels_print_example()


def print_hello_name(name='world'):
    """This function prints Hello Some Name"""
    print("Hello {}".format(name))


def logging_levels_print_example():
    """This function tests logging levels"""
    logging.debug('Debug message')
    logging.info('Info message')
    logging.warning('Warning message')
    logging.error('Error message')
    logging.critical('Critcal message')


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },

    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file.handler.errors': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(Config.LOG_DIR, 'errors.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.information': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(Config.LOG_DIR, 'information.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.default_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(Config.LOG_DIR, 'root_logger_default.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default', 'file.handler.default_file'],
            'level': 'DEBUG',
            'propagate': False
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default', 'file.handler.default_file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'information': {
            'handlers': ['file.handler.information'],
            'level': 'INFO',
            'propagate': False
        },
        'errors': {  # if __name__ == '__main__'
            'handlers': ['default', 'file.handler.errors'],
            'level': 'ERROR',
            'propagate': False
        },
    }
}


def setup_logs():
    # set the name of the apps log folder to logs
    logdir = Config.LOG_DIR
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    # this loads the log configuration
    logging.config.dictConfig(LOGGING_CONFIG)


def setup():
    """This is used to run the program and setup logging to print exceptions to the logs/errors.log file"""
    setup_logs()
    try:
        main()
    except Exception as e:
        app_log = logging.getLogger("errors")
        app_log.error(e, exc_info=True)


if __name__ == '__main__':
    """This causes the setup function to be called if this is the __main__ top level of code This makes this file a 
    script that can be run from the command line"""
    setup()
