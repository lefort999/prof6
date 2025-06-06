from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recherche", methods=["POST"])
def recherche():
    profession = request.form.get("profession")
    date = request.form.get("date")
    
    if not profession or not date:
        return jsonify({"error": "Veuillez fournir une profession et une date."}), 400
    
    return jsonify({"message": "Résultat basé sur profession et date."})

if __name__ == "__main__":
    app.run(debug=True)