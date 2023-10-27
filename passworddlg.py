from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class PasswordDlg(QDialog):
    def __init__(self, parent=None):
        super(PasswordDlg, self).__init__(parent)

        passwordLabel = QLabel("&Password:")
        self.passwordEdit = QLineEdit()
        passwordLabel.setBuddy(self.passwordEdit)
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok|
                                     QDialogButtonBox.StandardButton.Cancel)

        layout = QGridLayout()
        layout.addWidget(passwordLabel, 0, 0)
        layout.addWidget(self.passwordEdit, 0, 1)
        layout.addWidget(buttonBox, 1, 0, 1, 2)
        self.setLayout(layout)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        self.setWindowTitle("Set Server Password")

    def result(self):
        return self.passwordEdit.text()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = PasswordDlg()
    form.show()
    app.exec()
