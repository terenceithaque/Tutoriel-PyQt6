from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QRadioButton, QButtonGroup
from PyQt6.QtGui import QIcon


class Window(QMainWindow):
    """Une instance de fenêtre de l'application"""
    def __init__(self):
        super().__init__() # Initialiser la classe parente (QMainWindow)
        
        self.setMinimumSize(400, 150)
        parentLayout = QVBoxLayout()
        self.buttonGroup = QButtonGroup() # Créer un groupe de boutons

        self.radioButtonRed = QRadioButton("Red")
        self.radioButtonYellow = QRadioButton("Yellow")
        self.radioButtonBlue = QRadioButton("Blue")
        self.button = QPushButton("Click me")


        # Ajouter les boutons radio au groupe de boutons
        self.buttonGroup.addButton(self.radioButtonRed)
        self.buttonGroup.addButton(self.radioButtonYellow)
        self.buttonGroup.addButton(self.radioButtonBlue)
        


    
        self.button.clicked.connect(self.clickHandler) # Configurer le bouton pour appeller la méthode clickHandler() quand il est cliqué

        parentLayout.addWidget(self.radioButtonRed)
        parentLayout.addWidget(self.radioButtonBlue)
        parentLayout.addWidget(self.radioButtonYellow)

        parentLayout.addWidget(self.button)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)


    def clickHandler(self):
        """Méthode appellée quand le bouton est cliqué"""
        print("Button Clicked!")
        print(self.buttonGroup.checkedButton().text())


    

    

app = QApplication([]) # Créer l'application
window = Window() # Créer la fenêtre de l'application



window.show()
app.exec()