import sys
import cv2
import numpy as np
import mediapipe as mp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, 
                           QWidget, QMainWindow, QLineEdit, QMessageBox, QAction)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap, QImage
import subprocess
import pkg_resources
required = {'opencv-python', 'numpy', 'mediapipe', 'selenium', 'PyQt5'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing])


class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Splash Screen")
        self.setFixedSize(800, 600)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        layout = QVBoxLayout()
        logo = QLabel()
        pixmap = QPixmap(r"C:\Users\asus\Downloads\logofm.png").scaled(400, 136, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        label = QLabel("Welcome to Mental Health App")
        label.setAlignment(Qt.AlignCenter)
        layout.addStretch()
        layout.addWidget(logo)
        container = QWidget()
        container.setObjectName("container")
        container.setLayout(layout)
        self.setStyleSheet("""
            QMainWindow {
                border-radius: 20px;
                background-color: white;
            }
        """)
        layout.addStretch()
        self.setCentralWidget(container)
        layout = QVBoxLayout()
        logo = QLabel()
        pixmap = QPixmap(r"C:\Users\asus\Downloads\logofm.png").scaled(400, 136, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        label = QLabel("Welcome to Mental Health App")
        label.setAlignment(Qt.AlignCenter)
        layout.addStretch()
        layout.addWidget(logo)
        container = QWidget()
        container.setObjectName("container")
        container.setLayout(layout)
        layout.addStretch()
        self.setCentralWidget(container)

    def showSplash(self):
        self.show()
        QTimer.singleShot(3000, self.close)


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(800, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 18px;
                color: #333;
            }
            QLineEdit {
                font-size: 16px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QPushButton {
                font-size: 16px;
                padding: 10px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QMenuBar {
                background-color: #f0f0f0;
            }
            QMenuBar::item {
                background-color: #f0f0f0;
                color: #333;
            }
            QMenuBar::item:selected {
                background-color: #e0e0e0;
                color: #333;
            }
            QMenu {
                background-color: #f0f0f0;
                color: #333;
            }
            QMenu::item:selected {
                background-color: #e0e0e0;
                color: #333;
            }
        """)
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        help_menu = menubar.addMenu('Help')
        about_menu = menubar.addMenu('About')

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(QApplication.instance().quit)
        file_menu.addAction(exit_action)

        help_action = QAction('Help', self)
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)

        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about)
        about_menu.addAction(about_action)

        layout = QVBoxLayout()
        logo = QLabel()
        pixmap = QPixmap(r"C:\Users\asus\Downloads\layarui.png").scaledToWidth(self.width(), Qt.SmoothTransformation)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)
        label = QLabel("Login to your account")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Username')
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login to Instagram')
        self.login_button.clicked.connect(self.login_instagram)
        self.start_analysis_button = QPushButton('Start Mental Health Analysis')
        self.start_analysis_button.clicked.connect(self.start_analysis)
        self.start_analysis_button.setEnabled(False)
        self.status_label = QLabel('')
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.start_analysis_button)
        layout.addWidget(self.status_label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.driver = None

    def show_help(self):
        QMessageBox.information(self, "Help", "This is the help section.")

    def show_about(self):
        QMessageBox.information(self, "About", "Mental Health App v1.0")

    def login_instagram(self):
        self.status_label.setText('Logging in...')
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/accounts/login/')
        wait = WebDriverWait(self.driver, 10)
        username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        username_field.send_keys(self.username_input.text())
        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(self.password_input.text())
        password_field.send_keys(Keys.RETURN)
        wait.until(EC.url_contains('instagram.com'))
        if 'login' not in self.driver.current_url:
            self.status_label.setText('Login successful! You can now start the analysis.')
            self.start_analysis_button.setEnabled(True)
            self.login_button.setEnabled(False)
        else:
            self.status_label.setText('Login failed. Please try again.')
            self.driver.quit()
            self.driver = None

    def start_analysis(self):
        if self.driver:
            self.main_window = MentalHealthPredictor()
            self.main_window.show()
            self.hide()
        else:
            self.status_label.setText('Please login first')

    def closeEvent(self, event):
        if self.driver:
            self.driver.quit()
        event.accept()


class MentalHealthPredictor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setupFaceDetection()
        self.startVideo()

    def setupFaceDetection(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.drawing_spec = self.mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
        self.cap = cv2.VideoCapture(0)

    def initUI(self):
        self.setWindowTitle('Mental Health Analysis')
        self.setMinimumSize(800, 600)
        layout = QVBoxLayout()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.prediction_label = QLabel('Analyzing...')
        self.prediction_label.setAlignment(Qt.AlignCenter)
        self.back_button = QPushButton('Back to Login')
        self.back_button.clicked.connect(self.back_to_login)
        layout.addWidget(self.image_label)
        layout.addWidget(self.prediction_label)
        layout.addWidget(self.back_button)
        self.setLayout(layout)

    def back_to_login(self):
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, LoginWindow):
                widget.show()
        self.close()

    def startVideo(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face_mesh.process(rgb_frame)
            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    self.mp_drawing.draw_landmarks(
                        image=frame,
                        landmark_list=face_landmarks,
                        connections=self.mp_face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=self.drawing_spec,
                        connection_drawing_spec=self.drawing_spec)
                    mental_state = self.analyze_mental_state(face_landmarks, frame.shape)
                    self.prediction_label.setText(f'Mental State: {mental_state}')
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.image_label.setPixmap(QPixmap.fromImage(qt_image))

    def analyze_mental_state(self, landmarks, frame_shape):
        height, width = frame_shape[:2]
        points = np.array([(lm.x * width, lm.y * height) for lm in landmarks.landmark])
        eye_ratio = self.calculate_eye_ratio(points)
        mouth_ratio = self.calculate_mouth_ratio(points)
        brow_ratio = self.calculate_brow_ratio(points)
        if eye_ratio < 0.2:
            return "Fatigue Detected"
        elif mouth_ratio > 0.5:
            return "Positive Mood"
        elif brow_ratio > 0.3:
            return "Stressed/Concerned"
        else:
            return "Neutral"

    def calculate_eye_ratio(self, points):
        left_eye = [33, 160, 158, 133, 153, 144]
        right_eye = [362, 385, 387, 263, 373, 380]
        left_eye_points = points[left_eye]
        right_eye_points = points[right_eye]
        def eye_aspect_ratio(eye_points):
            vertical_dist = np.linalg.norm(eye_points[1] - eye_points[5]) + \
                          np.linalg.norm(eye_points[2] - eye_points[4])
            horizontal_dist = np.linalg.norm(eye_points[0] - eye_points[3]) * 2
            return vertical_dist / horizontal_dist if horizontal_dist != 0 else 0
        left_ear = eye_aspect_ratio(left_eye_points)
        right_ear = eye_aspect_ratio(right_eye_points)
        return (left_ear + right_ear) / 2

    def calculate_mouth_ratio(self, points):
        mouth_points = [61, 291, 0, 17]
        mouth_pts = points[mouth_points]
        vertical_dist = np.linalg.norm(mouth_pts[2] - mouth_pts[3])
        horizontal_dist = np.linalg.norm(mouth_pts[0] - mouth_pts[1])
        return vertical_dist / horizontal_dist if horizontal_dist != 0 else 0

    def calculate_brow_ratio(self, points):
        left_brow = [70, 63, 105, 66, 107]
        left_eye = [159, 145, 133]
        brow_points = points[left_brow]
        eye_points = points[left_eye]
        brow_height = np.mean(brow_points[:, 1])
        eye_height = np.mean(eye_points[:, 1])
        return (eye_height - brow_height) / (points[152, 1] - points[10, 1])

    def closeEvent(self, event):
        self.cap.release()
        self.face_mesh.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = SplashScreen()
    login_window = LoginWindow()
    splash.showSplash()
    QTimer.singleShot(3000, login_window.show)
    sys.exit(app.exec_())
