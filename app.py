from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from controllers import order, order_manager

app = Flask(__name__)
app.config.from_pyfile('settings.py')    # Tải cấu hình từ tệp settings.py

db = SQLAlchemy(app)

# Đăng ký blueprint của các controllers
app.register_blueprint(order.bp)
app.register_blueprint(order_manager.bp)

if __name__ == '__main__':
    app.run()
