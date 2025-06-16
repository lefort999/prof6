from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        profession = request.form.get("profession")
        if profession.lower() == "douanier":
            message = "Si profession = douanier, leurs archives sont aux archives nationales."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)