import logging as LOG
from logging.handlers import RotatingFileHandler

def setup_logger():
    # Tạo FileHandler và cấu hình encoding
    file_handler = RotatingFileHandler('example.log', encoding='utf-8', maxBytes=1000000, backupCount=3)
    LOG.basicConfig(level=LOG.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s', handlers=[file_handler])
    # Trả về logger đã được cấu hình
    return LOG.getLogger(__name__)
