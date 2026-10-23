from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# Homepage route that returns a welcome message
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API"}), 200

# GET /products returns all products, or filters them by ?category=
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        # Normalize case so "Books" and "books" both match
        filtered = [p for p in products if p["category"].lower() == category.lower()]
        return jsonify(filtered), 200
    return jsonify(products), 200

# GET /products/<id> returns a specific product by ID, or 404 if it doesn't exist
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = next((p for p in products if p["id"] == id), None)
    if product is None:
        return jsonify({"error": f"Product with id {id} not found"}), 404
    return jsonify(product), 200

if __name__ == "__main__":
    app.run(debug=True)
