import json

def load_db():

    with open("products.json", "r") as file:
        products = json.load(file)
        return products