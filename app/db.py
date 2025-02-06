import sqlite3


conn = sqlite3.connect("C:/Users/hp/PycharmProjects/Projet_TIC_Education/database/quiz.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    option1 TEXT,
    option2 TEXT,
    option3 TEXT,
    correct_option TEXT
)
""")


questions_logo = [
    ("Quel est le but de la commande `FORWARD 50` dans Logo ?",
     "Faire tourner la tortue",
     "Avancer de 50 unités",
     "Reculer de 50 unités",
     "2"),

    ("Quel est le résultat de la commande `REPEAT 4 [FORWARD 100 RIGHT 90]` ?",
     "Un carré",
     "Un triangle",
     "Un cercle",
     "1"),

    ("Comment changer la couleur de la tortue dans Logo ?",
     "SETCOLOR",
     "COLOR",
     "CHANGE_COLOR",
     "1"),

    ("Quel est l'effet de la commande `PENDOWN` ?",
     "Faire disparaître la tortue",
     "Faire apparaître la tortue",
     "Faire descendre le stylo",
     "3"),

    ("Que fait la commande `CLEARSCREEN` dans Logo ?",
     "Réinitialiser la position de la tortue",
     "Effacer l'écran",
     "Changer la couleur de l'écran",
     "2"),
]


cursor.executemany("""
INSERT INTO questions (question, option1, option2, option3, correct_option)
VALUES (?, ?, ?, ?, ?)
""", questions_logo)


conn.commit()
conn.close()

print("Base de données `quiz.db` avec les questions sur Logo a été créée avec succès !")
