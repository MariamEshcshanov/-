my.app.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
from second_win import*
from instr import*
class MainWin(QWidget):
    def __init__(self):
        super().set_apper()
        self.set_appear() #устанавливает внешний вид
        self.initUI() #граф элементы
        self.connects() #связь меж элементами
        self.show() # делает видимым

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_text = QLabel(txt_hello) #надпись
        self.instruction = QLabel(txt_instruction)#надпись
        self.button = QPushButtom(txt_next)#кнопку
        self.layout = QVBoxLayout() #направляющая
        self.hello_text.addWidhet(self.layout)
        self.instruction.addWidhet(self.layout)
        self.button.addWidhet(self.layout)

    def connects():
        self.btn_next.clicked.connect(self.new_click)
    
    def new_click(self):
        self.hide()
        self.tw = TestWin()


