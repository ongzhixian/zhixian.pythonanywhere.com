import inspect
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

    @staticmethod
    def infox(message, **kwargs):
        """Experimental
        Adds module name and function of log function caller to give log entries like the following:
        INF|logging     |your log message | {"module_name": "forum_app.api.gn-auth", "func_name": "<module>"}
        INF|logging     |your log message | {"operation": "myfun", "status": 400, "status_text": "Bad request", "status_description": "Request is not JSON", "module_name": "forum_app.api.gn-auth", "func_name": "<module>"}
        This works; but the downside(?) is that log entries are log as 'INF|logging' (cannot filter by module)
        Looks like the better option is use a custom logger (see below)
        """
        # We could reflect using currentframe() or get the entire stack
        # stack = inspect.stack()
        # the_class = stack[1][0].f_locals["self"].__class__.__name__
        # the_method = stack[1][0].f_code.co_name
        previous_frame = inspect.currentframe().f_back
        func_name = previous_frame.f_code.co_name
        module_name = inspect.getmodule(previous_frame).__name__
        kwargs['module_name'] = module_name
        kwargs['func_name'] = func_name
        logging.info(structured_log_message(message, **kwargs))


# def custom_logger():
#     return
#     # TODO: See if we synergise with the default logging setup in __init__.py 
#     # logger = logging.getLogger(__name__)
#     # # Create handlers
#     # c_handler = logging.StreamHandler()
#     # f_handler = logging.FileHandler('file.log')
#     # c_handler.setLevel(logging.WARNING)
#     # f_handler.setLevel(logging.ERROR)
#     # # Create formatters and add it to handlers
#     # c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#     # f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     # c_handler.setFormatter(c_format)
#     # f_handler.setFormatter(f_format)
#     # return logger