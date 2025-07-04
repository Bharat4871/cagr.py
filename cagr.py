from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QMessageBox
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")

        self.num1_input = QLineEdit(self)
        self.num1_input.setPlaceholderText("Enter first number")

        self.num2_input = QLineEdit(self)
        self.num2_input.setPlaceholderText("Enter second number")

        self.operation = QComboBox(self)
        self.operation.addItems(["Add", "Subtract", "Multiply", "Divide"])

        self.result_label = QLabel("Result: ", self)

        self.calc_button = QPushButton("Calculate", self)
        self.calc_button.clicked.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addWidget(self.num1_input)
        layout.addWidget(self.num2_input)
        layout.addWidget(self.operation)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self):
        try:
            a = float(self.num1_input.text())
            b = float(self.num2_input.text())
            op = self.operation.currentText()

            if op == "Add":
                result = a + b
            elif op == "Subtract":
                result = a - b
            elif op == "Multiply":
                result = a * b
            elif op == "Divide":
                if b == 0:
                    raise ZeroDivisionError
                result = a / b

            self.result_label.setText(f"Result: {result}")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers.")
        except ZeroDivisionError:
            QMessageBox.warning(self, "Math Error", "Cannot divide by zero.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
