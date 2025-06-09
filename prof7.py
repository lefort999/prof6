import tkinter as tk

# Fonction de vérification
def check_data():
    messages = []

    # Vérification profession et date
    if profession_entry.get().strip().lower() == "douanier" and date_entry.get().strip() == "1805":
        messages.append("Pour cette date, on trouvera aux archives nationales le dossier professionnel complet des douaniers.")

    # Vérification lieu et date uniquement si une date est entrée
    date_text = date_entry.get().strip()
    if date_text:
        try:
            date_value = int(date_text)
            if lieu_entry.get().strip().lower() == "strasbourg" and 1870 <= date_value < 1918:
                messages.append("Pour cette période et l'Alsace, les règles administratives sont différentes.")
        except ValueError:
            messages.append("La date doit être un nombre valide.")

    # Vérification acte d'état civil
    acte_reponse = acte_entry.get().strip().lower()
    if acte_reponse == "oui":
        messages.append("Si un acte de mariage est entre vos mains, empressez-vous d'exploiter les données qui s'y trouvent comme contrat de mariage, divorce, professions.")
    elif acte_reponse == "non":
        messages.append("Empressez-vous de l'acquérir auprès des mairies ou des archives départementales pour un document plus ancien.")

    # Vérification archives judiciaires
    archives_reponse = archives_entry.get().strip().lower()
    if archives_reponse == "oui":
        messages.append("""Les archives judiciaires peuvent contenir des documents précieux, comme les jugements, les dossiers criminels ou civils.
Un de vos ancêtres a pu être en rapport avec la justice :
- Soit à travers sa profession : Notaire, avocat, huissier, avoué, commissaire-priseur, juge...
- Soit dans le cadre de procès comme partie prenante (ex : divorce, successions litigieuses).""")

    if messages:
        result_label.config(text=messages.pop(0))
        check_button.config(command=lambda: display_next_message(messages))
    else:
        result_label.config(text="Pas de réponse")

# Fonction pour afficher le prochain message
def display_next_message(messages):
    if messages:
        result_label.config(text=messages.pop(0))
        check_button.config(command=lambda: display_next_message(messages))
    else:
        check_button.config(command=check_data)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Vérification des données et lexique")
root.geometry("900x700")  # Agrandit la fenêtre

# Création des widgets de saisie
profession_label = tk.Label(root, text="Profession :", fg="white", bg="blue")
profession_label.grid(row=0, column=0)
profession_entry = tk.Entry(root, width=50)
profession_entry.grid(row=0, column=1)

date_label = tk.Label(root, text="Date :", fg="white", bg="blue")
date_label.grid(row=1, column=0)
date_entry = tk.Entry(root, width=50)
date_entry.grid(row=1, column=1)

lieu_label = tk.Label(root, text="Lieu :", fg="white", bg="blue")
lieu_label.grid(row=2, column=0)
lieu_entry = tk.Entry(root, width=50)
lieu_entry.grid(row=2, column=1)

acte_label = tk.Label(root, text="Acte d'état civil (Oui/Non) :", fg="white", bg="blue")
acte_label.grid(row=3, column=0)
acte_entry = tk.Entry(root, width=50)
acte_entry.grid(row=3, column=1)

archives_label = tk.Label(root, text="Archives judiciaires ? (Oui/Non) :", fg="white", bg="blue")
archives_label.grid(row=4, column=0)
archives_entry = tk.Entry(root, width=50)
archives_entry.grid(row=4, column=1)

# Ajout de la Listbox pour les mots-clés, placée à droite des champs de saisie
listbox_label = tk.Label(root, text="Lexique généalogique :", fg="white", bg="green")
listbox_label.grid(row=0, column=2, rowspan=2)

listbox = tk.Listbox(root, height=10, width=30)
listbox.grid(row=2, column=2, rowspan=3)  # Placée sur plusieurs lignes

# Dictionnaire des mots-clés et leurs explications
explanations = {
    "Terrier": "Ancien registre foncier qui recense les propriétés et leurs propriétaires.",
    "Censier": "Document décrivant les obligations d’un paysan envers un seigneur.",
    "Tabellion": "Notaire médiéval chargé de la rédaction des actes.",
    "Testament": "Document qui précise la transmission des biens après décès.",
    "Curé": "Responsable paroissial ayant souvent tenu des registres d’état civil."
}

for word in explanations.keys():
    listbox.insert(tk.END, word)

# Fonction pour afficher l'explication d'un mot-clé
def show_explanation(event):
    selection = listbox.curselection()
    if selection:
        selected_word = listbox.get(selection[0])
        explanation_label.config(text=explanations.get(selected_word, "Explication non disponible"))

listbox.bind("<<ListboxSelect>>", show_explanation)

# Label pour afficher les explications des mots-clés
explanation_label = tk.Label(root, text="Sélectionnez un mot pour voir son explication.", fg="black", wraplength=300)
explanation_label.grid(row=5, column=2)

check_button = tk.Button(root, text="Vérifier", command=check_data)
check_button.grid(row=5, column=0, columnspan=2)

result_label = tk.Label(root, text="", fg="black", wraplength=700)
result_label.grid(row=6, column=0, columnspan=3)

# Lancer la boucle principale
root.mainloop()