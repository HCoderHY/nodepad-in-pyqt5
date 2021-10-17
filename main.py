import pyautogui
from PyQt5.QtWidgets import QApplication, QMenuBar, QMenu, QFileDialog
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("<+NodePad->")
        self.setStyleSheet("background-color: #252526;")
        self.setGeometry(50,80,1800,925)
        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.setGeometry(0,45,1920,1010)
        self.text_edit.setStyleSheet("background-color: #1C2B33; color: #CDD3D5; font-size: 15px; font-family: Noto Sans, sans-serif; border: 2px solid #252526; border-radius: 5%; margin: 5px")
        self.createMenuBar()
        self.pushButton = QtWidgets.QPushButton()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        self.menuBar.setStyleSheet("background-color: #323233; color: #8E8E8E;")

        fileMenu = QMenu("&File", self)
        self.menuBar.addMenu(fileMenu)
        editMenu = QMenu("&Edit", self)
        self.menuBar.addMenu(editMenu)

        copy = editMenu.addAction("Copy", self.actions_clicked)
        cut = editMenu.addAction("Cut", self.actions_clicked)
        paste = editMenu.addAction("Paste", self.actions_clicked)
        s_a = editMenu.addAction("Select All", self.actions_clicked)
        u_t = editMenu.addAction("Undo Typing", self.actions_clicked)
        redo = editMenu.addAction("Redo", self.actions_clicked)
        delete = editMenu.addAction("Delete", self.actions_clicked)

        open = fileMenu.addAction("Open", self.actions_clicked)
        save = fileMenu.addAction("Save", self.actions_clicked)
        exit = fileMenu.addAction("Exit", self.actions_clicked)

    @QtCore.pyqtSlot()
    def actions_clicked(self):
        save_l = False
        action = self.sender()
        if action.text() == "Open":
            fname = QFileDialog.getOpenFileName(self)[0]
            try:
                f = open(fname, 'r')
                print(fname)
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
            except FileNotFoundError:
                pass
        elif action.text() == "Save":
            fname = QFileDialog.getSaveFileName(self)[0]
            try:
                f = open(fname, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                save_l = True
            except FileNotFoundError:
                pass
        elif action.text() == "Exit":
            if save_l == False:
                save_file = QMessageBox()
                save_file.setWindowTitle("Save file")
                save_file.setIcon(QMessageBox.Warning)
                save_file.setText("You want save file?")
                save_file.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                save_file.exec_()
                if save_file.StandardButton.Ok:
                    fname = QFileDialog.getSaveFileName(self)[0]
                    try:
                        f = open(fname, 'w')
                        text = self.text_edit.toPlainText()
                        f.write(text)
                    except FileNotFoundError:
                        pass
                elif save_file.StandardButton.Cancel:
                    pass

                sys.exit()

        elif action.text() == "Undo Typing":
            pyautogui.hotkey("ctrl", 'z')
        elif action.text() == "Redo":
            pyautogui.hotkey("ctrl", 'y')
        elif action.text() == "Copy":
            pyautogui.hotkey("ctrl", 'c')
        elif action.text() == "Cut":
            pyautogui.hotkey("ctrl", 'x')
        elif action.text() == "Paste":
            pyautogui.hotkey("ctrl", 'v')
        elif action.text() == "Select All":
            pyautogui.hotkey("ctrl", 'a')
        elif action.text() == "Delete":
            pyautogui.press("delete")


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


application()
