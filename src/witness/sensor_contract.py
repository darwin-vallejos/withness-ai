from dataclasses import dataclass
from typing import Optional, Dict, Any


SENSOR_CONTRACT_VERSION = "1.0.0"


@dataclass(frozen=True)
class SensorResult:
    fear: float
    source: str
    meta: Optional[Dict[str, Any]] = None


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


def aggregate(results: list[SensorResult]) -> float:
    if not results:
        return 0.0
    return sum(r.fear for r in results) / len(results)
