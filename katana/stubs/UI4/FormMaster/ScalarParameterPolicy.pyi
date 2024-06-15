# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import UI4.FormMaster.ParameterCurveEditSet as ParameterCurveEditSet
import UI4.FormMaster.ParameterPolicy as ParameterPolicy
import PyFCurve as PyFCurve
import QT4FormWidgets as QT4FormWidgets
import Utils as Utils
from UI4.FormMaster.BaseParameterPolicy import BaseParameterPolicy as BaseParameterPolicy
from typing import Set, Tuple

ALLOWED_TYPES: tuple

class ScalarParameterPolicy(BaseParameterPolicy):
    def __init__(self, param, parent) -> None: ...
    def _ScalarParameterPolicy__checkForUpdate(self, final): ...
    def _ScalarParameterPolicy__getFullValue(self, param): ...
    def _ScalarParameterPolicy__isConstant(self): ...
    def _freeze(self): ...
    def _getFullValue(self, param: NodegraphAPI.Parameter) -> Tuple[None, str, bool]: ...
    def _handleParamChanged(self, args): ...
    def _handleParamFinalized(self, args): ...
    def _handleTimeChanged(self, final): ...
    def _hintsChanged(self): ...
    def _thaw(self): ...
    def bakeCurve(self, keys): ...
    def canHaveCurve(self): ...
    def getCurve(self): ...
    def getCurveAutoKey(self): ...
    def getCurveKey(self): ...
    def getValue(self): ...
    def getValueAsString(self): ...
    def hasFloatingCurve(self): ...
    def isCurveEnabled(self): ...
    def isCurveViewed(self): ...
    def loadCurveFromFile(self, path, curvename: str = ...): ...
    def setCurve(self, curve): ...
    def setCurveAutoKey(self, autoKey): ...
    def setCurveEnabled(self, state): ...
    def setCurveKey(self, state, final: bool = ...): ...
    def setCurveViewed(self, state): ...
    def setValue(self, value, final: bool = ...): ...
    def setValueFromString(self, strValue, final: bool = ...): ...
    def writeCurveToFile(self, path): ...