from langgraph.graph import StateGraph, START, END

from core.state import ThumbnailState
from nodes.search import web_search_node
from nodes.writer import prompt_writer_node
from nodes.generator import generator_node
from nodes.critic import critic_node
from nodes.router import should_continue
from nodes.compiler import compiler_node
from nodes.saver import saver_node


def build_graph():
    workflow = StateGraph(ThumbnailState)
    workflow.add_node("web_search", web_search_node)
    workflow.add_node("prompt_writer", prompt_writer_node)
    workflow.add_node("generator", generator_node)
    workflow.add_node("critic", critic_node)
    workflow.add_node("compiler", compiler_node)
    workflow.add_node("saver", saver_node)
    workflow.add_edge(START, "web_search")
    workflow.add_edge("web_search", "prompt_writer")
    workflow.add_edge("prompt_writer", "generator")
    workflow.add_edge("generator", "critic")

    workflow.add_conditional_edges(
        "critic",
        should_continue,
        {
            "continue": "prompt_writer",
            "finish": "compiler"
        }
    )

    workflow.add_edge("compiler", "saver")
    workflow.add_edge("saver", END)

    return workflow.compile()