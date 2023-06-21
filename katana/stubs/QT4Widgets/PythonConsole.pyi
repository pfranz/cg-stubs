# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import PyQt5.QtWidgets
import QtGui
import QtWidgets
import QT4Widgets.TextEditorUtils as TextEditorUtils
import Utils as Utils
import code
import re
from typing import Any, ClassVar
from typing import Callable
from typing import Hashable

_TAB_WIDTH: int

class FullInteractivePython(PyQt5.QtWidgets.QFrame):
    def __init__(self, *args, **kwargs): ...
    def _FullInteractivePython__buildChildren(self): ...
    def _FullInteractivePython__buildCommands(self): ...
    def _FullInteractivePython__buildMenuBar(self): ...
    def _FullInteractivePython__on_preferencesAction_triggered(self): ...
    def _FullInteractivePython__sourceFileCallback(self): ...
    def getMenuBar(self) -> QtWidgets.QMenuBar: ...
    def scriptWidget(self) -> InteractivePython: ...

class InteractivePython(PyQt5.QtWidgets.QFrame):
    class CustomInterp(code.InteractiveInterpreter):
        def __init__(self, outputwidget): ...
    class _CommandEntryWidget(PyQt5.QtWidgets.QTextEdit):
        backtabPressed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
        editingFinished: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
        enterPressed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
        returnPressed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
        tabPressed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
        def __init__(self, *args): ...
        def _CommandEntryWidget__formatDocument(self, selectionOnly: bool): ...
        def _CommandEntryWidget__formatText(self, text: str, lineIndices) -> str | None: ...
        def _CommandEntryWidget__on_pref_changed(self, eventType: str | None, eventID: Hashable, prefKey: str, prefValue: Any): ...
        def _CommandEntryWidget__returnKeyPressEvent(self, event: QtGui.QKeyEvent): ...
        def _CommandEntryWidget__toggleComment(self): ...
        def _sanitiseMimeData(self, mimeData): ...
        def contextMenuEvent(self, event: QtGui.QContextMenuEvent): ...
        def dragEnterEvent(self, event): ...
        def dragMoveEvent(self, event): ...
        def dropEvent(self, event): ...
        def focusOutEvent(self, event: QtGui.QFocusEvent): ...
        def getFormatAllAction(self) -> QtWidgets.QAction: ...
        def getFormatSelectionAction(self) -> QtWidgets.QAction: ...
        def getToggleCommentAction(self) -> QtWidgets.QAction: ...
        def insertFromMimeData(self, mimeData): ...
        def keyPressEvent(self, keyEvent): ...
        def keyReleaseEvent(self, keyEvent): ...
        def paintEvent(self, event: QtGui.QPaintEvent): ...
    class _ResultWidget(PyQt5.QtWidgets.QTextEdit):
        def __init__(self, *args): ...
        def keyPressEvent(self, keyEvent): ...
    class _ScriptStderr:
        def __init__(self, resultWidget, realstderr): ...
        def flush(self): ...
        def write(self, msg): ...
    class _ScriptStdin:
        def __init__(self, scriptWidget): ...
    class _ScriptStdout:
        def __init__(self, resultWidget): ...
        def flush(self): ...
        def write(self, msg): ...
    _InteractivePython__customFormatFunction: ClassVar[None] = ...
    _InteractivePython__identifier: ClassVar[re.Pattern] = ...
    aboutToExecuteCode: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    assMidgetCmd: ClassVar[re.Pattern] = ...
    def __init__(self, *args): ...
    def _InteractivePython__buildCommandWidget(self): ...
    def _InteractivePython__buildResultWidget(self): ...
    def _InteractivePython__echoCommand(self, commandString): ...
    def _autoComplete(self): ...
    def _enterCommand(self): ...
    def _indentCommand(self): ...
    def _unindentCommand(self): ...
    def clear(self): ...
    def commandWidget(self): ...
    def copy(self): ...
    def cut(self): ...
    @classmethod
    def getCustomFormatFunction(cls) -> Callable | None: ...
    def getEnvironment(self): ...
    def nextHist(self): ...
    def on_commandWidget_tabPressed(self): ...
    def paste(self): ...
    def prevHist(self): ...
    def printMessage(self, messageString): ...
    def resultWidget(self): ...
    def runCommand(self, commandString): ...
    @classmethod
    def setCustomFormatFunction(cls, customFormatFunction: Callable | None): ...
    def setEnvironment(self, env): ...
    def setUseAutoCompletionPopup(self, useAutoCompletionPopup): ...