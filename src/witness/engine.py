# src/witness/engine.py

import hashlib
import json
from math import exp


class WitnessEngine:
    def __init__(self):
        self.alpha = 0.75
        self.beta = 1.1
        self.r = 2
        self.k = 1.0
        self.threshold = 0.8

    def evaluate(self, prompt: str, sensors: list):
        # Compute coherence
        C = self.alpha * (self.beta ** self.r)

        # Run sensors deterministically
        sensor_results = {}
        fears = []

        for sensor in sensors:
            fear = sensor.analyze(prompt)
            sensor_results[sensor.name] = fear
            fears.append(fear)

        aggregated_fear = round(sum(fears) / len(fears), 6)

        # Compute trust
        A = round(C * exp(-self.k * aggregated_fear), 6)

        allowed = A >= self.threshold

        # Canonical hash payload (NO TIMESTAMP)
        payload = {
            "version": "WRF-1.0",
            "prompt": prompt,
            "C": round(C, 6),
            "A": A,
            "allowed": allowed,
            "aggregated_fear": aggregated_fear,
            "sensors": dict(sorted(sensor_results.items()))
        }

        receipt_hash = hashlib.sha256(
            json.dumps(payload, sort_keys=True).encode()
        ).hexdigest()

        return allowed, A, receipt_hash
