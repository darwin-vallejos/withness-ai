# Reference verifier — Witness Receipt Format (WRF) v1.0

import json, hashlib

with open("receipt.json", "r", encoding="utf-8") as f:
    receipt = json.load(f)

payload = receipt["payload"]
claimed_hash = receipt["receipt_hash"]

canonical = json.dumps(
    payload,
    sort_keys=True,
    separators=(",", ":"),
    ensure_ascii=False,
)

computed_hash = hashlib.sha256(
    canonical.encode("utf-8")
).hexdigest()

print("✓ VALID receipt" if computed_hash == claimed_hash else "✗ INVALID receipt")
