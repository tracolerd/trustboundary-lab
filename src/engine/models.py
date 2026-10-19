from pydantic import BaseModel
from typing import Literal
class AssertionConfig(BaseModel):
    type: str
    value: str
class Scenario(BaseModel):
    id: str
    version: str
    name: str
    threat_category: Literal["direct_injection", "indirect_injection", "unauthorized_tool", "canary_leak"]
    input_payload: str
    expected_safe_behavior: str
    assertion: AssertionConfig
