from flask import Flask, request, jsonify
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)

@app.route("/api/gerar_qrcode", methods=["POST"])
def gerar_qrcode():
    data = request.get_json()
    valor = data.get("valor")
    identificador = data.get("identificador")

    payload = f"https://pagseguro.com.br/pagamento?valor={valor}&id={identificador}"

    qr = qrcode.make(payload)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return jsonify({"qrcode_base64": img_base64})
