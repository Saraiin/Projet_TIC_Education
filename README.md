# Projet_TIC_Education
# (En cours de développement)

## Description
Ce projet implémente une application quiz. Il utilise une interface graphique avec Tkinter et une base de données SQLite pour stocker les questions et les options de réponses. L'application permet aux étudiants de répondre à des questions, de recevoir des résultats, et de générer un rapport PDF de leurs réponses avec leur nom, classe et note.


## Fonctionnalités
- Chargement des questions depuis une base de données SQLite.
- Interface graphique avec Tkinter pour afficher les questions et recueillir les réponses.
- Calcul automatique du score.
- Génération d'un rapport PDF avec le score final, le nom de l'élève, et la classe.

## Prérequis
Avant de commencer, assurez-vous d'avoir Python installé sur votre ordinateur ainsi que les bibliothèques suivantes :

- `sqlite3` (inclus par défaut avec Python)
- `tkinter` (inclus par défaut avec Python)
- `reportlab` (pour générer des fichiers PDF)

### Installer les dépendances
Si `reportlab` n'est pas installé, vous pouvez l'installer en exécutant la commande suivante :

```bash
pip install reportlab
