from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World"}), 200

@app.route('/invoice', methods=['POST'])
def post_invoice():
    body = request.get_json()
    items = body["fullTextAnnotation"]["text"].split('\n')
    invoiceNumber = None
    value = None
    verificationCode = None
    for index, item in enumerate(items):
        if invoiceNumber and verificationCode and value:
            break
        if not invoiceNumber and "N°" in item:
            invoiceNumber = item
        elif not verificationCode and "AUTORIZAÇÃO" in item:
            verificationCode = items[index+1].split(' ')[0]
        elif not value and "VALOR TOTAL DA NOTA" in item:
            value = items[index+4]
    print(invoiceNumber)
    print(verificationCode)
    print(value)
    return jsonify(
            {
                "invoiceNumber": invoiceNumber,
                "value": value,
                "verificationCode": verificationCode
            }
        ), 200