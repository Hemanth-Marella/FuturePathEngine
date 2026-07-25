from pydantic import BaseModel

class student(BaseModel):

    id: str
    name: str
    age: int
    education: str
    interests: list[str]
    current_skills: list[str]
    goal: str
