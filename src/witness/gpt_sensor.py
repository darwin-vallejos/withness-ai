from witness.sensor_contract import SensorResult

def analyze_prompt(prompt: str) -> SensorResult:
    text = prompt.lower()

    fear = 0.25 if "danger" in text else 0.1

    return SensorResult(
        fear=fear,
        confidence=0.9,
        source="stub",
        features={
            "keyword_danger": float("danger" in text)
        }
    )
