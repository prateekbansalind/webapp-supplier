from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_supplier.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/announcements')
def announcements():
    return render_template('announcements.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
