from flask import Flask, render_template
import flask.sessions
import requests
import json
import jinja2
from db import load_db

app = Flask("shop")

@app.route('/products')
def products():
    products = load_db()
    return render_template('products.html', products=products)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route("/product/<string:product_id>")
def product(product_id):

    return render_template("product.html", product_id=product_id)

@app.route("/shopping")
def shopping_chart():
#     session['products'].append(42)
    return render_template("shoppingchart.html")


app.run(debug=True)

