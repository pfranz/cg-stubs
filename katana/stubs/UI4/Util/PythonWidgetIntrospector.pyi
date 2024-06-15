# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import typing
from _typeshed import Incomplete
from typing import Set, Tuple

class CaseInsensitiveStringListModel(PyQt5.QtCore.QStringListModel):
    def __init__(self, parent: Incomplete | None = ..., *args) -> None: ...
    def setStringList(self, stringList): ...

class PythonWidgetIntrospector:
    def __init__(self, parent, executionEnvironment: Incomplete | None = ...) -> None: ...
    def _PythonWidgetIntrospector__findMatchingObjects(self, tokenFragments: list[str]) -> dict: ...
    def _PythonWidgetIntrospector__getFunctionArgsString(self, module: Module, attributeName: str, explicitAttr: Incomplete | None = ...): ...
    def _PythonWidgetIntrospector__onCompleterHighlighted(self, completionText: str): ...
    def _PythonWidgetIntrospector__setCompletionPrefix(self, prefix: str): ...
    def _PythonWidgetIntrospector__setTooltipPalette(self): ...
    def addCommandWidget(self, widget): ...
    def addFunctionCallback(self, obj: object, functionName: str, enterCallback: typing.Optional[typing.Callable] = ..., exitCallback: typing.Optional[typing.Callable] = ...): ...
    def addTooltipWidget(self, widget): ...
    def endCompletion(self): ...
    def getCurrentToken(self, widget: QWidget, textCursor: Incomplete | None = ...): ...
    def getPossibleCompletions(self, token: str): ...
    def getStringToLastDelimiter(self, text: str, delimiters: list = ...) -> str: ...
    def getStringToNextDelimiter(self, text: str, delimiters: list = ...) -> str: ...
    def insertCompleterSelection(self, selectedText: str): ...
    def onKeyPressEvent(self, widget: PyQt5.QtWidgets.QWidget, keyEvent: PyQt5.QtGui.QKeyEvent) -> bool: ...
    def onKeyPressEventExit(self, widget: PyQt5.QtWidgets.QWidget, keyEvent: PyQt5.QtGui.QKeyEvent): ...
    def onMouseMove(self, widget: QWidget, mouseEvent): ...
    def removeTooltipWidget(self, widget): ...
    def setExecutionEnvironment(self, env: dict): ...
    def setUseAutoCompletionPopup(self, useAutoCompletionPopup): ...
    def updateCompletionsWithToken(self, widget: QWidget, token: str): ...