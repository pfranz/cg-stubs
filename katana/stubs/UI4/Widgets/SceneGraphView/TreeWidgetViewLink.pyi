# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Widgets.SceneGraphView.DataRoles as DataRoles
import NodegraphAPI as NodegraphAPI
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import QItemSelectionModel
import QT4Widgets as QT4Widgets
import QT4Widgets.SortableTreeWidget
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4.Widgets.SceneGraphView.SceneGraphLocationTranslation as SceneGraphLocationTranslation
import SceneGraphViewColumn
import UI4.Util.ScenegraphIconManager as ScenegraphIconManager
import Nodes3DAPI.ScenegraphManager as ScenegraphManager
import UI4.Widgets.SceneGraphView.Bridge
import UI4.Widgets.SceneGraphView.ItemDelegates
import Utils as Utils
import typing
from PyUtilModule.WorkingSet import WorkingSet as WorkingSet
from PyUtilModule.WorkingSetManager import WorkingSetManager as WorkingSetManager
from QT4Widgets.SortableTreeWidget import SortableTreeWidget
from UI4.Util.WorkingSets import IncludeProxyChildrenInWorkingSet as IncludeProxyChildrenInWorkingSet
from UI4.Widgets.SceneGraphView.AttributeValuePopupWidgetManager import AttributeValuePopupWidgetManager as AttributeValuePopupWidgetManager
from UI4.Widgets.SceneGraphView.ContextMenuEvent import ContextMenuEvent as ContextMenuEvent
from UI4.Widgets.SceneGraphView.HorizontalHeaderView import HorizontalHeaderView as HorizontalHeaderView
from UI4.Widgets.SceneGraphView.ItemDelegates.ParameterItemDelegate import ParameterItemDelegate as ParameterItemDelegate
from UI4.Widgets.SceneGraphView.ItemDelegates.WorkingSetItemDelegate import WorkingSetItemDelegate as WorkingSetItemDelegate
from UI4.Widgets.SceneGraphView.SceneGraphHandle import SceneGraphHandle as SceneGraphHandle
from UI4.Widgets.SceneGraphView.SceneGraphLocationTranslation import IsLocationUnderTopLevelLocation as IsLocationUnderTopLevelLocation
from UI4.Widgets.SceneGraphView.SceneGraphViewColumn import SceneGraphColumnTitle as SceneGraphColumnTitle
from UI4.Widgets.SceneGraphView.TreeWidgetItems import LocationTreeWidgetItem as LocationTreeWidgetItem
from UI4.Widgets.SceneGraphView.ViewLink import ViewLink as ViewLink
from UI4.Widgets.WorkingSetWidgets import WorkingSetExpandBranchAction as WorkingSetExpandBranchAction
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ExpandedLocationsRegistry:
    def __init__(self) -> None: ...
    def clear(self, clearCurrent: bool = ...): ...
    def getCurrentlyExpandedLocations(self) -> set[tuple]: ...
    def renameLocation(self, oldLocationPath: str, newLocationPath: str): ...
    def resetCurrentlyExpandedLocations(self): ...
    def setLocationCollapsed(self, locationPath: str, topLevelLocationPath): ...
    def setLocationExpanded(self, locationPath: str, topLevelLocationPath): ...
    def wasLocationExpanded(self, locationPath: str, topLevelLocationPath: str) -> bool: ...
    def __len__(self) -> int: ...

class TreeWidget(SortableTreeWidget):
    PaddingRight: ClassVar[int] = ...
    hideSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    showSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, contextMenuEventHandler: typing.Callable, keyPressEventHandler: typing.Callable, dragMoveEventHandler: typing.Callable, dropEventHandler: typing.Callable, aboutToDragEventHandler: typing.Callable, fontChangeEventHandler: typing.Callable, parent: Incomplete | None = ...) -> None: ...
    def _TreeWidget__on_aboutToDrag(self, draggedItems: list[LocationTreeWidgetItem], drag: PyQt5.QtGui.QDrag): ...
    def _TreeWidget__on_customContextMenuRequested(self, pos: PyQt5.QtGui.QPoint): ...
    def _TreeWidget__on_dragMoveEvent(self, event: PyQt5.QtGui.QDragMoveEvent, parentItem: LocationTreeWidgetItem, childItemIndex: int, callbackRecord: QT4Widgets.SortableTreeWidget.CallbackRecord): ...
    def _TreeWidget__on_dropEvent(self, event: PyQt5.QtGui.QDragMoveEvent, parentItem: LocationTreeWidgetItem, childItemIndex: int): ...
    def _TreeWidget__updateWidgetFromFont(self): ...
    def _getCorrespondingPointInNameColumn(self, point: PyQt5.QtCore.QPoint) -> PyQt5.QtCore.QPoint: ...
    def event(self, event: PyQt5.QtCore.QEvent) -> bool: ...
    def fontChange(self, oldFont: PyQt5.QtGui.QFont): ...
    def hideEvent(self, event: PyQt5.QtGui.QHideEvent): ...
    def indexAt(self, point: PyQt5.QtCore.QPoint) -> PyQt5.QtCore.QModelIndex: ...
    def itemDelegateForColumn(self, column): ...
    def keyPressEvent(self, keyEvent: PyQt5.QtGui.QKeyEvent): ...
    def mousePressEvent(self, mouseEvent: PyQt5.QtGui.QMouseEvent): ...
    def resizeColumnToContents(self, column: int): ...
    def selectionCommand(self, index: PyQt5.QtCore.QModelIndex, event: Incomplete | None = ...) -> QItemSelectionModel.SelectionFlags: ...
    def setItemDelegateForColumn(self, column, delegate): ...
    def showEvent(self, event: PyQt5.QtGui.QShowEvent): ...
    def visualRect(self, index: PyQt5.QtCore.QModelIndex) -> PyQt5.QtCore.QRect: ...

class TreeWidgetException(Exception):
    def __init__(self, errorMessage: str) -> None: ...

class TreeWidgetViewLink(ViewLink):
    _TreeWidgetViewLink__erroneousItemDelegateClasses: ClassVar[list] = ...
    _TreeWidgetViewLink__instanceRefs: ClassVar[list] = ...
    _TreeWidgetViewLink__stopAtLocationTypes: ClassVar[tuple] = ...
    _TreeWidgetViewLink__stopCollapsingActionIDs: ClassVar[dict] = ...
    _TreeWidgetViewLink__stopExpandingActionIDs: ClassVar[dict] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    contextName: ClassVar[str] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    def __init__(self, bridge: Bridge[UI4.Widgets.SceneGraphView.Bridge.Bridge], parent: Incomplete | None = ...) -> None: ...
    @classmethod
    def GetStopAtLocationTypes(cls) -> tuple[str, ...]: ...
    @classmethod
    def SetStopAtLocationTypes(cls, *locationTypes): ...
    @classmethod
    def _TreeWidgetViewLink__GetCapitalizedWords(cls, text: str, joiner: str = ...) -> str: ...
    def _TreeWidgetViewLink__aboutToDragEventHandler(self, draggedItems, drag): ...
    def _TreeWidgetViewLink__addChildLocationsToSelectionActionCallback(self): ...
    def _TreeWidgetViewLink__addParentLocationsToSelectionActionCallback(self): ...
    def _TreeWidgetViewLink__buildParameterItemDelegatesDictionary(self, handle, locationPath): ...
    def _TreeWidgetViewLink__collapseBranchesActionCallback(self): ...
    def _TreeWidgetViewLink__collapseBranchesToMultipleActionCallback(self): ...
    def _TreeWidgetViewLink__collapseLocationsActionCallback(self): ...
    def _TreeWidgetViewLink__contextMenuEventHandler(self, event): ...
    def _TreeWidgetViewLink__deleteLocationItem(self, locationItem, subTree): ...
    def _TreeWidgetViewLink__dragMoveEventHandler(self, dragMoveEvent, draggedItems, parentItem, childItemIndex, callbackRecord): ...
    def _TreeWidgetViewLink__dropEventHandler(self, dropEvent, droppedItems, parentItem, childItemIndex): ...
    def _TreeWidgetViewLink__expandBranchesActionCallback(self): ...
    def _TreeWidgetViewLink__expandBranchesToMultipleActionCallback(self): ...
    def _TreeWidgetViewLink__expandLocationsActionCallback(self): ...
    def _TreeWidgetViewLink__expandToAndSelectProxyChildrenCallback(self): ...
    def _TreeWidgetViewLink__fontChangeEventHandler(self): ...
    def _TreeWidgetViewLink__getAncestorLocationsOfType(self, locations, types: set[str]): ...
    def _TreeWidgetViewLink__getHandlesForSelectedItems(self, returnMinimalSet: bool = ...) -> list[None]: ...
    def _TreeWidgetViewLink__getHandlesForTopLevelItems(self) -> list[None]: ...
    def _TreeWidgetViewLink__getParentLocationItem(self, locationPath, subTree): ...
    def _TreeWidgetViewLink__getSubTreeByPath(self, topLevelLocationPath: str) -> dict: ...
    def _TreeWidgetViewLink__isItemExpandedTo(self, treeWidgetItem: PyQt5.QtWidgets.QTreeWidgetItem) -> bool: ...
    def _TreeWidgetViewLink__keyPressEventHandler(self, event): ...
    def _TreeWidgetViewLink__moveSelectionDownActionCallback(self, replaceSelection: bool = ...): ...
    def _TreeWidgetViewLink__moveSelectionUpActionCallback(self, replaceSelection: bool = ...): ...
    def _TreeWidgetViewLink__onNewScene(self, **kwargs): ...
    def _TreeWidgetViewLink__onSceneLoad(self, **kwargs): ...
    def _TreeWidgetViewLink__on_cacheManager_flush(self): ...
    def _TreeWidgetViewLink__on_event_idle_updateItemDelegates(self, eventType, eventID): ...
    def _TreeWidgetViewLink__on_sceneGraph_locationRenamed(self, eventType: str | None, eventID: object, oldLocationPath: str, newLocationPath: str, selectLocation: bool = ..., replaceSelection: bool = ...): ...
    def _TreeWidgetViewLink__on_treeWidgetHeader_sectionMoved(self, logicalIndex, oldVisualIndex, newVisualIndex): ...
    def _TreeWidgetViewLink__on_treeWidgetHeader_sectionPressed(self, logicalIndex): ...
    def _TreeWidgetViewLink__on_treeWidgetHeader_sectionResized(self, logicalIndex, oldSize, newSize): ...
    def _TreeWidgetViewLink__on_treeWidget_destroyed(self): ...
    def _TreeWidgetViewLink__on_treeWidget_hide(self): ...
    def _TreeWidgetViewLink__on_treeWidget_itemCollapsed(self, item): ...
    def _TreeWidgetViewLink__on_treeWidget_itemDoubleClicked(self, item, columnIndex): ...
    def _TreeWidgetViewLink__on_treeWidget_itemExpanded(self, item): ...
    def _TreeWidgetViewLink__on_treeWidget_itemSelectionChanged(self): ...
    def _TreeWidgetViewLink__on_treeWidget_show(self): ...
    def _TreeWidgetViewLink__recursiveShowItems(self, locationItem: LocationTreeWidgetItem): ...
    def _TreeWidgetViewLink__requestOverrideParameters(self, overrideParameters: dict): ...
    def _TreeWidgetViewLink__selectChildLocationsActionCallback(self, replaceSelection: bool = ...): ...
    def _TreeWidgetViewLink__selectLocationsByCallback(self, callback, replaceSelection: bool = ...): ...
    def _TreeWidgetViewLink__selectParentLocationsActionCallback(self, replaceSelection: bool = ...): ...
    def _TreeWidgetViewLink__showLocationItem(self, locationItem: LocationTreeWidgetItem, show: bool = ...): ...
    def _TreeWidgetViewLink__sortItemChildren(self, treeItem: LocationItem): ...
    def _TreeWidgetViewLink__updateItemChildList(self, treeItem, newItem: bool = ...): ...
    def _TreeWidgetViewLink__updateItemDelegatesForLocations(self, locationItems: list[LocationTreeWidgetItem]): ...
    def _TreeWidgetViewLink__updateLocationItems(self, locationItems: list[LocationTreeWidgetItem]): ...
    def _TreeWidgetViewLink__updateParameterItemDelegateOverrideParameters(self, parameterItemDelegates: None): ...
    def _TreeWidgetViewLink__updateTreeWidgetItem(self, treeWidgetItem, handle): ...
    def addOrUpdateLocation(self, handle, topLevelHandle, potentialChildrenChanged: bool = ...): ...
    def addOrUpdateTopLevelLocation(self, topLevelHandle, potentialChildrenChanged: bool = ...): ...
    def allowMultipleSelection(self) -> bool: ...
    def clearExpandedLocationsRegistry(self, clearCurrent: bool = ...): ...
    def collapseLocation(self, handle, topLevelHandle): ...
    def evaluateFilterRules(self, handle: Incomplete | None = ..., topLevelHandle: Incomplete | None = ...): ...
    def expandLocation(self, handle, topLevelHandle): ...
    def frozenWhenHidden(self) -> bool: ...
    def getAllLocations(self, visibleOnly: bool = ...) -> list[tuple[str, ...]]: ...
    def getChildLocations(self, locationPath, topLevelLocationPath, visibleOnly: bool = ..., allDescendants: bool = ...): ...
    def getItemDelegateTerminalOps(self): ...
    def getOverrideNodeAndParameterName(self, locationPath: str, attributeName: str) -> None: ...
    def getSelectedItems(self): ...
    def getSelectedLocations(self, sortBySceneGraphOrder: bool = ...): ...
    def getUpdateSuppressor(self): ...
    def getWidget(self): ...
    def hideAttributeValuePopupWidget(self, force: bool = ...): ...
    def isLocationExpanded(self, handle, topLevelHandle): ...
    @classmethod
    def registerKeyboardShortcuts(cls): ...
    @classmethod
    def registerKeyboardShortcutsForStopAtLocationTypes(cls): ...
    def removeLocation(self, handle, topLevelHandle, removeFromParent: bool = ...): ...
    def removeTopLevelLocation(self, topLevelHandle): ...
    def resetModel(self): ...
    def saveExpandedLocations(self): ...
    def scrollToLocation(self, handle, topLevelHandle): ...
    def selectChildLocations(self, replaceSelection: bool = ...): ...
    def selectLocations(self, locations, replaceSelection: bool = ...): ...
    def selectParentLocations(self, replaceSelection: bool = ...): ...
    def setAboutToDragCallback(self, callback): ...
    def setAllowMultipleSelection(self, allowMultipleSelection: bool): ...
    def setAttributeDataChildren(self, handle, topLevelHandle, attributeDataChildren): ...
    def setColumnTitles(self, columnTitles: list[SceneGraphColumnTitle[SceneGraphViewColumn.SceneGraphColumnTitle]]): ...
    def setColumnWidths(self, columnWidths): ...
    def setContextMenuEventCallback(self, callback): ...
    def setDragMoveEventCallback(self, callback): ...
    def setDropEventCallback(self, callback): ...
    def setExpandsOnDoubleClick(self, expandsOnDoubleClick): ...
    def setFrozenWhenHidden(self, frozenWhenHidden: bool = ...): ...
    def setKeyPressEventCallback(self, callback): ...
    def setOverrideParameterRequestCallback(self, callback): ...
    def setSelectionChangedCallback(self, callback): ...
    def setSelectionState(self, topLevelLocationPath, locationPath, selected): ...
    def showAttributeValuePopupWidget(self, index: PyQt5.QtCore.QModelIndex, itemDelegate: UI4.Widgets.SceneGraphView.ItemDelegates.ParameterItemDelegate, keepVisible: bool = ...): ...
    def sortChildrenUnderLocation(self, handle, topLevelHandle): ...
    def sortTopLevelLocations(self): ...
    def updateItemDelegates(self): ...
    def updateLocationIcons(self, handle, topLevelHandle): ...
    def updateSelection(self, selectedLocations, deselectedLocations): ...
    def updateViewport(self): ...
    def updateWidget(self): ...