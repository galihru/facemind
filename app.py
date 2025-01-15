import numpy as np
from selenium import webdriver

class MentalStateAnalyzer:
    def __init__(self):
        # Initialize the web driver for selenium if needed
        self.driver = webdriver.Chrome()

    def calculate_eye_ratio(self, points):
        """Calculate the average eye aspect ratio for both eyes."""
        left_eye = [33, 160, 158, 133, 153, 144]
        right_eye = [362, 385, 387, 263, 373, 380]
        left_eye_points = points[left_eye]
        right_eye_points = points[right_eye]

        def eye_aspect_ratio(eye_points):
            vertical_dist = np.linalg.norm(eye_points[1] - eye_points[5]) + \
                            np.linalg.norm(eye_points[2] - eye_points[4])
            horizontal_dist = np.linalg.norm(eye_points[0] - eye_points[3])
            return vertical_dist / (2.0 * horizontal_dist)

        left_ratio = eye_aspect_ratio(left_eye_points)
        right_ratio = eye_aspect_ratio(right_eye_points)
        return (left_ratio + right_ratio) / 2.0

    def calculate_mouth_ratio(self, points):
        """Calculate the mouth aspect ratio based on given points."""
        mouth = [78, 95, 88, 178, 87, 14]
        vertical_dist = np.linalg.norm(points[13] - points[14])  # Upper to lower lip
        horizontal_dist = np.linalg.norm(points[78] - points[95])  # Mouth width
        return vertical_dist / horizontal_dist

    def calculate_brow_ratio(self, points):
        """Calculate the ratio of brow to eye center distance."""
        brow = [70, 105, 107, 336, 296, 334]
        eye_top = np.mean(points[brow], axis=0)  # Average brow position
        eye_center = np.mean(points[33:133], axis=0)  # Average eye center position
        vertical_dist = np.linalg.norm(eye_top - eye_center)
        return vertical_dist

    def analyze_mental_state(self, points):
        """Analyze mental state based on facial landmarks."""
        eye_ratio = self.calculate_eye_ratio(points)
        mouth_ratio = self.calculate_mouth_ratio(points)
        brow_ratio = self.calculate_brow_ratio(points)

        # Example conditions for mental state analysis
        if eye_ratio < 0.2 and mouth_ratio > 0.5:
            return "Tired or Sleepy"
        elif brow_ratio > 0.3:
            return "Surprised"
        else:
            return "Neutral"


# Example usage with pytest:
# Create sample points array for testing
sample_points = np.random.rand(500, 2)  # 500 random points for illustration
analyzer = MentalStateAnalyzer()
result = analyzer.analyze_mental_state(sample_points)
print(result)
