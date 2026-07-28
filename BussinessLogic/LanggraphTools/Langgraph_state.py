from typing import TypedDict

class LanggraphState(TypedDict):

    query : str
    group : str
    group_details : dict
    carrer : str
    carrer_details : dict
    marks : str | None
    cgpa : int | None
    eligibility : dict
    Execution_plan : list[str]