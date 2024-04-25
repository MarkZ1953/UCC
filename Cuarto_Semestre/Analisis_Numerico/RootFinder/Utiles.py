from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QLabel


class Etiqueta(QLabel):
    def __init__(self, ruta_imagen=None, texto="", bold=False, font="Arial", font_size=10):
        super().__init__()

        self.setText(texto)
        font = QFont(font, font_size)
        self.setContentsMargins(0, 0, 0, 0)

        if bold:
            font.setBold(True)

        if ruta_imagen is not None:
            pixmap = QPixmap(ruta_imagen)
            pixmap.scaled(32, 32)
            self.setPixmap(pixmap)

        self.setFont(font)