from flask import Flask, render_template, request, redirect
from config.db import get_db
from models.menu import get_menu, get_specials
from models.order import save_order
import datetime

app = Flask(__name__)

@app.route('/')
def menu():
    items = get_menu()
    specials = get_specials()
    return render_template('menu.html', menu = items, specials = specials)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        data = request.form
        save_order(data)
        return redirect('/')
    return render_template('menu.html')

<<<<<<< HEAD
if __name__ == '__main__':
    app.run(debug = True)
=======

@app.route("/sale")
def view_sale():
    summary = get_summary()
    return render_template("sale.html", summary=summary)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
>>>>>>> branch1
