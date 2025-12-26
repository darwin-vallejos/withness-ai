import json
import hashlib
import sys

def verify_receipt(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        receipt = json.load(f)

    canonical = receipt["canonical"]
    stored_hash = receipt["hash"]

    computed_hash = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()

    if computed_hash == stored_hash:
        print("✅ RECEIPT VERIFIED")
        print("Hash:", stored_hash)
    else:
        print("❌ RECEIPT INVALID")
        print("Stored:  ", stored_hash)
        print("Computed:", computed_hash)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify_receipt.py receipt.json")
        sys.exit(1)

    verify_receipt(sys.argv[1])
