import logging as LOG
from logging.handlers import RotatingFileHandler
from flask import *
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from controllers import order, order_manager

load_dotenv()

app = Flask(__name__)
app.config.from_pyfile('settings.py')    # Tải cấu hình từ tệp settings.py

db = SQLAlchemy(app)

# Tạo FileHandler và cấu hình encoding
file_handler = RotatingFileHandler('example.log', encoding='utf-8', maxBytes=1000000, backupCount=3)
LOG.basicConfig(level=LOG.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s', handlers=[file_handler])
LOG.info('Start')

# Đăng ký blueprint của các controllers
app.register_blueprint(order.bp)
app.register_blueprint(order_manager.bp)

if __name__ == '__main__':
    app.run()
