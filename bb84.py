"""
===========================================================
BB84 Quantum Key Distribution
Project : Jas Quantum Security Toolkit
===========================================================
"""

import random

from config import *

from utils import (
    generate_random_bits,
    generate_random_bases,
    compare_bases,
    extract_secret_key,
    calculate_qber,
    calculate_accuracy
)


class BB84Protocol:

    def __init__(self, num_bits=NUM_BITS):

        self.num_bits = num_bits

        self.reset()

    # --------------------------------------------------

    def reset(self):

        self.alice_bits = []

        self.alice_bases = []

        self.bob_bits = []

        self.bob_bases = []

        self.matching = []

        self.alice_key = []

        self.bob_key = []

        self.qber = 0

        self.accuracy = 0

    # --------------------------------------------------

    def generate_alice_data(self):

        self.alice_bits = generate_random_bits(
            self.num_bits
        )

        self.alice_bases = generate_random_bases(
            self.num_bits
        )

    # --------------------------------------------------

    def generate_bob_bases(self):

        self.bob_bases = generate_random_bases(
            self.num_bits
        )

    # --------------------------------------------------

    def transmit(self, eve=None):

        """
        Alice → Eve → Bob

        If Eve is absent,
        Bob receives Alice's original qubits.

        If Eve exists,
        Bob receives Eve's resent qubits.
        """

        if eve is None:

            transmitted_bits = self.alice_bits

            transmitted_bases = self.alice_bases

        else:

            transmitted_bits, transmitted_bases = (

                eve.intercept_resend(

                    self.alice_bits,

                    self.alice_bases

                )

            )

        self.bob_bits = []

        for bit, basis, bob_basis in zip(

                transmitted_bits,

                transmitted_bases,

                self.bob_bases):

            if basis == bob_basis:

                self.bob_bits.append(bit)

            else:

                self.bob_bits.append(

                    random.randint(0, 1)

                )

    # --------------------------------------------------

    def reconcile(self):

        self.matching = compare_bases(

            self.alice_bases,

            self.bob_bases

        )

        self.alice_key = extract_secret_key(

            self.alice_bits,

            self.matching

        )

        self.bob_key = extract_secret_key(

            self.bob_bits,

            self.matching

        )

    # --------------------------------------------------

    def analyse(self):

        self.qber = calculate_qber(

            self.alice_key,

            self.bob_key

        )

        self.accuracy = calculate_accuracy(

            self.alice_key,

            self.bob_key

        )

    # --------------------------------------------------

    def is_secure(self):

        return self.qber <= QBER_THRESHOLD
    # --------------------------------------------------

    def security_message(self):

        if self.is_secure():

            return "Secure Communication"

        return "Possible Eavesdropping Detected"

    # --------------------------------------------------

    def run_protocol(self, eve=None):

        self.reset()

        self.generate_alice_data()

        self.generate_bob_bases()

        self.transmit(eve)

        self.reconcile()

        self.analyse()

        return self.get_statistics()

    # --------------------------------------------------

    def get_statistics(self):

        return {

            "Total Bits": self.num_bits,

            "Matching Bases": sum(self.matching),

            "Secret Key Length": len(self.alice_key),

            "QBER": round(self.qber, 2),

            "Accuracy": round(self.accuracy, 2),

            "Security": self.security_message()

        }

    # --------------------------------------------------

    def display_data(self):

        print("\n" + LINE)

        print("BB84 QUANTUM KEY DISTRIBUTION".center(70))

        print(LINE)

        print("\nAlice Bits")

        print(self.alice_bits)

        print("\nAlice Bases")

        print(self.alice_bases)

        print("\nBob Bases")

        print(self.bob_bases)

        print("\nBob Measured Bits")

        print(self.bob_bits)

        print("\nMatching Bases")

        print(self.matching)

        print("\nAlice Secret Key")

        print(self.alice_key)

        print("\nBob Secret Key")

        print(self.bob_key)

    # --------------------------------------------------

    def print_report(self):

        stats = self.get_statistics()

        print("\n" + LINE)

        print("FINAL REPORT".center(70))

        print(LINE)

        print(f"Total Qubits           : {stats['Total Bits']}")

        print(f"Matching Bases         : {stats['Matching Bases']}")

        print(f"Secret Key Length      : {stats['Secret Key Length']}")

        print(f"Measurement Accuracy   : {stats['Accuracy']} %")

        print(f"Quantum Bit Error Rate : {stats['QBER']} %")

        print(f"Security Status        : {stats['Security']}")

        print(LINE)

    # --------------------------------------------------

    def __str__(self):

        return (

            f"BB84Protocol("

            f"bits={self.num_bits}, "

            f"QBER={self.qber:.2f}%, "

            f"Accuracy={self.accuracy:.2f}%)"

        )