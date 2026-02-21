from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt


app = QApplication([]) # Créer l'application

window = QMainWindow() # Créer la fenêtre principale de l'application


# Configuration de la fenêtre
window.setMinimumSize(400, 500) # Régler la taille de la fenêtre
window.setWindowTitle("A new application") # Titre de la fenêtre
#window.setMinimumHeight(400) # Régler la hauteur minimale de la fenêtre
#window.setMinimumWidth(500) # Idem pour la largeur
window.setWindowIcon(QIcon("application_icon.png")) # Icône de la fenêtre


# Ajout de widgets

#label = QLabel() # Créer un label et le centrer
#label.setPixmap(QPixmap("application_icon.png").scaledToHeight(250))
button = QPushButton("Click Me")
button.setFixedSize(200, 200)
font = window.font()
font.setPointSize(17)
button.setFont(font)
window.setCentralWidget(button)

window.show() # Afficher la fenêtre
app.exec() # Exécuter l'application