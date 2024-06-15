# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import UI4.FormMaster.HintsDelegate as HintsDelegate
import Naming as Naming
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import UI4.FormMaster.Pages as Pages
import PyFnGeolibProducers
import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.ValuePolicy
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import UI4.FormMaster.States as States
import Utils as Utils
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ArrayAttributePolicy(BaseAttributePolicy):
    def __init__(self, attr, typeName, name, parent, stateSource: Incomplete | None = ...) -> None: ...
    def _ArrayAttributePolicy__getChildPolicyObject(self, index): ...
    def _equivalent(self, other): ...
    def _setAttr(self, attr): ...
    def getArrayChild(self, index): ...
    def getArraySize(self): ...
    def getChildPolicyObjects(self): ...
    def getNumChildren(self): ...
    def getType(self): ...
    def setValueState(self, state): ...

class AttributeStateSource(PyQt5.QtCore.QObject):
    _AttributeStateSource__activeStateMappings: ClassVar[dict] = ...
    _AttributeStateSource__stateMappings: ClassVar[dict] = ...
    showAttributeHistory: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    showAttributeInheritance: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, producer: PyFnGeolibProducers.GeometryProducer, path, hintDict, scopeDict, stripLen: int = ...) -> None: ...
    def _AttributeStateSource__getKey(self, key): ...
    def _transferState(self, rhs): ...
    def _triggerAttributeHistory(self, policy): ...
    def _triggerAttributeInheritance(self, policy): ...
    def getActiveAttributeEditor(self, policy): ...
    def getAttrPath(self, policy): ...
    def getAvailableStates(self, policy): ...
    def getHints(self, path): ...
    def getPath(self): ...
    def getProducer(self): ...
    def getState(self, path): ...
    def isLocked(self, policy): ...
    def setAttributeEditorsDict(self, editors): ...
    def setLocked(self, state): ...

class BaseAttributePolicy(QT4FormWidgets.ValuePolicy.AbstractValuePolicy):
    def __init__(self, attr, name, parent, stateSource: Incomplete | None = ...) -> None: ...
    def _BaseAttributePolicy__attributeHistoryTrigger(self, checked): ...
    def _BaseAttributePolicy__attributeInheritanceTrigger(self, checked): ...
    def _appendToStateMenu(self, menu: PyQt5.QtWidgets.QMenu) -> bool: ...
    def _equivalent(self, other): ...
    def _getAttr(self): ...
    def _getFullAttrName(self): ...
    def _setAttr(self, attr): ...
    def getAttrPath(self): ...
    def getAvailableStates(self): ...
    def getIndex(self): ...
    def getMimeData(self) -> PyQt5.QtCore.QMimeData: ...
    def getName(self): ...
    def getPath(self): ...
    def getScenegraphPath(self): ...
    def getStateAppearance(self, state): ...
    def getStateSource(self): ...
    def getValueAsAttr(self): ...
    def getValueState(self): ...
    def getWidgetHints(self): ...
    def isLocked(self): ...
    def shouldDisplayState(self): ...

class GroupAttributePolicy(BaseAttributePolicy):
    def __init__(self, attr, name, parent, stateSource: Incomplete | None = ...) -> None: ...
    def _GroupAttributePolicy__buildChildren(self): ...
    def _GroupAttributePolicy__getChildPageHintCallback(self, childName): ...
    def _buildChildren(self, childDict, childNames): ...
    def _setAttr(self, attr): ...
    def getChildByName(self, name): ...
    def getChildren(self): ...
    def getIgnorePages(self): ...
    def getNumChildren(self): ...
    def getType(self): ...
    def setIgnorePages(self, ignorePages): ...

class PageGroupAttributePolicy(GroupAttributePolicy):
    def __init__(self, attr, name, parent, childNames, childPages, stateSource: Incomplete | None = ..., pagePath: str = ...) -> None: ...
    def _buildChildren(self, childDict, childNames): ...
    def _getFullAttrName(self): ...
    def getValueState(self): ...
    def getWidgetHints(self): ...
    def shouldDisplayState(self): ...

class ScalarAttributePolicy(BaseAttributePolicy):
    def __init__(self, attr, index, typeName, name, parent, stateSource: Incomplete | None = ...) -> None: ...
    def _ScalarAttributePolicy__buildEmptyOverride(self): ...
    def _setAttr(self, attr): ...
    def getIndex(self): ...
    def getType(self): ...
    def getValue(self): ...
    def getValueState(self): ...
    def getWidgetHints(self): ...
    def setValue(self, value, final: bool = ...): ...
    def setValueState(self, state): ...

def CreateAttributePolicy(parentPolicy, name, attr, stateSource: Incomplete | None = ...): ...
def CreateProducerGroupPolicy(producer: PyFnGeolibProducers.GeometryProducer, attributes: Incomplete | None = ..., excludeAttributes: Incomplete | None = ..., ignorePages: bool = ..., deepExclude: Incomplete | None = ...): ...