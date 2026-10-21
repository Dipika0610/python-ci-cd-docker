from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Python CI/CD with Docker & GitHub Actions"

@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        message="Application is running smoothly!",
        environment="production"
    )

if __name__ == "__main__":
    # In production/Docker containers, bind to 0.0.0.0
    app.run(host="0.0.0.0", port=5000)
