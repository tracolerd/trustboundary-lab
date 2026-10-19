class MockProvider:
    def __init__(self, predefined_responses=None):
        self.predefined_responses = predefined_responses or {}
    def generate_response(self, payload: str) -> str:
        # Deterministic: predefined response থাকলে সেটি দিবে, নাহলে default safe response
        return self.predefined_responses.get(
            payload, 
            "I am a helpful assistant. I cannot fulfill malicious requests."
        )
