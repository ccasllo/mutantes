import logging
import logging.handlers
import os
from datetime import datetime

log_location = os.getenv('LOG_LOCATION', '/home/carlos/proyectos/mutantes/app/logs')

def set_up_logging():

    if not os.path.exists(log_location):
        os.makedirs(log_location)
    current_time = datetime.now()
    current_date = current_time.strftime("%Y-%m-%d")
    file_name = current_date + '.log'
    file_location = log_location + '/' + file_name
    with open(file_location, 'a+'):
        pass

    logger = logging.getLogger(__name__)
    format = '%(asctime)s: %(levelname)s: ' \
             '%(message)s [Path %(pathname)s ' \
             '[%(process)d]: Line %(lineno)d]'

    if os.getenv("DEBUG"):
        logging.basicConfig(format=format, level=logging.NOTSET)
    else:
        logging.basicConfig(
            format=format,
            filemode='a+',
            filename=file_location,
            level=logging.DEBUG
        )

    return logger


logger = set_up_logging()


if __name__ == '__main__':
    logger.debug('prueba')
