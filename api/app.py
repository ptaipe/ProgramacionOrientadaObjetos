from flask import Flask # pip install flask
from controllers.cliente_controller import cliente_api

app = Flask(__name__)

app.register_blueprint(cliente_api)

@app.get("/")
def home():
    return {"Api":" API POO Funcionando. Ok"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)