import networkx as nx
from typing import Any, Dict, Union

Num = Union[int, float]

class GraphToTreeConverter():
    def convert_limits(self, graph: nx.Graph, root: Any, #max_depth: int = None, \
        limits: Dict[str, Num] = None) -> nx.Graph:
        #is_multi = isinstance(graph, nx.MultiGraph)
        is_multi = False
        is_directed = isinstance(graph, nx.DiGraph)
        result = nx.DiGraph()
        new_name = nx.utils.generate_unique_node()
        result.add_node(new_name, name=root)
        # if max_depth is not None and limits is not None:
        #     raise ValueError("max_depth and limits are mutually exclusive")
        has_cycle = False
        try:
            nx.find_cycle(graph, source=root)
            has_cycle = True
        except:
            has_cycle = False
        if limits is None and has_cycle:
            raise RecursionError("Infinite tree on graph without limits or max_depth")
        for child_candidate in graph.neighbors(root):
            if is_multi:
                #TODO add inner cycle for every edge in multiedge
                pass
            else:
                costs = graph.get_edge_data(root, child_candidate)
                new_limits = {k: limits[k] - v for k, v in costs.items()}
                if any([v < 0 for v in new_limits.values()]):
                    continue
                else:
                    child_name = nx.utils.generate_unique_node()
                    result.add_node(child_name, name=child_candidate)
                    result.add_edge(new_name, child_name, **costs)
                    


class TreeToGraphConverter():
    pass