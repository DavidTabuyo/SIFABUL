import sys
from PyQt5.QtWidgets import QApplication
from inicio_sesion import InicioSesion


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = InicioSesion()
    demo.show()
    sys.exit(app.exec_())