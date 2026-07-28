from langgraph.graph import StateGraph,START,END
from ..LanggraphTools import LanggraphState
from ..LanggraphNodes import group_node
from ..Agents import planner_agent
from .GraphRouter import graph_router
from .GraphUpdate import graph_update

graph_builder = StateGraph(LanggraphState)

# CREATE NODES FIRST
graph_builder.add_node("agent_node",planner_agent)
graph_builder.add_node("group",group_node)
graph_builder.add_node("graph_update",graph_update)

# CREATE EDGES
graph_builder.add_edge(START,"agent_node")
graph_builder.add_edge("agent_node","graph_update")

# CREATE CONDITIONAL EDGE FOR DYNAMIC TOOL SELECTION
graph_builder.add_conditional_edges(
    "graph_update",
    graph_router,
    {
        "group":"group",
        END:END,
    }
)

graph_builder.add_edge("group","graph_update")

graph = graph_builder.compile()