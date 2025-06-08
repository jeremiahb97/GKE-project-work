from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "I love you, mami"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080)) # ✅ Cloud Run provides this
    app.run(host="0.0.0.0", port=port)         # ✅ Must bind to 0.0.0.0
