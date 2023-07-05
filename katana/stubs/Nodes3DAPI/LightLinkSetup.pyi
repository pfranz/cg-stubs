# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
from Nodes3DAPI.LightLinkConstants import InitialState as InitialState
from Nodes3DAPI.Node3D import Node3D as Node3D

_ExtraHints: dict
_Parameter_XML: str

class LightLinkSetupNode3D(Node3D):
    def __init__(self): ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...