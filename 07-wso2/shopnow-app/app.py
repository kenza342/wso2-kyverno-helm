from flask import Flask, jsonify, request

app = Flask(__name__)

customers = [
    {
        "id": 1,
        "firstName": "Kenza",
        "lastName": "Test",
        "email": "kenza@example.com"
    }
]


@app.route("/status/200", methods=["GET"])
def status():
    return "", 200


@app.route("/customers", methods=["GET"])
def get_customers():
    return jsonify(customers), 200


@app.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = next(
        (c for c in customers if c["id"] == customer_id),
        None
    )

    if customer is None:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify(customer), 200


@app.route("/customers", methods=["POST"])
def create_customer():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    new_id = max([c["id"] for c in customers], default=0) + 1

    customer = {
        "id": new_id,
        "firstName": data.get("firstName"),
        "lastName": data.get("lastName"),
        "email": data.get("email")
    }

    customers.append(customer)

    return jsonify(customer), 201


@app.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    customer = next(
        (c for c in customers if c["id"] == customer_id),
        None
    )

    if customer is None:
        return jsonify({"error": "Customer not found"}), 404

    data = request.get_json()

    customer["firstName"] = data.get("firstName", customer["firstName"])
    customer["lastName"] = data.get("lastName", customer["lastName"])
    customer["email"] = data.get("email", customer["email"])

    return jsonify(customer), 200


@app.route("/customers/<int:customer_id>", methods=["PATCH"])
def patch_customer(customer_id):
    customer = next(
        (c for c in customers if c["id"] == customer_id),
        None
    )

    if customer is None:
        return jsonify({"error": "Customer not found"}), 404

    data = request.get_json()

    if "firstName" in data:
        customer["firstName"] = data["firstName"]

    if "lastName" in data:
        customer["lastName"] = data["lastName"]

    if "email" in data:
        customer["email"] = data["email"]

    return jsonify(customer), 200


@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    global customers

    customer = next(
        (c for c in customers if c["id"] == customer_id),
        None
    )

    if customer is None:
        return jsonify({"error": "Customer not found"}), 404

    customers = [
        c for c in customers
        if c["id"] != customer_id
    ]

    return jsonify({
        "message": "Customer deleted",
        "id": customer_id
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
