"""
Authors:
    Liat Cohen  205595283
    Adir Biran  308567239
    12/2020
"""

import os

# Project's path
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# Directories paths
FACES_PATH = os.path.join(PROJECT_PATH, 'Faces')
DATA_PATH = os.path.join(PROJECT_PATH, 'Data')
RESOURCES_PATH = os.path.join(PROJECT_PATH, 'Resources')
CLUSTERS_PATH = os.path.join(PROJECT_PATH, 'Clusters')
CONNECTIONS_PATH = os.path.join(PROJECT_PATH, 'Connections')

# Clustering Threshold
CLUSTERING_THRESHOLD = 0.94

# Image Max Sizes
IMAGE_MAX_SIZE = 300

# Face Size
FACE_SIZE = 50

# App Name
APP_NAME = "Socianalyzer"
