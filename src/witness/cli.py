# src/witness/cli.py

import sys
from witness.engine import WitnessEngine
from witness.length_sensor import LengthSensor


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m witness.cli <prompt>")
        sys.exit(1)

    prompt = sys.argv[1]

    # Instantiate sensors
    sensors = [LengthSensor()]

    # Run engine
    engine = WitnessEngine()
    allowed, trust, receipt_hash = engine.evaluate(prompt, sensors)

    # Output
    print("=== WITNESS DECISION ===")
    print(f"Allowed: {allowed}")
    print(f"Trust (A): {trust}")
    print(f"Receipt hash: {receipt_hash}")


if __name__ == "__main__":
    main()
