from pydantic import BaseModel

class Roadmap(BaseModel):
    career_id: str
    step_number: int
    skill: str | None
    prerequisite: list[str]