from flask import Flask, render_template, request
from Uzivatel import Uzivatel

app = Flask(__name__, static_url_path="/static", static_folder="static", template_folder="templates")

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/registrace", methods=["GET", "POST"])
def registrace():
    if request.method == "GET":
        return render_template("registrace.html")

    if request.method == "POST":
        je_plavec = False
        if request.form["je_plavec"] == "on": je_plavec = True

        uzivatel = Uzivatel(
            nick= request.form["nick"],
            je_plavec= je_plavec,
            kamarad_do_lode= request.form["kanoe_kamarad"]
        )
        print(uzivatel.je_plavec)
        return "uzivatel byl registrovan"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000)

