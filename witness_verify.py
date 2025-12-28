#!/usr/bin/env python3
import json
import hashlib
import sys
from pathlib import Path


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
# LEGACY — DO NOT USE
# Superseded by src/witness/verify.py
# Kept for reference only


def sha256_hex(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main():
    if len(sys.argv) != 2:
        print("Usage: python witness_verify.py receipt.json")
        sys.exit(1)

    path = Path(sys.argv[1])
    receipt = json.loads(path.read_text(encoding="utf-8"))

    payload = receipt["payload"]
    claimed = receipt["receipt_hash"]

    computed = sha256_hex(canonical(payload))

    if computed == claimed:
        print("✓ Receipt VALID")
        print(f"  receipt_hash: {claimed}")
        print(f"  allowed: {payload.get('allowed')}")
        print(f"  A: {payload.get('A')}")
        sys.exit(0)

    print("✗ Receipt INVALID")
    print(f"  claimed:  {claimed}")
    print(f"  computed: {computed}")
    sys.exit(2)


if __name__ == "__main__":
    main()
