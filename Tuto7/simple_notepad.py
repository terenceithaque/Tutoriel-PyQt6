from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QGridLayout, QWidget, QFileDialog
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__() # Initialiser l'objet QMainWindow parent
        self.setMinimumSize(500, 300)
        self.setWindowTitle("Notedly")

        parenLayout = QGridLayout() # Disposition des widgets en grille

        self.textEdit = QTextEdit() # Champ d'édition de texte
        saveBtn = QPushButton("Save File")
        openBtn = QPushButton("Open File")

        parenLayout.addWidget(self.textEdit, 0, 0, 1, 2)
        parenLayout.addWidget(saveBtn, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        parenLayout.addWidget(openBtn, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        centralWidget = QWidget()
        centralWidget.setLayout(parenLayout)

        self.setCentralWidget(centralWidget)

        saveBtn.clicked.connect(self.saveHandler) # Enregistrer si le bouton "Save" est cliqué
        openBtn.clicked.connect(self.openHandler) # Ouvrir un fichier si le bouton "Open" est cliqué

    def saveHandler(self):
        """Enregistre le texte présent dans le champ de texte dans un fichier."""
        dialog = QFileDialog() # Dialogue d'enregistrement du fichier
        dialog.setNameFilter("Text File (*.txt)")
        dialogSuccessful = dialog.exec() # Exécuter le dialogue

        if dialogSuccessful: # Si l'utilisateur a cliqué sur "OK"
            fileLocation = dialog.selectedFiles()[0] # Chemin du premier fichier sélectionné
            with open(fileLocation, mode="w") as file:
                file.write(self.textEdit.toPlainText())


    def openHandler(self):
        """Ouvre un fichier texte"""
        dialog = QFileDialog() # Dialogue d'ouverture de fichier
        dialog.setNameFilter("Text File (*.txt)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile) # L'utilisateur ne peut ouvrir un fichier que s'il existe
        
        dialogSuccessful = dialog.exec() # Exécuter le dialogue

        if dialogSuccessful: # Si l'utilisateur a cliqué sur "OK"
            fileLocation = dialog.selectedFiles()[0]  # Chemin du premier fichier sélectionné
            with open(fileLocation) as file: # Ouvrir le fichier en lecture
                self.textEdit.setText(file.read())


app = QApplication([]) # Créer une instance de l'application
window = Window() # Créer une instance de fenêtre de l'application

window.show()
app.exec()