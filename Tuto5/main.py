from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFontDialog, QLabel, QVBoxLayout, QWidget


class Window(QMainWindow):
    """Une fenêtre de l'application"""
    def __init__(self):
        super().__init__() # Initialiser l'objet QMainWindow

        self.setMinimumSize(200,200)

        parentLayout = QVBoxLayout() # Disposition verticale des widgets de la fenêtre

        self.label = QLabel("This is a label")
        self.button = QPushButton("Open Dialog")
        parentLayout.addWidget(self.label)
        parentLayout.addWidget(self.button)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)

        self.button.clicked.connect(self.clickHandler)


    def clickHandler(self):
        """Affiche un dialogue quand le bouton est cliqué."""
        dialog = QFontDialog() # Créer un dialogue de sélection de police

        clickedOk = dialog.exec() # Récupérer le bouton cliqué par l'utilisateur

        if clickedOk: # Si l'utilisateur a cliqué sur "OK"
            self.label.setFont(dialog.currentFont()) # Remplacer la police actuelle du label par celle sélectionnée
            print(dialog.currentFont().family()) # Afficher la famille (nom) de la police

        else:
            print("Dialog Cancelled")

app = QApplication([]) # Créer l'application
window = Window() # Fenêtre de l'application

window.show()
app.exec()