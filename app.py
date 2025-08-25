from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/log", methods=["POST"])
def log():
    data = request.get_json()
    # سجل البيانات في ملف JSON (سطر لكل زيارة)
    with open("visitors_log.json", "a") as f:
        f.write(json.dumps(data) + "\n")
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
