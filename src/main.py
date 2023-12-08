import sys
from PyQt5.QtWidgets import QApplication
from view.principal_view import PrincipalView


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = PrincipalView()
    login.show()
    sys.exit(app.exec_())