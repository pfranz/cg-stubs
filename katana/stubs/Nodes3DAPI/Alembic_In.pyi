# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import PyFnAttribute as FnAttribute
import PyFnGeolibServices as FnGeolibServices
import NodegraphAPI as NodegraphAPI
from Nodes3DAPI.Node3D import Node3D as Node3D
from Nodes3DAPI.TimingUtils import GetModifiedFrameTime as GetModifiedFrameTime, GetTimingParameterHints as GetTimingParameterHints, GetTimingParameterXML as GetTimingParameterXML

_ExtraHints: dict
_Parameter_XML: str

class Alembic_In(Node3D):
    def __init__(self): ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...