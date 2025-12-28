# src/witness/cli.py

import sys
import json
import hashlib
from datetime import datetime, timezone

from witness.engine import WitnessEngine
from witness.length_sensor import LengthSensor


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_hex(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m witness.cli <prompt>")
        sys.exit(1)

    prompt = sys.argv[1]

    # Sensors
    sensors = [LengthSensor()]

    # Run engine (ENGINE DOES NOT OWN THE HASH)
    engine = WitnessEngine()
    allowed, trust, _ = engine.evaluate(prompt, sensors)

    # === BUILD PAYLOAD ONCE (NO MUTATION AFTER THIS) ===
    payload = {
        "version": "WRF-1.0",
        "act": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "prompt": prompt,
        "allowed": bool(allowed),
        "A": round(float(trust), 6),
    }

    # === HASH EXACT PAYLOAD ===
    payload_json = canonical(payload)
    receipt_hash = sha256_hex(payload_json)

    # === BIND PAYLOAD + HASH ===
    receipt = {
        "payload": payload,
        "receipt_hash": receipt_hash,
    }

    # === WRITE EXACT CANONICAL RECEIPT ===
    with open("receipt.json", "w", encoding="utf-8", newline="\n") as f:
        f.write(canonical(receipt))

    # === OUTPUT ===
    print("=== WITNESS DECISION ===")
    print(f"Allowed: {allowed}")
    print(f"Trust (A): {payload['A']}")
    print(f"Receipt hash: {receipt_hash}")
    print("Receipt file: receipt.json")


if __name__ == "__main__":
    main()
