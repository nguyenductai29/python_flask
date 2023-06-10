from flask import render_template
from controllers.order import bp

# Định nghĩa route '/' cho blueprint 'index'
@bp.route('/')
def index():
    data = []
    return render_template('order_screen/index.html', data=data)
