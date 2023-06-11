from flask import render_template
from controllers.order import bp

# Định nghĩa route '/' cho blueprint 'index'
@bp.route('/', methods=["GET", "POST"])
def order_index():
    data = []
    return render_template('views/order_screen/index.html', data=data)
