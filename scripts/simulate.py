# scripts/simulate.py

from witness.engine import WitnessEngine


def run_prompt(prompt: str):
    engine = WitnessEngine()

    # Fixed coherence for demo
    C = 1.25

    allowed, C, A, sensors, receipt = engine.step(C, prompt)

    print("\n=== WITNESS DECISION ===")
    print(f"Allowed: {allowed}")
    print(f"Coherence (C): {C}")
    print(f"Trust (A): {A}")

    for i, s in enumerate(sensors, start=1):
        print(f"Sensor {i}: {s.source}, fear={s.fear}")

    print(f"Aggregated fear: {sum(s.fear for s in sensors) / len(sensors)}")
    print(f"Receipt hash: {receipt}")


if __name__ == "__main__":
    prompt = input("PROMPT: ")
    run_prompt(prompt)
