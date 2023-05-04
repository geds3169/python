import sys
import os
import sounddevice as sd
import numpy as np
import speech_recognition as sr
import matplotlib.pyplot as plt
import pandas as pd
import subprocess
import threading
import time
import tkinter as tk
import pyaudio
import pyttsx3
import csv
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

# Install with pip install sounddevice numpy speechrecognition matplotlib pandas PyQt5
# pip install --upgrade PyQt5

class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window flags
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Set window geometry
        window_width = 400 # Définir la largeur de la fenêtre
        window_height = 400 # Définir la hauteur de la fenêtre
        screen_geometry = QApplication.desktop().availableGeometry() # Obtenir les informations sur l'écran
        window_x = int((screen_geometry.width() - window_width) / 2) # Calculer la position horizontale de la fenêtre pour la centrer
        window_y = int((screen_geometry.height() - window_height) / 2) # Calculer la position verticale de la fenêtre pour la centrer
        self.setGeometry(QRect(window_x, window_y, window_width, window_height)) # Définir la géométrie de la fenêtre en utilisant les paramètres précédents

        # Set window title
        self.setWindowTitle('J.A.R.V.I.S')

        # Set window layout
        layout = QVBoxLayout()

        # Add background image
        background = QLabel(self)
        pixmap = QPixmap('images/JARVIS.png')
        pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        background.setPixmap(pixmap)
        background.setAlignment(Qt.AlignCenter)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(0, 0)
        background.setGraphicsEffect(shadow)
        layout.addWidget(background)

        # Add J.A.R.V.I.S label to the new QVBoxLayout
        jarvis_label = QLabel(self) # Créer un label pour le texte "J.A.R.V.I.S"
        jarvis_label.setText("J.A.R.V.I.S") # Définir le texte du label
        jarvis_label.setFont(QFont('Arial', 30, QFont.Bold)) # Changer la police et la taille du texte
        jarvis_label.setStyleSheet("color: cyan;") # Changer la couleur du texte
        jarvis_label.setAlignment(Qt.AlignCenter) # Centrer le label horizontalement et verticalement
        jarvis_label.adjustSize() # Ajuster la taille du label en fonction de son contenu
        jarvis_label.move(int(self.width() / 2 - jarvis_label.width() / 2), int(self.height() / 2 - jarvis_label.height() / 2)) # Définir la position du label pour le centrer
        shadow = QGraphicsDropShadowEffect() # Créer un effet d'ombre portée
        shadow.setBlurRadius(10) # Définir le rayon de flou de l'ombre portée
        shadow.setColor(QColor(0, 0, 0, 150)) # Définir la couleur de l'ombre portée (noir semi-transparent)
        shadow.setOffset(0, 10) # Définir le décalage de l'ombre portée par rapport au label
        jarvis_label.setGraphicsEffect(shadow) # Appliquer l'effet d'ombre portée au label

        # Add close button close
        close_button = QPushButton('X', self)
        close_button.setFont(QFont('Arial', 12))
        close_button.setStyleSheet('background-color: red; color: white; border-radius: 15px;')
        close_button.setGeometry(self.width() - 35, 5, 30, 30)
        close_button.clicked.connect(self.close)

        # Set up drop shadow effect for labels and buttons
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(5)
        shadow_effect.setXOffset(0)
        shadow_effect.setYOffset(0)
        shadow_effect.setColor(QColor(0, 0, 0, 100))

        # Set the layout
        self.setLayout(layout)

        # Show the window
        self.show()

        # Initialize the drag position
        self.drag_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Store the position of the mouse click
            self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # Move the window by the distance the mouse has moved
            self.move(event.globalPos() - self.drag_pos)
            event.accept()

    def closeEvent(self, event):
        # Appeler la méthode closeEvent() de la classe parente
        super().closeEvent(event)
        # Fermer l'application
        QApplication.quit()

    def start_voice_recognition(self):
        print('Starting voice recognition...')

    def stop_voice_recognition(self):
        print('Stopping voice recognition...')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TransparentWindow()
    sys.exit(app.exec_())