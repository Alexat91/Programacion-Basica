import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, QMessageBox
)

# Funciones matemáticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Interfaz
class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Básica")
        self.setGeometry(100, 100, 300, 200)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.input1 = QLineEdit(self)
        self.input1.setPlaceholderText("Número 1")
        self.input2 = QLineEdit(self)
        self.input2.setPlaceholderText("Número 2")

        self.resultado = QLabel("Resultado:", self)

        botones_layout = QHBoxLayout()
        self.boton_suma = QPushButton("Suma", self)
        self.boton_resta = QPushButton("Resta", self)
        self.boton_mult = QPushButton("Multiplicación", self)
        self.boton_div = QPushButton("División", self)

        for boton in [self.boton_suma, self.boton_resta, self.boton_mult, self.boton_div]:
            botones_layout.addWidget(boton)

        self.boton_suma.clicked.connect(self.operar)
        self.boton_resta.clicked.connect(self.operar)
        self.boton_mult.clicked.connect(self.operar)
        self.boton_div.clicked.connect(self.operar)

        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addLayout(botones_layout)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def operar(self):
        sender = self.sender().text()
        try:
            a = float(self.input1.text())
            b = float(self.input2.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor ingrese números válidos.")
            return

        if sender == "Suma":
            res = suma(a, b)
        elif sender == "Resta":
            res = resta(a, b)
        elif sender == "Multiplicación":
            res = multiplicacion(a, b)
        elif sender == "División":
            res = division(a, b)

        self.resultado.setText(f"Resultado: {res}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec_())