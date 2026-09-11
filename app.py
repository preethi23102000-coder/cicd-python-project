from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "CI/CD Pipeline Application is Running"


@app.route("/health")
def health():
    return "Application is Healthy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
