from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton,QGridLayout, QWidget, QLabel
from PyQt6.QtCore import Qt

app = QApplication([]) # Créer l'application
window = QMainWindow() # Créer la fenêtre de l'application

window.setMinimumSize(400, 400)

parentLayout = QGridLayout() # Créer une disposition "parent" qui représente la disposition générale des widgets



label = QLabel("This is a label", alignment=Qt.AlignmentFlag.AlignCenter) # Ajouter un label centré. Cela le décale d'une colonne dans la disposition en grille.
parentLayout.addWidget(label,0,0, 1, 2) # Ajouter le label à la disposition "parent". On spécifie également la ligne et la colonne. Les attributs rowSpan et columnSpan définissent la portée de la ligne et de la colonne.

button1 = QPushButton("Button 1")
button2 = QPushButton("Button 2")
# Définir les boutons comme cibles de la disposition verticale
parentLayout.addWidget(button1, 1, 0)
parentLayout.addWidget(button2, 1, 1)
parentLayout.setRowMinimumHeight(1, 200) # Changer la hauteur de la deuxième colonne
parentLayout.setHorizontalSpacing(50) # Espacer les widgets horizontalement. Cela modifie l'espacement entre les colonnes.



centerWidget = QWidget() # Créer un widget central pour la fenêtre  afin d'appliquer la disposition verticale à tous les éléments
centerWidget.setLayout(parentLayout)

window.setCentralWidget(centerWidget)

window.show() # Afficher la fenêtre
app.exec() # Exécuter l'application