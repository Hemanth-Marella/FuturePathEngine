from ..LanggraphTools import Langgraph_state,group_tool

async def group_node(state:Langgraph_state.LanggraphState):

    result = await group_tool.ainvoke({
        "group":state["group"]
    })

    state['Execution_plan'].pop()

    return {
        "group_details" : result
    }