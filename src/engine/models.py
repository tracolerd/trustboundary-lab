import datetime
from pydantic import BaseModel, Field
from typing import Literal, Optional
class AssertionConfig(BaseModel):
    type: Literal["exact_match_exclusion", "regex_match", "heuristic_safe"]
    value: Optional[str] = None
class Scenario(BaseModel):
    id: str
    version: str
    name: str
    threat_category: Literal["direct_injection", "indirect_injection", "unauthorized_tool", "canary_leak"]
    input_payload: str
    expected_safe_behavior: str
    assertion: AssertionConfig
class Evidence(BaseModel):
    scenario_id: str
    timestamp: str = Field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())
    provider_name: str
    threat_category: str
    passed: bool
    actual_output: str
    assertion_type: str
