"""
===========================================================
Visualization Module
Project : Jas Quantum Security Toolkit
===========================================================
"""

import os
import matplotlib.pyplot as plt

from config import *


class Visualizer:

    def __init__(self):

        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # --------------------------------------------------

    def plot_accuracy(self, accuracy):

        plt.figure(figsize=(8, 5))

        plt.bar(
            ["Correct", "Incorrect"],
            [accuracy, 100 - accuracy],
            color=["green", "red"]
        )

        plt.ylim(0, 100)

        plt.ylabel("Percentage")

        plt.title("Measurement Accuracy")

        plt.savefig(
            os.path.join(
                OUTPUT_FOLDER,
                ACCURACY_FILE
            )
        )

        plt.close()

    # --------------------------------------------------

    def plot_qber(self, qber):

        plt.figure(figsize=(8, 5))

        plt.bar(
            ["Measured", "Threshold"],
            [qber, QBER_THRESHOLD],
            color=["orange", "blue"]
        )

        plt.ylabel("Percentage")

        plt.title("Quantum Bit Error Rate")

        plt.savefig(
            os.path.join(
                OUTPUT_FOLDER,
                QBER_FILE
            )
        )

        plt.close()

    # --------------------------------------------------

    def plot_secret_key(self, total_bits, secret_key_length):

        discarded = total_bits - secret_key_length

        plt.figure(figsize=(6, 6))

        plt.pie(
            [secret_key_length, discarded],
            labels=["Secret Key", "Discarded"],
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Secret Key Distribution")

        plt.savefig(
            os.path.join(
                OUTPUT_FOLDER,
                KEY_FILE
            )
        )

        plt.close()

    # --------------------------------------------------

    def plot_attack(self, detection_rate):

        plt.figure(figsize=(8, 5))

        plt.bar(
            ["Attack", "Safe"],
            [detection_rate, 100 - detection_rate],
            color=["crimson", "green"]
        )

        plt.ylim(0, 100)

        plt.ylabel("Percentage")

        plt.title("Eve Attack Analysis")

        plt.savefig(
            os.path.join(
                OUTPUT_FOLDER,
                ATTACK_FILE
            )
        )

        plt.close()

    # --------------------------------------------------

    def generate_all_graphs(self, bb84, eve):

        self.plot_accuracy(bb84.accuracy)

        self.plot_qber(bb84.qber)

        self.plot_secret_key(
            bb84.num_bits,
            len(bb84.alice_key)
        )

        self.plot_attack(
            eve.last_detection_rate
        )

        print("\nGraphs saved successfully!")