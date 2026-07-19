"""
===========================================================
Utility Functions
Project : Jas Quantum Security Toolkit
===========================================================
"""

import random
from config import BASES


# ----------------------------------------------------------
# Random Bit Generator
# ----------------------------------------------------------

def generate_random_bits(num_bits):
    """
    Generate a random binary sequence.
    """

    return [
        random.randint(0, 1)
        for _ in range(num_bits)
    ]


# ----------------------------------------------------------
# Random Basis Generator
# ----------------------------------------------------------

def generate_random_bases(num_bits):
    """
    Generate random quantum bases.
    """

    return [
        random.choice(BASES)
        for _ in range(num_bits)
    ]


# ----------------------------------------------------------
# Basis Matching
# ----------------------------------------------------------

def compare_bases(alice_bases, bob_bases):
    """
    Compare Alice's and Bob's bases.
    """

    return [
        a == b
        for a, b in zip(
            alice_bases,
            bob_bases
        )
    ]


# ----------------------------------------------------------
# Secret Key Extraction
# ----------------------------------------------------------

def extract_secret_key(bits, matching):

    key = []

    for bit, match in zip(bits, matching):

        if match:

            key.append(bit)

    return key


# ----------------------------------------------------------
# Quantum Bit Error Rate
# ----------------------------------------------------------

def calculate_qber(alice_key, bob_key):

    if len(alice_key) == 0:
        return 0

    errors = sum(

        a != b

        for a, b in zip(
            alice_key,
            bob_key
        )

    )

    return (

        errors /

        len(alice_key)

    ) * 100


# ----------------------------------------------------------
# Accuracy
# ----------------------------------------------------------

def calculate_accuracy(alice_key, bob_key):

    if len(alice_key) == 0:
        return 0

    correct = sum(

        a == b

        for a, b in zip(
            alice_key,
            bob_key
        )

    )

    return (

        correct /

        len(alice_key)

    ) * 100


# ----------------------------------------------------------
# Pretty Printer
# ----------------------------------------------------------

def print_heading(title):

    print("\n" + "=" * 70)

    print(title.center(70))

    print("=" * 70)


def print_list(title, data):

    print(f"\n{title}")

    print(data)