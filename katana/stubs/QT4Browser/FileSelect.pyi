# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4Browser.BrowserSettings as BrowserSettings
import PyQt5.QtWidgets
from QT4Browser.FileBrowser import FileBrowser as FileBrowser
from typing import ClassVar

SETTINGS_GROUP_NAME: str

class FileSelect(PyQt5.QtWidgets.QDialog):
    _FileSelect__contextFileMap: ClassVar[dict] = ...
    def __init__(self, *pargs, **kargs): ...
    def _FileSelect__connect(self): ...
    def _FileSelect__doApply(self, selection): ...
    def _FileSelect__doDefault(self): ...
    def _FileSelect__setup_children(self): ...
    def _FileSelect__setup_layout(self): ...
    def bringTabToFront(self, tabName): ...
    def currentLocation(self): ...
    def done(self, code): ...
    def getFileBrowser(self): ...
    def hideEvent(self, event): ...
    def loadSettings(self): ...
    def saveSettings(self): ...
    def setCurrentLocation(self, location): ...