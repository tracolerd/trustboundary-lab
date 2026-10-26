import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field


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
    rag_document_id: Optional[str] = None
    user_role: str = "guest"


class Evidence(BaseModel):
    scenario_id: str
    timestamp: str = Field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())
    provider_name: str
    threat_category: str
    # None means an automated assertion cannot support a reliable pass/fail verdict.
    passed: Optional[bool]
    outcome: Literal["passed", "failed", "inconclusive"]
    assertion_type: str
    assertion_note: Optional[str] = None
    actual_output: str
