import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        profession = request.form.get("profession")
        message = f"Votre profession est : {profession}"
    return f"""
    <html>
    <head><title>Recherche Profession</title></head>
    <body>
        <h1>Entrez votre profession :</h1>
        <form method="post">
            <input type="text" name="profession">
            <button type="submit">Tester</button>
        </form>
        <p>{message}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render attribue un port automatiquement
    app.run(host="0.0.0.0", port=port)