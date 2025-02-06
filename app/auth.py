import sqlite3

def inscrire_utilisateur(nom, username, password, role):
    conn = sqlite3.connect("database/quiz.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (nom, username, password, role) VALUES (?, ?, ?, ?)",
                       (nom, username, password, role))
        conn.commit()
        print(f"Utilisateur {nom} ajouté avec succès !")
    except sqlite3.IntegrityError:
        print("Nom d'utilisateur déjà existant.")
    conn.close()

def connexion(username, password):
    conn = sqlite3.connect("database/quiz.db")
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user[0] if user else None
