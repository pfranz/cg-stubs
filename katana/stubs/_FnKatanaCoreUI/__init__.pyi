# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import sip

class Foundry(sip.simplewrapper):
    class UI(sip.simplewrapper):
        class FileBrowser(PyQt5.QtWidgets.QWidget):
            @classmethod
            def AddFavoriteDir(cls, *args, **kwargs): ...
            @classmethod
            def RemoveFavoriteDir(cls, *args, **kwargs): ...
            @classmethod
            def ResetFavorites(cls, *args, **kwargs): ...
            @classmethod
            def ResetNonPersistentFavorites(cls, *args, **kwargs): ...
            @classmethod
            def SetDefaultFavoritePaths(cls, *args, **kwargs): ...
            @classmethod
            def SetPreferencesPath(cls, *args, **kwargs): ...
            @classmethod
            def actionEvent(cls, *args, **kwargs): ...
            @classmethod
            def changeEvent(cls, *args, **kwargs): ...
            @classmethod
            def childEvent(cls, *args, **kwargs): ...
            @classmethod
            def closeEvent(cls, *args, **kwargs): ...
            @classmethod
            def connectNotify(cls, *args, **kwargs): ...
            @classmethod
            def contextMenuEvent(cls, *args, **kwargs): ...
            @classmethod
            def create(cls, *args, **kwargs): ...
            @classmethod
            def customEvent(cls, *args, **kwargs): ...
            @classmethod
            def destroy(cls, *args, **kwargs): ...
            @classmethod
            def disconnectNotify(cls, *args, **kwargs): ...
            @classmethod
            def dragEnterEvent(cls, *args, **kwargs): ...
            @classmethod
            def dragLeaveEvent(cls, *args, **kwargs): ...
            @classmethod
            def dragMoveEvent(cls, *args, **kwargs): ...
            @classmethod
            def dropEvent(cls, *args, **kwargs): ...
            @classmethod
            def enterEvent(cls, *args, **kwargs): ...
            @classmethod
            def event(cls, *args, **kwargs): ...
            @classmethod
            def focusInEvent(cls, *args, **kwargs): ...
            @classmethod
            def focusNextChild(cls, *args, **kwargs): ...
            @classmethod
            def focusNextPrevChild(cls, *args, **kwargs): ...
            @classmethod
            def focusOutEvent(cls, *args, **kwargs): ...
            @classmethod
            def focusPreviousChild(cls, *args, **kwargs): ...
            @classmethod
            def hideEvent(cls, *args, **kwargs): ...
            @classmethod
            def initPainter(cls, *args, **kwargs): ...
            @classmethod
            def inputMethodEvent(cls, *args, **kwargs): ...
            @classmethod
            def isSignalConnected(cls, *args, **kwargs): ...
            @classmethod
            def keyPressEvent(cls, *args, **kwargs): ...
            @classmethod
            def keyReleaseEvent(cls, *args, **kwargs): ...
            @classmethod
            def leaveEvent(cls, *args, **kwargs): ...
            @classmethod
            def metric(cls, *args, **kwargs): ...
            @classmethod
            def mouseDoubleClickEvent(cls, *args, **kwargs): ...
            @classmethod
            def mouseMoveEvent(cls, *args, **kwargs): ...
            @classmethod
            def mousePressEvent(cls, *args, **kwargs): ...
            @classmethod
            def mouseReleaseEvent(cls, *args, **kwargs): ...
            @classmethod
            def moveEvent(cls, *args, **kwargs): ...
            @classmethod
            def nativeEvent(cls, *args, **kwargs): ...
            @classmethod
            def paintEvent(cls, *args, **kwargs): ...
            @classmethod
            def receivers(cls, *args, **kwargs): ...
            @classmethod
            def refreshFavorites(cls, *args, **kwargs): ...
            @classmethod
            def resizeEvent(cls, *args, **kwargs): ...
            @classmethod
            def selectedFiles(cls, *args, **kwargs): ...
            @classmethod
            def sender(cls, *args, **kwargs): ...
            @classmethod
            def senderSignalIndex(cls, *args, **kwargs): ...
            @classmethod
            def setButtonsVisible(cls, *args, **kwargs): ...
            @classmethod
            def setDirectory(cls, *args, **kwargs): ...
            @classmethod
            def setFileSequenceEvaluator(cls, *args, **kwargs): ...
            @classmethod
            def setFilename(cls, *args, **kwargs): ...
            @classmethod
            def setFilters(cls, *args, **kwargs): ...
            @classmethod
            def setMayNotExist(cls, *args, **kwargs): ...
            @classmethod
            def setSequencesEnabled(cls, *args, **kwargs): ...
            @classmethod
            def setShowChooserTypes(cls, *args, **kwargs): ...
            @classmethod
            def sharedPainter(cls, *args, **kwargs): ...
            @classmethod
            def showEvent(cls, *args, **kwargs): ...
            @classmethod
            def tabletEvent(cls, *args, **kwargs): ...
            @classmethod
            def timerEvent(cls, *args, **kwargs): ...
            @classmethod
            def updateMicroFocus(cls, *args, **kwargs): ...
            @classmethod
            def wheelEvent(cls, *args, **kwargs): ...

        class FileInfo(sip.wrapper):
            @classmethod
            def fileName(cls, *args, **kwargs): ...
            @classmethod
            def insertSequenceFile(cls, *args, **kwargs): ...
            @classmethod
            def setEndFrame(cls, *args, **kwargs): ...
            @classmethod
            def setSequenceName(cls, *args, **kwargs): ...
            @classmethod
            def setStartFrame(cls, *args, **kwargs): ...

        class FileSequenceEvaluator(sip.wrapper):
            @classmethod
            def buildFileSequence(cls, *args, **kwargs): ...
            @classmethod
            def evaluateFiles(cls, *args, **kwargs): ...