from design import Ui_MainWindow # Importer le fichier de design créé
from PyQt6.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow, Ui_MainWindow):
    """Une fenêtre de l'application"""
    def __init__(self):
        super().__init__() # Initalisation du parent QMainWindow
        self.setupUi(self) # Configurer l'interface grâce au design créé


        self.pushButton.clicked.connect(self.clickHandler) # Connecter la fonction clickHandler au bouton 'Add'


    def clickHandler(self):
        """Méthode appellée lors du clic du bouton 'Add'"""
        print("Clicked!")

        entered_task = self.lineEdit.text()
        if entered_task.strip() != "":
            self.listWidget.addItem(entered_task)
            self.lineEdit.setText("")

app = QApplication([]) # Création de l'application
window = Window() # Création de la fenêtre

window.show()
app.exec()