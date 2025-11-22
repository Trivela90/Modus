from agent.modules.classes import Graph
from agent.modules.start_flow import get_entry_type
from agent.modules.text_extractor import input_expense_extraction, text_expense_extraction
from agent.modules.image_extractor import image_text_extractor
from agent.modules.information_check import finish
from langgraph.graph import StateGraph, START, END

def route_flow(state: Graph) -> str:
    flow_type = state.get("flow_type", "text")
    if flow_type == "image":
        return "image_text_extractor"
    else:
        return "input_expense_extraction"


builder = StateGraph(Graph)

builder.add_node("get_entry_type", get_entry_type)
builder.add_node("image_text_extractor", image_text_extractor)
builder.add_node("text_expense_extraction", text_expense_extraction)
builder.add_node("input_expense_extraction", input_expense_extraction)
builder.add_node("finish", finish)

builder.add_edge(START, "get_entry_type")

builder.add_conditional_edges(
    "get_entry_type",
    route_flow,
    {
        "image_text_extractor": "image_text_extractor",
        "input_expense_extraction": "input_expense_extraction",
    },
)

builder.add_edge("image_text_extractor", "text_expense_extraction")
builder.add_edge("text_expense_extraction", "finish")
builder.add_edge("input_expense_extraction", "finish")
builder.add_edge("finish", END)

graph = builder.compile()

def call_agent(input_data: dict) -> dict:
    response = graph.invoke(input_data)
    return {"expense_record": response.get("expense_record", None), "end_flag": response.get("end_flag", False), "missing_fields": response.get("missing_fields", None)}
