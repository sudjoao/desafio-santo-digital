from flask import Flask, jsonify, request
from project.controllers.invoice import InvoiceController
app = Flask(__name__)

invoice_controller = InvoiceController()
@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World"}), 200

@app.route('/invoice', methods=['POST'])
def post_invoice():
    body = request.get_json()
    items = body["fullTextAnnotation"]["text"].split('\n')
    return jsonify(
            invoice_controller.get_invoice_data(items)
        ), 200