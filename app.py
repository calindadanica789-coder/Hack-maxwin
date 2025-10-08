from flask import Flask, request, redirect, render_template
from datetime import datetime
import json
import os

app = Flask(__name__)

# ganti target ini kalau mau arahkan ke link lain
TARGET_URL = "https://jali.me/hackmaxwin"
LOG_FILE = "clicks.log"

@app.route("/", methods=["GET"])
def home():
    # kirim TARGET_URL ke template supaya link langsung bisa menggunakan variable ini
    return render_template("page.html", TARGET_URL=TARGET_URL)

@app.route("/activate", methods=["POST"])
def activate():
    # baca pilihan (single-select radios)
    option = request.form.get("option")        # "freespin" atau "maxwin"
    provider = request.form.get("provider")    # nama provider yg dipilih (atau None)

    data = {
        "time": datetime.now().isoformat(),
        "ip": request.remote_addr,
        "user_agent": request.headers.get("User-Agent"),
        "referrer": request.referrer,
        "option": option,
        "provider": provider
    }

    # append ke file log (newline-delimited JSON)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")

    # redirect ke target (seperti sebelumnya)
    return redirect(TARGET_URL)

@app.route("/health", methods=["GET"])
def health():
    return "ok", 200

if __name__ == "__main__":
    # Jalankan lokal: python app.py
    app.run(debug=True, host="0.0.0.0", port=5000)
