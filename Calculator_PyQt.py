from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit

class CalcuApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.resize(250, 300)

        self.text_box = QLineEdit()
        self.text_box.setStyleSheet("font: 23pt Helvetica; color: #dbe9f4;")
        self.grid = QGridLayout()

        self.button_list = [
            "7", "8", "9", "/", 
            "4", "5", "6", "*", 
            "1", "2", "3", "-", 
            "0", ".", "=", "+" 
            ]
        
        self.clear = QPushButton("C")
        self.delete = QPushButton("<")
        self.clear.setStyleSheet("QPushButton { font: 15pt Comic Sans MS; color: #f2f3f4; padding: 5px; }")
        self.delete.setStyleSheet("QPushButton { font: 15pt Comic Sans MS; color: #f2f3f4; padding: 5px; }")

        row = 0
        col = 0

        for bt in self.button_list:
            button = QPushButton(bt)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("QPushButton { font: 20pt Comic Sans MS; color: #f2f3f4; padding: 5px; }")
            self.grid.addWidget(button, row, col)

            col += 1

            if col > 3:
                col = 0
                row += 1

        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(15,15,15,15)

        self.setLayout(master_layout)


        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

    def button_click(self):
        button = app.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))

            except Exception as e:
                self.text_box.setText("Error")

        elif text == "C":
            self.text_box.clear()

        elif text == "<": 
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])

        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)

if __name__ in "__main__":
    app = QApplication([])
    main_window = CalcuApp()
    main_window.setStyleSheet("QWidget { background-color: #123}")
    main_window.show()
    app.exec_()
