import json, hashlib
from datetime import datetime, timezone
from pathlib import Path

EPOCH_FILE = Path("epoch_minute.jsonl")

def _canonical(obj: dict) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def append_epoch_event(receipt_hash: str, receipt_canonical: str) -> dict:
    """
    Append-only minute log. Each event links to previous event hash.
    """
    prev = None
    if EPOCH_FILE.exists():
        last_line = EPOCH_FILE.read_text(encoding="utf-8").splitlines()[-1]
        prev = json.loads(last_line)["event_hash"]

    event = {
        "version": "BIP-2",
        "ts": datetime.now(timezone.utc).isoformat(),
        "prev_event_hash": prev,
        "receipt_hash": receipt_hash,
        "receipt_canonical_sha256": hashlib.sha256(receipt_canonical.encode("utf-8")).hexdigest(),
    }

    canon = _canonical(event)
    event_hash = hashlib.sha256(canon.encode("utf-8")).hexdigest()
    row = {"event": event, "event_canonical": canon, "event_hash": event_hash}

    with EPOCH_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

    return row
