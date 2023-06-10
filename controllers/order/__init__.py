from flask import Blueprint

# Tạo một thể hiện của lớp Blueprint
bp = Blueprint('order', __name__)

# Import các route từ tệp routes.py
from controllers.order import routes
