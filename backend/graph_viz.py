"""Build an interactive knowledge graph visualization from correlation data."""

import tempfile
from pathlib import Path

import networkx as nx
from pyvis.network import Network

GROUP_COLORS = {
    "person": "#4fc3f7",
    "location": "#81c784",
    "platform": "#ffb74d",
    "behavior": "#e57373",
}


def build_graph_html(correlations: dict) -> str:
    """Convert correlation nodes/edges into a PyVis HTML visualization."""
    graph = nx.Graph()

    for node in correlations.get("nodes", []):
        graph.add_node(
            node["id"],
            label=node["label"],
            size=node.get("size", 10),
            group=node.get("group", "default"),
        )

    for edge in correlations.get("edges", []):
        graph.add_edge(
            edge["source"],
            edge["target"],
            label=edge.get("label", ""),
            weight=edge.get("weight", 1),
        )

    net = Network(
        height="420px",
        width="100%",
        bgcolor="#0e1117",
        font_color="#fafafa",
        directed=False,
    )
    net.from_nx(graph)

    for node in net.nodes:
        group = node.get("group", "default")
        color = GROUP_COLORS.get(group, "#90a4ae")
        node["color"] = color
        node["font"] = {"size": 14, "face": "Segoe UI"}

    for edge in net.edges:
        edge["color"] = "#546e7a"
        edge["width"] = 1.5

    net.set_options(
        """
        {
          "physics": {
            "enabled": true,
            "barnesHut": {
              "gravitationalConstant": -8000,
              "springLength": 160
            }
          },
          "interaction": {
            "hover": true,
            "tooltipDelay": 100
          }
        }
        """
    )

    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False) as tmp:
        net.save_graph(tmp.name)
        return Path(tmp.name).read_text(encoding="utf-8")
