# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
from Nodes3DAPI.Node3D import Node3D as Node3D

_ExtraHints: dict
_Parameter_XML: str

class Resolve(Node3D):
    def __init__(self): ...
    def addParameterHints(self, attrName, inputDict): ...