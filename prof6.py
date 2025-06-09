
python
Copier
Modifier
from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Conseils généalogiques</title>
</head>
<body>
    <h1>Vérification des données</h1>
    <form method="post">
        Profession: <input name="profession"><br>
        Date: <input name="date"><br>
        Lieu: <input name="lieu"><br>
        Acte d'état civil (oui/non): <input name="acte"><br>
        Archives judiciaires ? (oui/non): <input name="archives"><br>
        <input type="submit" value="Vérifier">
    </form>
    <hr>
    {% if messages %}
        <h2>Résultats</h2>
        <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    messages = []
    if request.method == "POST":
        profession = request.form.get("profession", "").strip().lower()
        date = request.form.get("date", "").strip()
        lieu = request.form.get("lieu", "").strip().lower()
        acte = request.form.get("acte", "").strip().lower()
        archives = request.form.get("archives", "").strip().lower()

        if profession == "douanier" and date == "1805":
            messages.append("Pour cette date, on trouvera aux archives nationales le dossier professionnel complet des douaniers.")

        if date:
            try:
                date_value = int(date)
                if lieu == "strasbourg" and 1870 <= date_value < 1918:
                    messages.append("Pour cette période et l'Alsace, les règles administratives sont différentes.")
            except ValueError:
                messages.append("La date doit être un nombre valide.")

        if acte == "oui":
            messages.append("Si un acte de mariage est entre vos mains, exploitez les données qu’il contient.")
        elif acte == "non":
            messages.append("Empressez-vous d'acquérir l'acte auprès des mairies ou des archives.")

        if archives == "oui":
            messages.append("Les archives judiciaires peuvent contenir des documents précieux : jugements, dossiers, etc.")

    return render_template_string(TEMPLATE, messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)