from flask import render_template
from controllers.order import bp

# Định nghĩa route '/' cho blueprint 'index'
@bp.route('/order_manager', methods=["GET", "POST"])
def order_manager_index():
    data = []
    return render_template('views/order_manager_screen/index.html', data=data)
