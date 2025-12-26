# src/witness/length_sensor.py

class LengthSensor:
    """
    Deterministic length-based sensor.
    """

    name = "length"

    def analyze(self, prompt: str) -> float:
        length = len(prompt)

        # Deterministic fear score
        fear = min(length / 1000.0, 1.0)

        return round(fear, 6)
