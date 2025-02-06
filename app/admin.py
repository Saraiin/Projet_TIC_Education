import sqlite3


def ajouter_question():
    conn = sqlite3.connect("database/quiz.db")
    cursor = conn.cursor()

    question = input("Entrez la question : ")
    option1 = input("Option 1 : ")
    option2 = input("Option 2 : ")
    option3 = input("Option 3 : ")
    correct_option = input("Réponse correcte (1, 2 ou 3) : ")

    cursor.execute("INSERT INTO questions (question, option1, option2, option3, correct_option) VALUES (?, ?, ?, ?, ?)",
                   (question, option1, option2, option3, correct_option))

    conn.commit()
    conn.close()
    print("Question ajoutée avec succès !")


def afficher_resultats():
    conn = sqlite3.connect("database/quiz.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resultats ORDER BY score DESC")
    resultats = cursor.fetchall()
    conn.close()

    print("\n📊 Classement des élèves 📊\n")
    for r in resultats:
        print(f"{r[1]} - {r[2]} : {r[3]} points (le {r[4]})")


# Ajouter une question ou afficher les résultats
choix = input("1. Ajouter une question\n2. Voir le classement\nChoisissez : ")
if choix == "1":
    ajouter_question()
elif choix == "2":
    afficher_resultats()
