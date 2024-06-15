# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import KatanaResources as KatanaResources
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyXmlIO as PyXmlIO
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import Utils as Utils
import types
import typing
from PyQt5.QtCore import __lastModifiers as __lastModifiers
from UI4.App.KeyboardShortcutManager.KeyboardShortcutModel import KeyboardShortcutModel as KeyboardShortcutModel
from UI4.App.KeyboardShortcutManager.ManagedAction import ManagedAction as ManagedAction
from _typeshed import Incomplete
from typing import Set, Tuple

def BindActions(contextName: str, widget: PyQt5.QtWidgets.QWidget, callbackInstance: Incomplete | None = ...): ...
def BuildShortcutModel(): ...
def CreateAction(actionID: str, widget: PyQt5.QtWidgets.QWidget, icon: Incomplete | None = ..., text: Incomplete | None = ..., enabled: bool = ...) -> PyQt5.QtWidgets.QAction | None: ...
def GenerateActionID(name: str) -> str: ...
def GetActionID(contextName: str, actionName: str) -> str | None: ...
def GetFullActionName(actionID: str) -> str | None: ...
def GetFullKeyEventName(keyEventID: str) -> str | None: ...
def GetKeyEventID(contextName: str, keyEventName: str) -> str | None: ...
def GetKeyEventNameForShortcut(contextName: str, shortcut: str) -> str: ...
def GetShortcutForAction(actionNameOrID: str) -> str | None: ...
def GetShortcutForKeyEvent(keyEventID: str) -> str | None: ...
def HandleKeyEvent(widget: PyQt5.QtWidgets.QWidget, keyEvent: PyQt5.QtGui.QKeyEvent) -> bool: ...
def IsShortcutRegisteredForAction(actionContext: str, shortcut: str) -> bool: ...
def IsShortcutRegisteredForClass(className: str, shortcut: str) -> bool: ...
def LoadShortcuts(): ...
def RegisterAction(actionID: str, name: str, shortcut: str | None, callback: types.FunctionType | types.MethodType): ...
def RegisterActions(contextName: str, actions: dict): ...
def RegisterKeyEvent(className: str, keyEventID: str, name: str, shortcut: str, pressCallback: typing.Optional[typing.Callable] = ..., releaseCallback: typing.Optional[typing.Callable] = ..., data: Incomplete | None = ...): ...
def UnregisterAction(actionID: str): ...
def UnregisterKeyEvent(keyEventID: str): ...
def UpdateAction(managedAction: ManagedAction): ...