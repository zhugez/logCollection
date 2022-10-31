from flask import *
import requests
app = Flask(__name__)
@app.route("/")
def home():
    api = "https://catfact.ninja/fact"
    res = requests.get(api).content.decode()
    return f"Server<br>{res}"
@app.route("/<path:url>")
def api(url):
    if "favicon.ico" not in url:
        data = f"{url}\n"
        with open("res.txt","a") as f:
            f.write(data)
        return "Admin"
    else:
        pass
@app.route("/api")
def run():
    with open("res.txt","r") as f:
        data = f.read()
    data = data.replace("\n","<br>")
    return f"<h1>{data}</h1>"

if __name__ == "__main__":
    app.run("0.0.0.0",80,debug=True)