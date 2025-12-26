import json
import sys
from witness.hashing import compute_hash

def verify_receipt(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        receipt = json.load(f)

    if "hash" not in receipt or "payload" not in receipt:
        print("Invalid receipt format")
        sys.exit(1)

    expected = receipt["hash"]
    computed = compute_hash(receipt["payload"])

    if expected == computed:
        print("✅ Receipt is valid")
        print(f"Hash: {expected}")
    else:
        print("❌ Receipt is INVALID")
        print(f"Expected: {expected}")
        print(f"Computed: {computed}")
        sys.exit(2)
