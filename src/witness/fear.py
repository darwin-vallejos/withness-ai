class StubFearSensor:
    def analyze(self, prompt: str):
        return {
            "fear": 0.1,
            "source": "stub-fear",
        }
