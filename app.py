from flask import *
from helpers.logger import setup_logger
from models.database import db
import secrets

from controllers import order, order_manager

# Định nghĩa logger
logger = setup_logger()

app = Flask(__name__)
app.config.from_pyfile('settings.py')    # Tải cấu hình từ tệp settings.py
app.secret_key = secrets.token_hex(16)

db.init_app(app)

logger.info('Start')

# Đăng ký blueprint của các controllers
app.register_blueprint(order.bp)
app.register_blueprint(order_manager.bp)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='8080')
