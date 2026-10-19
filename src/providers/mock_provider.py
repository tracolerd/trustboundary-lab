class MockProvider:
    def __init__(self, predefined_responses=None):
        self.predefined_responses = predefined_responses or {}
    def generate_response(self, payload: str) -> str:
        if payload in self.predefined_responses:
            return self.predefined_responses[payload]
        # Simulate LLM deciding to call a tool based on input
        if "delete the database" in payload.lower():
            return "CALL_TOOL: delete_database"
        return "I am a helpful assistant. I cannot fulfill malicious requests."
