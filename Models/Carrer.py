from pydantic import BaseModel

class Carrer(BaseModel):

    id: str
    career_name: str
    description: str
    salary_range: str