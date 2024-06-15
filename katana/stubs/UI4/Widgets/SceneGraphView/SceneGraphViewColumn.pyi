# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4.Widgets.SceneGraphView.SceneGraphViewIconManager as SceneGraphViewIconManager
import UI4
import Utils as Utils
import typing
from UI4.Widgets.SceneGraphView.ColumnDataType import ColumnDataType as ColumnDataType
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import Any, ClassVar, Set, Tuple

class BaseSceneGraphColumn:
    def __init__(self, name: str = ..., columnChangedCallback: typing.Optional[typing.Callable] = ..., parentSet: Incomplete | None = ...) -> None: ...
    def callColumnChangedCallback(self): ...
    def getColumnChangedCallback(self) -> typing.Callable | None: ...
    def getIndex(self) -> int: ...
    def getName(self) -> str: ...
    def getParentSet(self) -> SceneGraphColumnSet[SceneGraphColumnSet] | None: ...
    def getParentSetNames(self) -> list[str]: ...
    def getParentSets(self) -> list[SceneGraphColumnSet[SceneGraphColumnSet]]: ...
    def isVisible(self) -> bool: ...
    def setColumnChangedCallback(self, callback: typing.Callable | None): ...
    def setIndex(self, index: int): ...
    def setName(self, name: str): ...
    def setParentSet(self, parentSet: SceneGraphColumnSet[SceneGraphColumnSet] | None): ...
    def setVisible(self, visible: bool): ...

class SceneGraphColumn(BaseSceneGraphColumn):
    def __init__(self, columnName: str = ..., columnChangedCallback: typing.Optional[typing.Callable] = ..., parentSet: Incomplete | None = ...) -> None: ...
    def getAttributeName(self) -> str | None: ...
    def getAttributeNames(self) -> list[str]: ...
    @classmethod
    def getColorDisplayTypeName(cls) -> str: ...
    def getDataType(self) -> int: ...
    @classmethod
    def getDefaultDisplayTypeIndex(cls) -> int: ...
    @classmethod
    def getDefaultDisplayTypeName(cls) -> str: ...
    def getFixedWidth(self) -> int | None: ...
    def getLookFileMaterialAssignmentCallback(self) -> typing.Callable | None: ...
    def getMasterMaterialCallbacks(self): ...
    def getMaximumWidth(self) -> int | None: ...
    def getMinimumWidth(self) -> int | None: ...
    def getProperties(self) -> list[tuple[str, Any]]: ...
    @classmethod
    def getSupportedDisplayTypes(cls) -> list[str]: ...
    def getTemplateMaterialCallbacks(self) -> tuple[typing.Callable, ...] | None: ...
    def getTitle(self) -> SceneGraphColumnTitle[SceneGraphColumnTitle]: ...
    def getTitleClickStyle(self) -> str: ...
    def getTitleClickedCallback(self) -> typing.Callable | None: ...
    def getTitleIcon(self) -> PyQt5.QtGui.QIcon | None: ...
    def getTitleIconName(self) -> str: ...
    def getTitleStyle(self) -> str: ...
    def getTitleText(self) -> str: ...
    def getTitleToolTip(self) -> str: ...
    def getWidth(self) -> int: ...
    def isEditable(self) -> bool: ...
    def isLocationName(self) -> bool: ...
    def isTitleToggledOn(self) -> bool: ...
    def isValueComparisonEnabled(self) -> bool: ...
    def setAttributeName(self, attributeName: str, callCallback: bool = ...): ...
    def setAttributeNames(self, attributeNames: list[str]): ...
    def setDataType(self, dataType: cls): ...
    def setEditable(self, editable: bool): ...
    def setFixedWidth(self, fixedWidth: int | None): ...
    def setIsLocationName(self, isLocationName: bool): ...
    def setLookFileMaterialCallback(self, lookFileMaterialAssignmentCallback: typing.Callable | None): ...
    def setMasterMaterialCallbacks(self, masterMaterialsRequestCallback: typing.Callable, masterMaterialAssignmentCallback: typing.Callable): ...
    def setMaximumWidth(self, maximumWidth: int | None): ...
    def setMinimumWidth(self, minimumWidth: int | None): ...
    def setProperty(self, propertyName: str, propertyValue: object | None): ...
    def setTemplateMaterialCallbacks(self, templateMaterialsRequestCallback: typing.Callable | None, templateMaterialAssignmentCallback: typing.Callable | None): ...
    def setTitleClickStyle(self, titleClickStyle: str): ...
    def setTitleClickedCallback(self, callback: typing.Callable | None): ...
    def setTitleIcon(self, icon: PyQt5.QtGui.QIcon | None): ...
    def setTitleIconName(self, titleIconName: str): ...
    def setTitleStyle(self, titleStyle: str): ...
    def setTitleText(self, titleText: str): ...
    def setTitleToggledOn(self, titleToggledOn: bool): ...
    def setTitleToolTip(self, toolTip: str): ...
    def setValueComparisonEnabled(self, valueComparisonEnabled: bool): ...
    def setWidth(self, width: int): ...
    def titleClicked(self, columnTitleRect: PyQt5.QtCore.QRect): ...

class SceneGraphColumnSet(BaseSceneGraphColumn):
    _SceneGraphColumnSet__MAX_SET_NESTING_DEPTH: ClassVar[int] = ...
    def __init__(self, setName: str = ..., columnChangedCallback: typing.Optional[typing.Callable] = ..., parentSet: Incomplete | None = ..., columnPresetManager: Incomplete | None = ...) -> None: ...
    def _SceneGraphColumnSet__applyColumnSettings(self, settings: dict, setMethod: typing.Callable, depth: int = ...): ...
    @staticmethod
    def _SceneGraphColumnSet__checkRecursionDepth(depth: int): ...
    def _SceneGraphColumnSet__getChildByName(self, childName: str, childType: type, depth: int = ...) -> BaseSceneGraphColumn[BaseSceneGraphColumn] | None: ...
    def _SceneGraphColumnSet__getColumnByIndex(self, columnIndex: int, visibleOnly: bool, depth: int = ...) -> BaseSceneGraphColumn[BaseSceneGraphColumn] | None: ...
    def _SceneGraphColumnSet__getColumnSettings(self, settings: dict, getMethod: typing.Callable, depth: int = ...): ...
    def addChild(self, child: BaseSceneGraphColumn[BaseSceneGraphColumn], resetParentSet: bool = ...): ...
    def addColumn(self, columnName: str) -> SceneGraphColumn[SceneGraphColumn]: ...
    def addColumnSet(self, setName: str = ...) -> SceneGraphColumnSet[SceneGraphColumnSet]: ...
    def addKeyboardShortcut(self, shortcut: str | None | int | QKeySequence): ...
    def applyColumnVisibilitySettings(self, columnVisibilitySettings: dict): ...
    def clearChildren(self): ...
    def getAttributeName(self, columnIndex: int, visibleOnly: bool = ...) -> str | None: ...
    def getAttributeNames(self, columnIndex: int, visibleOnly: bool = ...) -> list[str]: ...
    def getChildByName(self, childName: str) -> Tuple[SceneGraphColumn[SceneGraphColumn], SceneGraphColumnSet[SceneGraphColumnSet] | None]: ...
    def getChildIndex(self, child: BaseSceneGraphColumn[BaseSceneGraphColumn]) -> int: ...
    def getColumnByIndex(self, columnIndex: int, visibleOnly: bool = ...) -> BaseSceneGraphColumn[BaseSceneGraphColumn]: ...
    def getColumnByName(self, columnName: str) -> BaseSceneGraphColumn[BaseSceneGraphColumn] | None: ...
    def getColumnCount(self, visibleOnly: bool = ...) -> int: ...
    def getColumnSetByName(self, columnSetName: str) -> SceneGraphColumnSet[SceneGraphColumnSet] | None: ...
    def getColumnVisibilitySettings(self) -> dict: ...
    def getColumns(self, visibleOnly: bool = ...) -> list[BaseSceneGraphColumn[BaseSceneGraphColumn]]: ...
    def getDataType(self, columnIndex: int, visibleOnly: bool = ...) -> int | None: ...
    def getNames(self, visibleOnly: bool = ...) -> list[str]: ...
    def getTitleText(self, columnIndex: int, visibleOnly: bool = ...) -> str | None: ...
    def getTitles(self, visibleOnly: bool = ...) -> list[SceneGraphColumnTitle[UI4.SceneGraphView.SceneGraphViewColumn.SceneGraphColumnTitle]]: ...
    def getWidth(self, columnIndex: int, visibleOnly: bool = ...) -> int | None: ...
    def getWidths(self, visibleOnly: bool = ...) -> list[int]: ...
    def isEditable(self, columnIndex: int, visibleOnly: bool = ...) -> bool | None: ...
    def isLocationNameColumn(self, columnIndex: int, visibleOnly: bool = ...) -> bool | None: ...
    def removeChild(self, child: BaseSceneGraphColumn[BaseSceneGraphColumn], resetParentSet: bool = ...): ...
    def removeKeyboardShortcut(self, shortcut: str | None | int | QKeySequence): ...
    def removeKeyboardShortcuts(self): ...
    def setChildIndex(self, child: BaseSceneGraphColumn[BaseSceneGraphColumn], index: int): ...
    def setColumnChangedCallback(self, callback: typing.Callable | None): ...

class SceneGraphColumnTitle:
    class ClickStyles:
        All: ClassVar[list] = ...
        MenuIndicator: ClassVar[str] = ...
        Toggle: ClassVar[str] = ...
    DisplayStyles: ClassVar[list] = ...
    IconOnly: ClassVar[str] = ...
    TextAndIcon: ClassVar[str] = ...
    TextOnly: ClassVar[str] = ...
    def __init__(self, text: str, iconName: str, style: str) -> None: ...
    def _SceneGraphColumnTitle__shouldShowIcon(self) -> bool: ...
    def _SceneGraphColumnTitle__shouldShowText(self) -> bool: ...
    def callClickedCallback(self, columnTitleRect: PyQt5.QtCore.QRect): ...
    def getClickStyle(self) -> str: ...
    def getClickedCallback(self) -> typing.Callable | None: ...
    def getIcon(self) -> PyQt5.QtGui.QIcon | None: ...
    def getIconName(self) -> str: ...
    def getStyle(self) -> str: ...
    def getText(self) -> str: ...
    def getToolTip(self) -> str: ...
    def isToggledOn(self) -> bool: ...
    def setClickStyle(self, clickStyle: str): ...
    def setClickedCallback(self, callback: typing.Callable | None): ...
    def setIcon(self, icon: PyQt5.QtGui.QIcon | None): ...
    def setIconName(self, iconName: str): ...
    def setStyle(self, style: str): ...
    def setText(self, text: str): ...
    def setToggledOn(self, toggledOn: bool): ...
    def setToolTip(self, toolTip: str): ...
    def setUpdateFunction(self, updateFunction: typing.Callable | None, *args): ...

def GetNonInformationalAttributeName(attributeNames: list[str]) -> str | None: ...