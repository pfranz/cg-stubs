# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes3DAPI.DynamicParameterUtil as DynamicParameterUtil
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import PyFnGeolibServices as FnGeolibServices
import LoggingAPI as LoggingAPI
import Naming as Naming
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI.TimingUtils as TimingUtils
import Nodes3DAPI.TransformUtil as TransformUtil
from Nodes3DAPI_cmodule import BuildAttrListFromDynamicParameterGroup as BuildAttrListFromDynamicParameterGroup
from _typeshed import Incomplete
from types import ModuleType
from typing import ClassVar, Type
from typing import Callable
from typing import Sequence

__attrTypeClasses: dict

class BaseOpChainInterface:
    FnAttribute: ClassVar[ModuleType] = ...
    FnGeolib: ClassVar[ModuleType] = ...
    def __init__(self, port, graphState): ...
    def addOpSystemArgs(self, gb: FnAttribute.GroupBuilder): ...
    def buildAttrFromParam(self, param: NodegraphAPI.Parameter, multisample: bool = ..., numberType: Type[FnAttribute.FloatAttribute] = ..., groupInherit: bool = ..., includeEmptyGroups: bool = ...): ...
    def buildAttrListForEnableableParameters(self, enclosingGroupParam: NodegraphAPI.Parameter): ...
    def getExclusiveToNameAndAttribute(self): ...
    def getFrameTime(self) -> float: ...
    def getGraphState(self) -> NodegraphAPI.GraphState: ...
    def getModifiedFrameTime(self) -> float: ...
    def getNumSamples(self) -> int: ...
    def getOutputPortName(self) -> str: ...
    def getShutterClose(self) -> float: ...
    def getShutterOpen(self) -> float: ...
    def getTransformAsAttribute(self) -> FnAttribute.GroupAttribute: ...

class NodeTypeBuilder:
    class OpChainInterface(BaseOpChainInterface):
        FAIL: ClassVar[int] = ...
        NO_OP: ClassVar[int] = ...
        SKIP: ClassVar[int] = ...
        def __init__(self, opChainInterface): ...
        def addInputRequest(self, inputPortName, graphState, invalidInputBehavior: int = ...): ...
        def appendOp(self, opType, opArgs: Incomplete | None = ...): ...
        def setExplicitInputRequestsEnabled(self, state): ...
        def setMinRequiredInputs(self, value): ...
    _NodeTypeBuilder__queuedPolicyRootValues: ClassVar[dict] = ...
    _NodeTypeBuilder__registeredTypes: ClassVar[dict] = ...
    def __init__(self, nodeTypeName: str): ...
    @classmethod
    def SetGenericAssignPolicyRegistrationCallback(cls, callback): ...
    def addInteractiveTransformCallbacks(self, gb: FnAttribute.GroupBuilder): ...
    def addMakeInteractiveParameter(self, gb: FnAttribute.GroupBuilder): ...
    def addTimingParameters(self, gb: FnAttribute.GroupBuilder): ...
    def addTransformParameters(self, gb: FnAttribute.GroupBuilder): ...
    def build(self): ...
    def setAddParameterHintsFnc(self, fnc: Callable): ...
    def setAppendToParametersOpChainFnc(self, fnc): ...
    def setBuildOpChainFnc(self, fnc): ...
    def setBuildParametersFnc(self, fnc: Callable): ...
    def setCustomMethod(self, fncName: str, fnc: Callable): ...
    def setGenericAssignRoots(self, paramRoot: str, attrRoot: str): ...
    def setGetInputPortAndGraphStateFnc(self, fnc: Callable): ...
    def setGetScenegraphLocationFnc(self, fnc: Callable): ...
    def setHintsForNode(self, hints: dict): ...
    def setHintsForParameter(self, paramPath: str, hints: dict): ...
    def setInputPortNames(self, names: Sequence[str]): ...
    def setIsHiddenFromMenus(self, state: bool): ...
    def setNodeTypeVersion(self, nodeTypeVersion): ...
    def setNodeTypeVersionUpdateFnc(self, nodeTypeVersion, updateFnc): ...
    def setOutputPortNames(self, names: Sequence[str]): ...
    def setParametersTemplateAttr(self, groupAttr: FnAttribute.GroupAttribute, forceArrayNames: tuple = ...): ...

class OpChainInterface(BaseOpChainInterface):
    FAIL: ClassVar[int] = ...
    NO_OP: ClassVar[int] = ...
    SKIP: ClassVar[int] = ...
    def __init__(self, opChainInterface): ...
    def addInputRequest(self, inputPortName, graphState, invalidInputBehavior: int = ...): ...
    def appendOp(self, opType, opArgs: Incomplete | None = ...): ...
    def setExplicitInputRequestsEnabled(self, state): ...
    def setMinRequiredInputs(self, value): ...

class ParametersOpChainInterface(BaseOpChainInterface):
    def __init__(self, port, graphState): ...
    def appendOp(self, opType, opArgs: Incomplete | None = ...): ...
    def getOps(self): ...

def _addParameterHints(self, attrName, inputDict): ...
def _getIncomingSceneOpAndLocation(self, port, graphState, transaction): ...
def _getOpChain(self, interface): ...
def _getScenegraphLocation(self, frameTime: Incomplete | None = ...): ...
def _getStaticAttrHintsForIncomingSceneQuery(self, attrPath): ...
def _getStaticDefaultAttrForIncomingSceneQuery(self, attrPath): ...
def _init(self): ...
def _isForcedArray(self, data, groupParam, name): ...
def _paramFromAttr(self, groupParam, groupAttr): ...