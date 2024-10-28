import functools
import logging


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('api_test.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger



def log_execution(func):
    logger = setup_logger()
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    logger.info(f"Starting execution of {func.__name__}")
    return wrapper

def handle_exceptions(func):
    logger = setup_logger()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Exception occurred in {func.__name__}: {str(e)}")
            raise

    return wrapper

