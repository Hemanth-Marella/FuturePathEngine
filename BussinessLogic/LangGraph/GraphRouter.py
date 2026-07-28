from ..LanggraphTools import LanggraphState
from langgraph.graph import END

def graph_router(state:LanggraphState):

    plan = state['Execution_plan']
    if not plan:
        return END

    print("plan is ",plan[0])
    return plan[0]