"""
Witness Receipt Protocol — Receipt Types Registry
Version: v1.1.0

This file defines allowed receipt types.
Receipt meaning is determined solely by:
(type, schema_version)
"""

RECEIPT_TYPES = {
    "witness_snapshot": {
        "description": "Attests that a specific payload existed at a specific time",
        "schema_version": "1.0.0"
    }
}
