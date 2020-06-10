from PyQt5.QtWidgets import QMainWindow, QApplication
from gerador_senha import *
import sys
from random import choice


class Novo(QMainWindow, GrafGerarSenha):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_gerar_senha.clicked.connect(self.gerando_pw)

    def gerando_pw(self):
        coletando = ''
        pw_gerada = ''
        if self.box_numeros.isChecked():
            coletando += '0123456789'
        if self.box_maiuscula.isChecked():
            coletando += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if self.box_minuscula.isChecked():
            coletando += 'abcdefghijklmnopqrstuwxyz'
        if self.box_caractere_especial.isChecked():
            coletando += '@!#$%&*()_+}{^?;:>/-+'
        for c in range(int(self.input_tamanho_senha.currentText())):
            pw_gerada += choice(coletando)
        self.textBrowser.setText(pw_gerada)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
