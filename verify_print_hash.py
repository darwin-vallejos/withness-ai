import json, hashlib

with open("receipt.json", "r", encoding="utf-8") as f:
    receipt = json.load(f)

payload = receipt["payload"]
claimed_hash = receipt.get("receipt_hash") or receipt.get("hash")

canonical = json.dumps(
    payload,
    sort_keys=True,
    separators=(",", ":")
)

computed_hash = hashlib.sha256(
    canonical.encode("utf-8")
).hexdigest()

print("Computed:", computed_hash)
print("Claimed :", claimed_hash)
print("MATCH:", computed_hash == claimed_hash)
