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

if __name__ == '__main__':
    app.run(debug = True)