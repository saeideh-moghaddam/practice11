from math import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from functools import partial

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('calculator.ui', None)
        self.ui.show()

        self.ui.btn_0.clicked.connect(partial(self.Number_x, 0))
        self.ui.btn_1.clicked.connect(partial(self.Number_x, 1))
        self.ui.btn_2.clicked.connect(partial(self.Number_x, 2))
        self.ui.btn_3.clicked.connect(partial(self.Number_x, 3))
        self.ui.btn_4.clicked.connect(partial(self.Number_x, 4))
        self.ui.btn_5.clicked.connect(partial(self.Number_x, 5))
        self.ui.btn_6.clicked.connect(partial(self.Number_x, 6))
        self.ui.btn_7.clicked.connect(partial(self.Number_x, 7))
        self.ui.btn_8.clicked.connect(partial(self.Number_x, 8))
        self.ui.btn_9.clicked.connect(partial(self.Number_x, 9))

        self.ui.btn_sum.clicked.connect(partial(self.Input, '+'))
        self.ui.btn_sub.clicked.connect(partial(self.Input, '-'))
        self.ui.btn_mult.clicked.connect(partial(self.Input, '*'))
        self.ui.btn_division.clicked.connect(partial(self.Input, '/'))
       
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_clear.clicked.connect(self.reset)
        self.ui.btn_change_sing.clicked.connect(self.Change_sing)
        self.ui.btn_decimal.clicked.connect(self.Decimal)
        self.ui.btn_percentage.clicked.connect(self.Percentage)
        self.ui.btn_sin.clicked.connect(partial(self.Fun_x, 'sin'))
        self.ui.btn_cos.clicked.connect(partial(self.Fun_x, 'cos'))
        self.ui.btn_tan.clicked.connect(partial(self.Fun_x, 'tan'))
        self.ui.btn_cot.clicked.connect(partial(self.Fun_x, 'cot'))
        self.ui.btn_log.clicked.connect(partial(self.Fun_x, 'log'))
        self.ui.btn_power.clicked.connect(partial(self.Fun_x, 'sqrt'))

    def Number_x(self, x):
        self.ui.label.setText(self.ui.label.text() + str(x))

    def Input(self, op):
        try:
            if self.ui.label.text() != '':
                self.num1 = float(self.ui.label.text())
                self.ui.label.setText('')
                self.operator = op
        except:
            self.ui.label.setText('Error')

    def equal(self):
        try:
            if self.ui.label.text() != '':
                self.num2 = float(self.ui.label.text())

                if self.operator == '+':
                    result = self.num1 + self.num2
                elif self.operator == '-':
                    result = self.num1 - self.num2
                elif self.operator == '*':
                    result = self.num1 * self.num2
                elif self.operator == '/':
                    result = self.num1 / self.num2
                
                self.ui.label.setText(str(result))
        except:
            self.ui.label.setText('Error')

    def reset(self):
        self.ui.label.setText('')

    def Change_sing(self):
        if '-' in self.ui.label.text():
            negative = float(self.ui.label.text()) * -1
            self.ui.label.setText(str(negative))
        else:
            self.ui.label.setText('-' + self.ui.label.text())

    def Decimal(self):
        if '.' not in self.ui.label.text() and self.ui.label.text() != '':
            self.ui.label.setText(self.ui.label.text() + '.')

    def Percentage(self):
        try:
            if self.ui.label.text() != '':
                cent = float(self.ui.label.text()) / 100
                self.ui.label.setText(str(cent))
        except:
            self.ui.label.setText('Error')       

    def Fun_x(self, t):
        try:
            if self.ui.label.text() != '':
                text = radians(float(self.ui.label.text()))

                if t == 'sin':
                    result = sin(text)
                elif t == 'cos':
                    result = cos(text)
                elif t == 'tan':
                    result = tan(text)
                elif t == 'cot':
                    result = cos(text) / sin(text)
                elif t == 'log':
                    result = log(float(self.ui.label.text()))
                elif t == 'sqrt':
                    result = sqrt(float(self.ui.label.text()))
                
                result = round(result, 6)
                self.ui.label.setText(str(result))
        except:
            self.ui.label.setText('Error')

app = QApplication()
window = Calculator()

app.exec()