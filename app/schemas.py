from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, Field

Status = Literal["open", "closed", "maintenance"]

class StationCreate(BaseModel):
    code: str = Field(min_length=1)
    name: str = Field(min_length=1)
    capacity: int = Field(ge=1)
    status: Status = "open"

class StationUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    status: Status | None = None

class StationRead(StationCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)