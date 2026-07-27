from typing import TypedDict

class LanggraphState(TypedDict):

    query : str
    group : str
    marks : str | None
    cgpa : int | None
    Execution_plan : list[str]