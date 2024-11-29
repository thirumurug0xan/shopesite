from flask import Flask, render_template
import sqlite3

app = Flask(__name__,template_folder='./')

# Route: Homepage
@app.route('/')
def home():
    return render_template('index.html')
#test
# Route: Products Page
# @app.route('/products')
# def products():
#     # Connect to the database
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, price FROM products")
#     products = cursor.fetchall()
#     conn.close()

#     # Pass product data to the template
#     return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)

