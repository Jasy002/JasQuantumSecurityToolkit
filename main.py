"""
===========================================================
Main Program
Project : Jas Quantum Security Toolkit
Author  : Jasmine
===========================================================
"""

from config import *
from bb84 import BB84Protocol
from eve import EveAttack
from visualization import Visualizer


def main():

    print(LINE)
    print(PROJECT_NAME.center(70))
    print(LINE)

    # --------------------------------------------------
    # Create Eve
    # --------------------------------------------------

    eve = EveAttack()

    # --------------------------------------------------
    # Run BB84 Protocol
    # --------------------------------------------------

    bb84 = BB84Protocol(NUM_BITS)

    bb84.run_protocol(eve)

    # --------------------------------------------------
    # Display Protocol Data
    # --------------------------------------------------

    bb84.display_data()

    bb84.print_report()

    # --------------------------------------------------
    # Eve Report
    # --------------------------------------------------

    eve_stats = eve.get_statistics()

    print("\n" + LINE)

    print("EVE ATTACK REPORT".center(70))

    print(LINE)

    print("\nEve Bases")

    print(eve.last_bases)

    print("\nEve Measured Bits")

    print(eve.last_bits)

    print()

    print(f"Detection Rate : {eve_stats['Detection Rate']} %")

    print(f"Attack Status  : {eve_stats['Attack Status']}")

    # --------------------------------------------------
    # Generate Graphs
    # --------------------------------------------------

    visualizer = Visualizer()

    visualizer.generate_all_graphs(
        bb84,
        eve
    )

    print("\n" + LINE)

    print("SIMULATION COMPLETED SUCCESSFULLY".center(70))

    print(LINE)


if __name__ == "__main__":
    main()