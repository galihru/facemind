# setup.py
from setuptools import setup, find_packages

setup(
    name='mental_health_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'pandas',
        'matplotlib',
        'mediapipe',
        'selenium',
        'PyQt5',
    ],
    entry_points={
        'console_scripts': [
            'mental_health_app=mental_health_app.main:main',
        ],
    },
)
