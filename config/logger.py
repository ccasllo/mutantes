import logging
import logging.handlers
import config.environment as env

def set_up_logging():

    logger = logging.getLogger(__name__)
    log_format = '%(asctime)s: %(levelname)s: ' \
             '%(message)s [Path %(pathname)s ' \
             '[%(process)d]: Line %(lineno)d]'

    if env.DEBUG:
        logging.basicConfig(format=log_format, level=logging.NOTSET)
    else:
        logging.basicConfig(
            format=log_format,
            level=logging.DEBUG
        )

    return logger

logger = set_up_logging()


