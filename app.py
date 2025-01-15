import sys
import cv2
import numpy as np
import mediapipe as mp
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
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
required = {'opencv-python', 'csv', 'datetime', 'pandas', 'matplotlib', 'numpy', 'mediapipe', 'selenium', 'PyQt5'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing])

# Fungsi untuk menyimpan prediksi ke file CSV
def save_to_database(prediction):
    filename = "mental_health_predictions.csv"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, prediction])

# Fungsi untuk menampilkan grafik monitoring prediksi mental health dan menghitung akurasi
def show_graph(date_filter=None):
    # Membaca data dari CSV
    data = pd.read_csv("mental_health_predictions.csv", names=["Time", "Prediction"])
    data["Time"] = pd.to_datetime(data["Time"])

    if date_filter:
        data = data[data["Time"].dt.date == date_filter]

    # Mapping prediksi ke angka untuk grafik
    predictions_map = {"Neutral": 0, "Fatigue Detected": 1, "Positive Mood": 2, "Stressed/Concerned": 3}
    data["Prediction Value"] = data["Prediction"].map(predictions_map)

    # Membuat grafik dengan warna berbeda untuk setiap prediksi
    plt.figure(figsize=(12, 8))
    colors = {'Neutral': 'blue', 'Fatigue Detected': 'red', 'Positive Mood': 'green', 'Stressed/Concerned': 'orange'}
    for prediction, group_data in data.groupby("Prediction"):
        plt.plot_date(group_data["Time"], group_data["Prediction Value"], linestyle='solid', marker='o', color=colors[prediction], label=prediction)

    plt.xlabel("Time")
    plt.ylabel("Prediction")
    plt.title("Mental Health Prediction Monitoring")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()

    # Tampilkan grafik
    plt.show()

    # Menghitung akurasi prediksi
    total_predictions = len(data)
    correct_predictions = data["Prediction"].value_counts().max()
    accuracy = (correct_predictions / total_predictions) * 100

    print(f"Total Predictions: {total_predictions}")
    print(f"Correct Predictions: {correct_predictions}")
    print(f"Accuracy: {accuracy:.2f}%")

    # Kesimpulan akhir prediksi emosi
    final_prediction = data["Prediction"].iloc[-1]
    print(f"Kesimpulan akhir prediksi emosi: {final_prediction}")

    # Saran untuk mengatasi atau mengurangi emosi
    suggestions = {
        "Neutral": "Pertahankan kondisi Anda saat ini dan terus lakukan aktivitas yang positif.",
        "Fatigue Detected": "Istirahat yang cukup, tidur yang berkualitas, dan hindari stres berlebihan.",
        "Positive Mood": "Lanjutkan aktivitas yang membuat Anda bahagia dan berbagi kebahagiaan dengan orang lain.",
        "Stressed/Concerned": "Lakukan relaksasi, meditasi, atau aktivitas yang menenangkan. Jangan ragu untuk mencari bantuan profesional jika diperlukan."
    }
    print(f"Saran: {suggestions.get(final_prediction, 'Tidak ada saran yang tersedia.')}")

    # Grafik akurasi prediksi
    plt.figure(figsize=(12, 8))
    plt.plot(data["Time"], data["Prediction Value"], label="Detected Emotion", color='blue', linestyle='solid', marker='o')
    plt.plot(data["Time"], data["Prediction Value"].rolling(window=10).mean(), label="Predicted Emotion", color='red', linestyle='dashed')
    plt.xlabel("Time")
    plt.ylabel("Prediction Value")
    plt.title("Detected vs Predicted Emotion")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()

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
        monitoring_menu = menubar.addMenu('Monitoring')

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(QApplication.instance().quit)
        file_menu.addAction(exit_action)

        help_action = QAction('Help', self)
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)

        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about)
        about_menu.addAction(about_action)

        show_graph_action = QAction('Show Monitoring Graph', self)
        show_graph_action.triggered.connect(self.show_graph)
        monitoring_menu.addAction(show_graph_action)

        layout = QVBoxLayout()
        logo = QLabel()
        pixmap = QPixmap(r"C:\Users\asus\Downloads\layarui.png").scaledToWidth(self.width(), Qt.SmoothTransformation)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)
        label = QLabel("Login to your account")
        layout.addWidget(label)
        label.setAlignment(Qt.AlignCenter)
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

    def show_graph(self):
        # Panggil fungsi untuk menampilkan grafik
        show_graph()

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
            self.status_label.setText('Login failed. Please check your credentials.')
            self.status_label.setText('Login successful! You can now start the analysis.')
            self.start_analysis_button.setEnabled(True)
            self.login_button.setEnabled(False)

    def start_analysis(self):
        if self.driver:
            self.main_window = MentalHealthPredictor()
            self.main_window.show()
            self.hide()
            self.monitor_instagram_posts()
        else:
            self.status_label.setText('Please login first')

    def monitor_instagram_posts(self):
        # Monitor Instagram posts and analyze user's emotion
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_posts)
        self.timer.start(1000)  # Check every second

    def check_posts(self):
        self.driver.get('https://www.instagram.com/')
        wait = WebDriverWait(self.driver, 10)
        posts = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article div div div div a')))
        for post in posts:
            post.click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.C4VMK span')))
            self.main_window.update_frame()
            self.driver.back()
            # Check the latest prediction
            latest_prediction = self.main_window.prediction_label.text().split(': ')[-1]
            if latest_prediction in ["Fatigue Detected", "Stressed/Concerned"]:
                self.driver.quit()
                QMessageBox.warning(self, "Warning", "Detected mental health issue. Instagram will be closed.")
                break

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
                    save_to_database(mental_state)
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
