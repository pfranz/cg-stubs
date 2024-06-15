# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnGeolibServices.ExpressionMath as ExpressionMath
import PyFnGeolib as FnGeolib
import UI4.Widgets.LightingToolsLayer.LightingToolsUtils as LightingToolsUtils
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import PyFnAttribute
import PyFnGeolib
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import UI4.FormMaster.KatanaFactory
import Utils as Utils
import ViewerAPI
import typing
from Callbacks.Callbacks import Callbacks as Callbacks
from UI4.Widgets.HBoxLayoutResizer import HBoxLayoutResizer
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

global_leakyWidgetFactory: LeakyWidgetFactory
kFileWidgetTypes: set
kSupportedWidgetTypes: set

class BaseColumn(PyQt5.QtWidgets.QWidget):
    kBorderRadius: ClassVar[float] = ...
    kFixedHeight: ClassVar[int] = ...
    kMinimumWidth: ClassVar[int] = ...
    def __init__(self, orientation: PyQt5.QtCore.Qt.Orientation = ..., parent: Incomplete | None = ...) -> None: ...
    def _addSpacer(self, count: int = ...): ...
    def mousePressEvent(self, event: PyQt5.QtGui.QMouseEvent): ...

class DragArea(HoverableButton):
    kPad: ClassVar[int] = ...
    def __init__(self, uiWidget: PyQt5.QtWidgets.QWidget, parent: Incomplete | None = ...) -> None: ...
    def getLastDragPosition(self) -> PyQt5.QtCore.QPointF: ...
    def mouseMoveEvent(self, mouseEvent): ...
    def mousePressEvent(self, mouseEvent): ...
    def mouseReleaseEvent(self, mouseEvent): ...

class DragAreaColumn(BaseColumn):
    toggled: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def getHandleRect(self) -> PyQt5.QtCore.QRect: ...
    def getLastDragPosition(self) -> PyQt5.QtCore.QPointF: ...
    def isChecked(self) -> DragArea: ...
    def setRowSpan(self, span: int, padding: int = ...): ...

class HoverableButton(PyQt5.QtWidgets.QPushButton):
    def __init__(self, normalPath: str, activePath: str, parent: Incomplete | None = ...) -> None: ...
    def _HoverableButton__update(self): ...
    def enterEvent(self, event): ...
    def leaveEvent(self, event): ...
    def mouseMoveEvent(self, event): ...
    def setChecked(self, checked): ...

class LabelsColumn(BaseColumn):
    def __init__(self, labels: list[str], widgetTypes: list[str], parameterPathLists, parent: Incomplete | None = ...) -> None: ...
    def _LabelsColumn__buildLabel(self, text: str, toolTip: str) -> PyQt5.QtWidgets.QLabel: ...
    def _LabelsColumn__buildToolTip(self, widgetType: str, parameterPaths: list[str]) -> str: ...
    def mousePressEvent(self, event: PyQt5.QtGui.QMouseEvent): ...

class LeakyWidgetFactory(UI4.FormMaster.KatanaFactory.ParameterWidgetFactoryClass):
    def getWidgetClass(self, policy: UI4.QT4FormWidgets.AbstractValuePolicy, hints: dict) -> type: ...

class LightingToolsUI(PyQt5.QtWidgets.QWidget):
    kDefaultPosition: ClassVar[tuple] = ...
    starredLocationsChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, viewerDelegate: ViewerAPI.ViewerDelegate, viewportWidget: ViewerAPI.ViewportWidget, parent: Incomplete | None = ...) -> None: ...
    def _LightingToolsUI__addParameterGroup(self, location: str): ...
    def _LightingToolsUI__adjustScrollerHeight(self): ...
    def _LightingToolsUI__getAttributes(self, location: str, client: PyFnGeolib.GeolibRuntime.Client | None, pendinglocationEvents: list[None], fallbackFn: Incomplete | None = ...) -> PyFnAttribute.GroupAttribute | None: ...
    def _LightingToolsUI__onLocationStarChanged(self, location: str, starred: bool): ...
    def _LightingToolsUI__onSceneAboutToLoad(self): ...
    def _LightingToolsUI__on_dragArea_toggled(self, checked: bool): ...
    def _LightingToolsUI__on_nodeLocked(self): ...
    def _LightingToolsUI__on_nodegraphChanged(self): ...
    def _LightingToolsUI__on_scenegraphLocationRenamed(self): ...
    def _LightingToolsUI__rebuildUI(self): ...
    def _LightingToolsUI__removeParameterGroup(self, location: str): ...
    def cleanup(self): ...
    def clear(self): ...
    def eventFilter(self, recipient, event): ...
    def getGafferAttributes(self, location: str) -> PyFnAttribute.GroupAttribute | None: ...
    def getViewAttributes(self, location: str) -> PyFnAttribute.GroupAttribute | None: ...
    def getVisibleLocations(self) -> set[str]: ...
    def paintEvent(self, event): ...
    def processLocationEvents(self): ...
    def rebuildUI(self): ...
    def setFocused(self, locations: typing.Iterable[str]): ...
    def setSelectedGafferNodeName(self, gafferName: str): ...
    def setSelectedLocations(self, locations): ...
    def updateGafferClient(self, gafferNodeName: str): ...
    def updateViewClient(self, viewerDelegate: ViewerAPI.ViewerDelegate, viewOp: GeolibRuntimeOp | None): ...
    def wheelEvent(self, event): ...

class ParameterColumn(BaseColumn):
    iconToggled: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    starChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, location: str, lightingToolsUI: LightingToolsUI, parent: Incomplete | None = ...) -> None: ...
    def _ParameterColumn__createLightIcon(self) -> PyQt5.QtWidgets.QWidget: ...
    def _ParameterColumn__createLocationLabel(self) -> PyQt5.QtWidgets.QLabel: ...
    def _ParameterColumn__createMissingWidget(self) -> PyQt5.QtWidgets.QLabel: ...
    def _ParameterColumn__createMuteAndSoloToolBar(self) -> PyQt5.QtWidgets.QToolBar: ...
    def _ParameterColumn__createPolicyWidget(self, policy: UI4.QT4FormWidgets.AbstractValuePolicy) -> QT4FormWidgets.FormWidget: ...
    def _ParameterColumn__createStarButton(self) -> PyQt5.QtWidgets.QPushButton: ...
    def _ParameterColumn__getLabelText(self) -> str: ...
    def _ParameterColumn__rebuildWidgets(self): ...
    def _ParameterColumn__styleWidget(self, widget: PyQt5.QtWidgets.QWidget): ...
    def getGafferNodeName(self) -> str: ...
    def getLocationLabel(self) -> RotatedLabel: ...
    def getLocationPath(self) -> str: ...
    def getParameterKeys(self): ...
    def getParameterOrdering(self) -> list[str]: ...
    def getParameterPaths(self) -> list[str]: ...
    def isParametersHashValid(self) -> bool: ...
    def mousePressEvent(self, event): ...
    def mouseReleaseEvent(self, event): ...
    def paintEvent(self, event: PyQt5.QtGui.QPaintEvent): ...
    def refreshState(self, attrs: Incomplete | None = ...): ...
    def setEnabled(self, enabled: bool): ...
    def setGafferNodeName(self, gafferName: str): ...
    def setIconChecked(self, checked: bool): ...
    def setIconEdges(self, edges: PyQt5.QtCore.Qt.Edge): ...
    def setLabelAdornment(self, adornment: Tuple[float, str | None]): ...
    def setOverrideIconName(self, iconName: str): ...
    def setParameterOrdering(self, ordering: list[str]): ...
    def setStarred(self, starred: bool): ...

class ParameterColumnGroup(BaseColumn):
    starChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, location: str, lightingToolsUI: LightingToolsUI, parent: Incomplete | None = ...) -> None: ...
    def _ParameterColumnGroup__buildRelatedColumns(self) -> list[ParameterColumn]: ...
    def _ParameterColumnGroup__createColumn(self, location: str) -> ParameterColumn: ...
    def _ParameterColumnGroup__getPrincipalColumn(self) -> ParameterColumn: ...
    def _ParameterColumnGroup__getRelatedLightPaths(self) -> list | str: ...
    def _ParameterColumnGroup__onSelectedLocationColumnToggled(self, *_args): ...
    def _ParameterColumnGroup__onTemplateMaterialColumnToggled(self, *_args): ...
    def _ParameterColumnGroup__updateColumnVisibility(self): ...
    def _ParameterColumnGroup__updateLayout(self): ...
    def _ParameterColumnGroup__updateTemplateMaterialCount(self): ...
    def _ParameterColumnGroup__updateWidth(self): ...
    def getColumns(self) -> typing.Iterator[ParameterColumn]: ...
    def getExpandedState(self) -> None: ...
    def getGafferNodeName(self) -> str: ...
    def getNumberOfVisibleColumns(self): ...
    def getParameterKeys(self): ...
    def getParameterPaths(self) -> list[str]: ...
    def getTemplateMaterialPath(self) -> str | None: ...
    def isParametersHashValid(self) -> bool: ...
    def mousePressEvent(self, event): ...
    def refreshRelatedLocations(self): ...
    def refreshState(self, attrsDict: Incomplete | None = ...): ...
    def setExpandedState(self, templateMaterialVisible: bool, relatedVisible: bool): ...
    def setGafferNodeName(self, gafferName: str): ...
    def setParameterOrdering(self, ordering: list[str]): ...
    def setStarred(self, starredLocations: set[str]): ...
    def setTemplateMaterialPath(self, templateMaterialPath: str | None): ...

class ParameterResizer(HBoxLayoutResizer):
    kMaximumWidth: ClassVar[int] = ...
    kMinimumWidth: ClassVar[int] = ...
    def __init__(self, targetWidget) -> None: ...
    def hasBeenManuallyResized(self) -> bool: ...
    def mouseDoubleClickEvent(self, event): ...
    def mouseMoveEvent(self, event): ...

class RotatedLabel(PyQt5.QtWidgets.QLabel):
    def __init__(self, text: str, angle: float) -> None: ...
    def _RotatedLabel__getBoxSize(self, fontMetrics: PyQt5.QtGui.QFontMetrics) -> None: ...
    def draw(self, paintDevice: PyQt5.QtGui.QPaintDevice): ...
    def paintEvent(self, event: PyQt5.QtGui.QPaintEvent): ...
    def setFocused(self, focused: bool): ...
    def setHighlighted(self, highlighted: bool): ...
    def sizeHint(self) -> PyQt5.QtCore.QSize: ...

class RoundedCap(PyQt5.QtWidgets.QFrame):
    def __init__(self, edge: PyQt5.QtCore.Qt.Edge, parent: Incomplete | None = ...) -> None: ...

class RoundedCapsColumn(BaseColumn):
    def __init__(self, edge: PyQt5.QtCore.Qt.Edge, numRows: int, parent: Incomplete | None = ...) -> None: ...

def ClearLayout(layout: PyQt5.QtWidgets.QLayout): ...
def ConvertParameterPathToTitleCaseLabel(text: str) -> str: ...
def DefineParameterWidgetType(policy: QT4FormWidgets.AbstractValuePolicy) -> QT4FormWidgets.FormWidget: ...
def GetAllLightPaths(worldAttrs: PyFnAttribute.GroupAttribute) -> list | str: ...
def GetWidgetType(policy: QT4FormWidgets.AbstractValuePolicy) -> str | None: ...
def IsSupportedWidgetType(widgetType: str | None) -> bool: ...