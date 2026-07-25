from pydantic import BaseModel

class TimeLine(BaseModel):

    skill: str
    estimated_weeks: int