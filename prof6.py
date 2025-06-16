import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        profession = request.form.get("profession")
        message = f"Votre profession est : {profession}"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render attribue automatiquement un port
    app.run(host="0.0.0.0", port=port)