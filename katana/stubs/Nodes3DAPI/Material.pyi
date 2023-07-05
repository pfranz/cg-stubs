# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import Nodes3DAPI.DynamicParameterUtil as DynamicParameterUtil
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import PyFnGeolibServices as FnGeolibServices
import Nodes3DAPI.IncomingSceneOpDelegates as IncomingSceneOpDelegates
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI_cmodule as Nodes3DAPI_cmodule
import PyFnAttribute
import PyXmlIO as PyXmlIO
import Utils as Utils
from Nodes3DAPI.Node3D import Node3D as Node3D
from Nodes3DAPI_cmodule import GetLeafAttrPairs as GetLeafAttrPairs
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import ClassVar

_ExtraHints: dict
_Parameter_XML: str

class Material(Node3D):
    _Material__incomingCookKey: ClassVar[str] = ...
    _Material__topLevelStaticHints: ClassVar[dict] = ...
    def __init__(self): ...
    def _Material__addDeepParam(self, parent, path, value: Incomplete | None = ...): ...
    def _Material__addShaderPair(self, parent, prefix, isCoshader: bool = ...): ...
    def _Material__checkDynamicParametersInternal(self, universalAttr, updateLastValue: bool = ...): ...
    def _Material__deleteDeepParam(self, path, deleteEmptyParentGroups: bool = ...): ...
    def _Material__findUniqueCoshaderName(self, renderer): ...
    def _Material__getCoshaderNames(self, renderer): ...
    def _Material__getMaterialAttrList(self, graphState): ...
    def _Material__getShaderTypeParameters(self): ...
    def _Material__isNetworkMaterial(self): ...
    def _Material__lastValueDiffers(self, param, currentValue, sourceTime, updateLastValue: bool = ...): ...
    def _Material__updateShaderTypeParamsWithAttr(self, paramsParam, paramsAttr, dynamicArrayAttrPaths, attrPrefix): ...
    def _cookAndWaitToUpdateParameters(self, updateLastValue: bool = ...): ...
    def _getIncomingSceneOpAndLocation(self, port, graphState, transaction): ...
    def _getOpChain(self, interface): ...
    def _getStaticAttrHintsForIncomingSceneQuery(self, attrPath): ...
    def _getUpdateParametersSupportedKeywords(self): ...
    def _updateParameters(self, groupAttr, force: bool = ..., defaultAttr: Incomplete | None = ..., updateLastValue: bool = ...): ...
    def addAttributeEntry(self, attr: PyFnAttribute.Attribute, path: str, hints: dict): ...
    def addCoshader(self, renderer, coshaderName): ...
    def addParameterHints(self, attrName, inputDict): ...
    def addShaderType(self, shaderType): ...
    def canOverride(self, attrName): ...
    def checkDynamicParameters(self, *args, **kwds): ...
    def clearParamHistory(self): ...
    def deleteAttributeEntry(self, index: int): ...
    def findOverrideParameter(self, path, attrName, time, **kwargs): ...
    def getAttributeEntries(self) -> NodegraphAPI.Parameter: ...
    def getInfoString(self): ...
    def getScenegraphLocation(self, sourceTime: int = ...): ...
    def initializeFromMaterialAttr(self, materialAttr): ...
    def isResetPossible(self): ...
    def removeAllShaders(self): ...
    def removeCoshader(self, coshaderName, renderer): ...
    def removeShaderAtPath(self, shaderParameterPath: str): ...
    def removeShaderType(self, shaderType, isCoshader: bool = ...): ...
    def renameCoshader(self, path, newName): ...
    def reorderAttributeEntries(self, oldPos: int, oldPosCount: int, newPos: int, newPosCount: int): ...
    def reorderAttributeEntry(self, oldPos: int, newPos: int): ...
    def setOverride(self, path, attrName, time, attrData, attrType: Incomplete | None = ..., attrTupleSize: Incomplete | None = ..., makeEmptyGroup: bool = ..., groupInherit: bool = ..., index: Incomplete | None = ...): ...
    def setShader(self, shaderType, shaderName): ...
    def setShaderParam(self, shaderType, paramName, newValue): ...

class ShaderPathComponents:
    class Role:
        PARAMETER: ClassVar[int] = ...
        PARAMETER_GROUP: ClassVar[int] = ...
        SHADER_NAME: ClassVar[int] = ...
    PATH_REGEX: ClassVar[str] = ...
    def __init__(self, canonicalPath, role, shaderType, parameterName, isCoshader): ...
    def _ShaderPathComponents__getPathForRole(self, role): ...
    @classmethod
    def _ShaderPathComponents__getPeerPathForPath(cls, path, pathRole, isCoshader): ...
    @classmethod
    def create(cls, path: str) -> ShaderPathComponents | None: ...
    def getCanonicalPath(self): ...
    def getParameterGroupPath(self): ...
    def getParameterName(self) -> str | None: ...
    def getRole(self): ...
    def getShaderNamePath(self): ...
    def getShaderType(self): ...
    def isCoshader(self): ...