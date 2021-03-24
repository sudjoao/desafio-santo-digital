from flask import Flask, jsonify, request
from project.controllers.invoice import InvoiceController
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World"}), 200

@app.route('/invoice', methods=['POST'])
def post_invoice():
    body = request.get_json()
    invoice_controller = InvoiceController()
    try:
        items = body["fullTextAnnotation"]["text"].split('\n')
        print(items)
        invoice_info = invoice_controller.get_invoice_data(items)
    except KeyError:
        return jsonify(
            {
                "error": "Missing parameters"
            }
        ), 400

    return jsonify(
            invoice_info
        ), 200