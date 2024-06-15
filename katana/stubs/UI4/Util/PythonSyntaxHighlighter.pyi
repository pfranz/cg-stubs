# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
from UI4.Util.AbstractSyntaxHighlighter import AbstractSyntaxHighlighter as AbstractSyntaxHighlighter
from typing import Set, Tuple

class PythonSyntaxHighlighter(AbstractSyntaxHighlighter):
    def __init__(self, document: PyQt5.QtWidgets.QTextEdit | PyQt5.QtGui.QTextDocument | PyQt5.QtCore.QObject, baseFormat: PyQt5.QtGui.QTextCharFormat, interpreterInputOnly: bool = ...) -> None: ...
    def _createCustomBlocks(self): ...
    def _createFormats(self): ...
    def _createPostBlockRules(self): ...
    def _createRules(self): ...
    def highlightBlock(self, text: str): ...