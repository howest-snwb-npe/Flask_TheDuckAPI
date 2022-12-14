from flask import Flask, render_template, request
import requests
import base64

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/random")
def random():
    r = requests.get("https://random-d.uk/api/v2/random")
    photo_url = r.json()["url"]
    return render_template("random.html", photo_url=photo_url)

@app.route("/status-code",methods=["POST"])
def status_code():
    status_code = request.form.get("status-code")
    list_all = requests.get("https://random-d.uk/api/v2/list").json()["http"]
    if f"{status_code}.jpg" in list_all:
        photo_url = f"https://random-d.uk/api/v2/http/{status_code}"
        return render_template("status-code.html", photo_url=photo_url, found=True)
    else:
        photo_url = f"https://random-d.uk/api/v2/http/404"
        return render_template("status-code.html", photo_url=photo_url, found=False)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)