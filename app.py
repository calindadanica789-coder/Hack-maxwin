from flask import Flask, request, redirect, render_template_string
from datetime import datetime
import json

app = Flask(__name__)
TARGET_URL = "https://jali.me/hackmaxwin"
LOG_FILE = "clicks.log"

HTML = """
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Aktivasi Sekarang</title></head>
<body style="font-family:sans-serif;text-align:center;margin-top:100px">
<h1>Aktivasi Sekarang</h1>
<p>Klik tombol di bawah untuk melanjutkan.</p>
<form method="POST" action="/activate">
<button type="submit" style="padding:10px 20px;font-size:18px">Aktivasi</button>
</form>
</body>
</html>
"""

@app.route("/")
def home():
    return HTML

@app.route("/activate", methods=["POST"])
def activate():
    data = {
        "time": datetime.now().isoformat(),
        "ip": request.remote_addr,
        "user_agent": request.headers.get("User-Agent"),
        "referrer": request.referrer
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")
    return redirect(TARGET_URL)

if __name__ == "__main__":
    app.run(debug=True)
