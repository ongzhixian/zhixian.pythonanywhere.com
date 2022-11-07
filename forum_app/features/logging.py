import json
import logging

class structured_log_message(object):
    """Structured logging message

    **Usage**

    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info(_('message 1', foo='bar', bar='baz', num=123, fnum=123.456))

    **Reference**
    
    https://docs.python.org/3/howto/logging-cookbook.html#implementing-structured-logging
    """
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        return '%s | %s' % (self.message, json.dumps(self.kwargs)) if len(self.kwargs) > 0 else '%s' % (self.message)

class log(object):
    @staticmethod
    def critical(message, **kwargs):
        logging.critical(structured_log_message(message, **kwargs))

    @staticmethod
    def error(message, **kwargs):
        logging.error(structured_log_message(message, **kwargs))

    @staticmethod
    def exception(message, **kwargs):
        logging.exception(structured_log_message(message, **kwargs))

    @staticmethod
    def warning(message, **kwargs):
        logging.warning(structured_log_message(message, **kwargs))

    @staticmethod
    def info(message, **kwargs):
        logging.info(structured_log_message(message, **kwargs))

    @staticmethod
    def debug(message, **kwargs):
        logging.debug(structured_log_message(message, **kwargs))
