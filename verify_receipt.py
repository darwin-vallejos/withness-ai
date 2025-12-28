import json
import sys
import hashlib
from src.witness.receipt_types import RECEIPT_TYPES

def canonicalize(payload: dict) -> str:
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False
    )

def sha256_hex(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

def verify_receipt(path: str):
    # Load receipt
    with open(path, "r", encoding="utf-8") as f:
        receipt = json.load(f)

    # --- Required fields ---
    receipt_type = receipt.get("type")
    if receipt_type not in RECEIPT_TYPES:
        raise ValueError(f"Unknown receipt type: {receipt_type}")

    schema_version = receipt.get("schema_version")
    if not schema_version:
        raise ValueError("Missing schema_version")

    payload = receipt.get("payload")
    if payload is None:
        raise ValueError("Missing payload")

    claimed_hash = receipt.get("hash")
    if not claimed_hash:
        raise ValueError("Missing hash")

    # --- Verification ---
    canonical = canonicalize(payload)
    computed = sha256_hex(canonical)

    print("Computed :", computed)
    print("Claimed  :", claimed_hash)
    print("MATCH    :", computed == claimed_hash)

    if computed != claimed_hash:
        raise ValueError("Hash mismatch")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify_receipt.py <receipt.json>")
        sys.exit(1)

    verify_receipt(sys.argv[1])
