from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QGridLayout, QLabel, QPushButton, QWidget
from PyQt6.QtCore import Qt

# Challenge: créer un formulaire avec un label de connexion, deux champs de saisie, un bouton d'envoi et une dimension de 400×400

app = QApplication([])
window = QMainWindow()

window.setMinimumSize(400,400)

parentLayout = QGridLayout()

loginLabel = QLabel("Login", alignment=Qt.AlignmentFlag.AlignCenter)
loginLabel.setMaximumHeight(100)
emailLabel = QLabel("Email: ")
passwordLabel = QLabel("Password: ")

emailInput = QLineEdit() # Champ de saisie de l'adresse email
passwordInput = QLineEdit() # Champ de saisie pour le mot de passe
passwordInput.setEchoMode(QLineEdit.EchoMode.Password) # Passer le champ de saisie du mot de passe en "echo mode" afin de masquer la saisie

submitButton = QPushButton("Submit") # Bouton de connexion

# Ajouter les widgets à la disposition "parent"
parentLayout.addWidget(loginLabel, 0, 0, 1, 2)
parentLayout.addWidget(emailLabel, 1, 0)
parentLayout.addWidget(emailInput, 1, 1)
parentLayout.addWidget(passwordLabel, 2, 0)
parentLayout.addWidget(passwordInput, 2, 1)
parentLayout.addWidget(submitButton, 3, 0, 1, 2)


# Créer un widget central
centerWidget = QWidget()
centerWidget.setLayout(parentLayout)
window.setCentralWidget(centerWidget)

window.show()
app.exec()