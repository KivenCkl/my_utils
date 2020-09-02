import logging
from logging import Logger
from logging.handlers import TimedRotatingFileHandler


def initLogger(logger_name: str = None):
    if logger_name not in Logger.manager.loggerDict:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        # handler all
        handler = logging.StreamHandler()
        datefmt = "%Y-%m-%d %H:%M:%S"
        format_str = "[%(asctime)s]: %(filename)s[%(funcName)s:%(lineno)d] %(levelname)-8s %(message)s"
        formatter = logging.Formatter(format_str, datefmt)
        handler.setFormatter(formatter)
        handler.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        # handler info
        handler = logging.FileHandler('info.log', encoding='utf-8')
        datefmt = "%Y-%m-%d %H:%M:%S"
        format_str = "[%(asctime)s]: %(filename)s[%(funcName)s:%(lineno)d] %(levelname)-8s %(message)s"
        formatter = logging.Formatter(format_str, datefmt)
        handler.setFormatter(formatter)
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
        # handler error
        handler = TimedRotatingFileHandler(
            'error.log', backupCount=7, encoding='utf-8')
        datefmt = "%Y-%m-%d %H:%M:%S"
        format_str = "[%(asctime)s]: %(filename)s[%(funcName)s:%(lineno)d] %(levelname)-8s %(message)s"
        formatter = logging.Formatter(format_str, datefmt)
        handler.setFormatter(formatter)
        handler.setLevel(logging.ERROR)
        logger.addHandler(handler)

    logger = logging.getLogger(logger_name)
    return logger


logger = initLogger(__name__)


class LoggingContext:
    def __init__(self, logger, level=None, handler=None, close=True):
        self.logger = logger
        self.level = level
        self.handler = handler
        self.close = close

    def __enter__(self):
        if self.level is not None:
            self.old_level = self.logger.level
            self.logger.setLevel(self.level)
        if self.handler:
            self.logger.addHandler(self.handler)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.level is not None:
            self.logger.setLevel(self.old_level)
        if self.handler:
            self.logger.removeHandler(self.handler)
        if self.handler and self.close:
            self.handler.close()


if __name__ == '__main__':
    logger = initLogger(__name__)
    logger.error("test-error")
    logger.info("test-info")
    logger.warning("test-warn")

    import sys
    logger = logging.getLogger('foo')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.INFO)
    logger.info('1. This should appear just once on stderr.')
    logger.debug('2. This should not appear')
    with LoggingContext(logger, level=logging.DEBUG):
        logger.debug('3. This should appear once on stderr.')
    logger.debug('4. This should not appear')
    h = logging.StreamHandler(sys.stdout)
    with LoggingContext(logger, level=logging.DEBUG, handler=h, close=True):
        logger.debug(
            '5. This should appear twice - once on stderr and onceon stdout.')
    logger.info('6. This should appear just once on stderr.')
    logger.debug('7. This should not appear.')
