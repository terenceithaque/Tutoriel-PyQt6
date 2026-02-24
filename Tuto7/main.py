from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class Window(QMainWindow):
    def __init__(self):
        super().__init__() # Initialiser l'objet QMainWindow

        btn = QPushButton("Open file dialog")
        self.setCentralWidget(btn)

        btn.clicked.connect(self.clickHandler) # Afficher une boîte de dialogue d'ouverture de fichiers quand le bouton est cliqué


    def clickHandler(self):
        """Affiche un dialogue d'ouverture de fichiers quand le bouton est cliqué"""
        dialog = QFileDialog() # Dialogue d'ouverture de fichiers
        dialog.setNameFilter("All images (*.png *.jpg)") # Définir les extensions de fichiers acceptées par le dialogue
        dialog.setFileMode(QFileDialog.FileMode.Directory) # L'utilisateur ne peut sélectionner que des dossiers
        dialogSuccessful = dialog.exec()

        print(dialogSuccessful)
        # N'afficher les fichiers que si l'utilisateur a cliqué sur "OK"
        if dialogSuccessful:
            selectedFiles = dialog.selectedFiles() # Récupérer les fichiers sélectionnés par l'utilisateur
            print(selectedFiles)

        else:
            print("User cancelled file dialog")

app = QApplication([]) # Créer une instance de l'application
window = Window() # Créer une instance de fenêtre d'application

window.show()
app.exec()