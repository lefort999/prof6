
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Hello"
    
    
    from flask import Flask, request, render_template



@app.route("/", methods=["GET", "POST"])
def check_data():
    messages = []
    
    if request.method == "POST":
        profession = request.form.get("profession", "").strip().lower()
        date_text = request.form.get("date", "").strip()
        lieu = request.form.get("lieu", "").strip().lower()
        acte = request.form.get("acte", "").strip().lower()
        archives = request.form.get("archives", "").strip().lower()
        militaire = request.form.get("militaire", "").strip().lower()
        militairebis = request.form.get("militairebis", "").strip().lower()

        # Vérifications
        if profession == "douanier" and date_text == "1805":
            messages.append("Pour cette date, on trouvera aux archives nationales le dossier professionnel complet des douaniers.")
        
        if date_text:
            try:
                date_value = int(date_text)
                if lieu == "strasbourg" and 1870 <= date_value < 1918:
                    messages.append("Pour cette période et l'Alsace, les règles administratives sont différentes.")
            except ValueError:
                messages.append("La date doit être un nombre valide.")

        if acte == "oui":
            messages.append("Si un acte de mariage est entre vos mains, exploitez les données qui s'y trouvent.")
        elif acte == "non":
            messages.append("Acquérez-le auprès des mairies ou archives départementales.")

        if archives == "oui":
            messages.append("Les archives judiciaires peuvent contenir des documents précieux.")

        if militaire == "oui":
            messages.append("Dès 1665, on trouvera des registres par régiments avec description physique et événements comme blessures, décès, désertion.")
        elif militaire == "non":
            messages.append("Voir à d'autres dates.")

        if militairebis == "oui":
            messages.append("Avant 1665, seules des sources comme armoriaux et livres d'histoire sont disponibles.")
        elif militairebis == "non":
            messages.append("Voir à d'autres dates.")

    return render_template("index.html", messages=messages)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render impose un port
    app.run(host="0.0.0.0", port=port)
