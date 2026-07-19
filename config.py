"""
===========================================================
Configuration File
Project : Jas Quantum Security Toolkit
===========================================================
"""

# -------------------------
# Simulation Settings
# -------------------------

NUM_BITS = 100

QBER_THRESHOLD = 11.0

# -------------------------
# Quantum Bases
# -------------------------

RECTILINEAR = "+"
DIAGONAL = "x"

BASES = [
    RECTILINEAR,
    DIAGONAL
]

# -------------------------
# Binary Values
# -------------------------

ZERO = 0
ONE = 1

# -------------------------
# Output Folder
# -------------------------

OUTPUT_FOLDER = "outputs"

# -------------------------
# Graph Names
# -------------------------

ACCURACY_FILE = "accuracy.png"

QBER_FILE = "qber.png"

KEY_FILE = "key_distribution.png"

ATTACK_FILE = "attack_analysis.png"

# -------------------------
# Project Info
# -------------------------

PROJECT_NAME = "Jas Quantum Security Toolkit"

AUTHOR = "Jasmine"

VERSION = "2.0"

LINE = "=" * 70