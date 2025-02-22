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
    author='GALIH RIDHO UTOMO',
    author_email='g4lihru@students.unnes.ac.id',
    description='A mental health prediction app using facial analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/4211421036/facemind',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
