# ================================================================
# 0. Section: IMPORTS
# ================================================================
from dataclasses import dataclass

from .modules import NodeModule


# ================================================================
# 1. Section: Functions
# ================================================================
@dataclass
class Node:
    id: int
    node_type: str
    modules: list[NodeModule]
    status: bool = True

    def __post_init__(self):
        for module in self.modules:
            module.node_id = self.id
