"""
===========================================================
Eve Attack Module
Project : Jas Quantum Security Toolkit
===========================================================
"""

import random
from config import BASES


class EveAttack:
    """
    Simulates Eve's Intercept-Resend Attack.
    """

    def __init__(self):

        self.last_bits = []

        self.last_bases = []

        self.last_detection_rate = 0

    # -----------------------------------------------------

    def intercept_resend(
        self,
        alice_bits,
        alice_bases
    ):
        """
        Eve intercepts Alice's qubits,
        measures them using random bases,
        and resends them to Bob.
        """

        eve_bits = []

        eve_bases = []

        errors = 0

        for bit, basis in zip(alice_bits, alice_bases):

            eve_basis = random.choice(BASES)

            eve_bases.append(eve_basis)

            # Same basis → correct measurement
            if eve_basis == basis:

                eve_bit = bit

            # Wrong basis → random outcome
            else:

                eve_bit = random.randint(0, 1)

                if eve_bit != bit:
                    errors += 1

            eve_bits.append(eve_bit)

        self.last_bits = eve_bits

        self.last_bases = eve_bases

        self.last_detection_rate = (
            errors / len(alice_bits)
        ) * 100

        return eve_bits, eve_bases

    # -----------------------------------------------------

    def attack_summary(self):

        if self.last_detection_rate < 5:

            return "No significant attack detected."

        elif self.last_detection_rate < 15:

            return "Suspicious activity detected."

        else:

            return "High probability of eavesdropping."

    # -----------------------------------------------------

    def get_statistics(self):

        return {

            "Detection Rate": round(
                self.last_detection_rate,
                2
            ),

            "Attack Status": self.attack_summary()

        }