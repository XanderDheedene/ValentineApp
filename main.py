from PyQt5.QtWidgets import QMessageBox, QApplication
import sys


def we_pressed_no(msg, count):
    if count < 5:
        msg.setText("Please")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        res = msg.exec_()
        if res == QMessageBox.Yes:
            yessss(msg)
        else:
            we_pressed_no(msg, count + 1)
    else:
        msg.setText("Fuck you :(")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        sys.exit()


def yessss(msg):
    msg.setText("Are you joking?")
    result2 = msg.exec_()
    msg.setIcon(QMessageBox.NoIcon)
    if result2 == QMessageBox.Yes:
        msg.setText("Bruh, fuck you :(")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    else:
        msg.setText("Really?? nicee, msg me via whatever platform you like :))")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    sys.exit()


app = QApplication(sys.argv)

msg = QMessageBox()
msg.setIcon(QMessageBox.Warning)
msg.setWindowTitle(" ")
msg.setText("Your pc has been hacked, LOL (/jk)")
msg.setStandardButtons(QMessageBox.Ok)
msg.exec_()

msg.setText("However, I've just got one question for you...")
msg.setStandardButtons(QMessageBox.Ok)
msg.exec_()
msg.setText("Will you be my valentine?")
msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
result = msg.exec_()
if result == QMessageBox.Yes:
    yessss(msg)
else:
    we_pressed_no(msg, 0)


