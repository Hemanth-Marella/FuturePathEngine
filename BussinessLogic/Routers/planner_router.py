from ..Agents.planner_agent import planner_agent
from fastapi import APIRouter
from ..LanggraphTools import Langgraph_state
from pydantic import BaseModel
from ..LangGraph.GraphBuilder import graph

router = APIRouter(prefix="/planner")

class User_details(BaseModel):
    query : str
    group : str
    marks : int
    cgpa : int

@router.post("/user_details")

async def user_details(request:User_details):

    initial_state = {
        "query" : request.query,
        "group" : request.group,
        "marks" : request.marks,
        "cgpa" : request.cgpa,
        "Execution_plan":[]
    }

    result = await graph.ainvoke(initial_state)

    return result