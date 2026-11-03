from flask import Flask

app = Flask(__name__)

products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Mobile", "price": 15000},
    3: {"name": "Headphones", "price": 2000}
}

@app.route('/product/<int:id>')
def product(id):
    if id in products:
        return f"Product Name: {products[id]['name']}<br>Price: ₹{products[id]['price']}"
    return "Product not found"

if __name__ == '__main__':
    app.run(debug=True)