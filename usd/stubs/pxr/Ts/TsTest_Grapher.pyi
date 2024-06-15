# mypy: disable-error-code="misc, override, no-redef"

from _typeshed import Incomplete
from pxr.Ts import SData as SData

class TsTest_Grapher:
    class Diff:
        def __init__(self, time, value) -> None: ...

    class Spline:
        def __init__(self, name, data, samples, baked) -> None: ...

    class _KeyframeData:
        def __init__(self, splineData) -> None: ...
        def Draw(self, ax, color): ...

    class _StyleTable:
        class _Region:
            def __init__(self, start, openStart, isDim) -> None: ...
        def __init__(self, data, forKnots) -> None: ...
        def IsDim(self, time): ...
    def __init__(self, title, widthPx: int = ..., heightPx: int = ..., includeScales: bool = ...) -> None: ...
    def AddDiffData(self, diffs): ...
    def AddSpline(self, name, splineData, samples, baked: Incomplete | None = ...): ...
    def Display(self): ...
    @classmethod
    def Init(cls): ...
    def Write(self, filePath): ...
    def _ClearGraph(self): ...
    def _ConfigureAxes(self, axes): ...
    @staticmethod
    def _DimColor(colorStr): ...
    def _MakeGraph(self): ...