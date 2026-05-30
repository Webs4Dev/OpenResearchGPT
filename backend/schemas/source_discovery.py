from pydantic import BaseModel

class SourceDiscoveryResult(BaseModel):
    recommended_sources:list[str]
    reasoning:dict[str, str] | None = None