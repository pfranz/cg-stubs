# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Usd
from _typeshed import Incomplete
from typing import Callable, overload

TraceFunction: Callable
TraceMethod: Callable
TraceScope: Callable
__MFB_FULL_PACKAGE_NAME: str

class AggregateNode(Boost.Python.instance):
    expanded: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def children(self) -> list[AggregateNode]: ...
    @property
    def count(self): ...
    @property
    def exclusiveCount(self) -> int: ...
    @property
    def exclusiveTime(self): ...
    @property
    def expired(self): ...
    @property
    def id(self) -> pxr.Usd.StageCache.Id: ...
    @property
    def inclusiveTime(self) -> TimeStamp: ...
    @property
    def key(self) -> str: ...

class Collector(Boost.Python.instance):
    enabled: Incomplete
    pythonTracingEnabled: Incomplete
    def __init__(self) -> None: ...
    def BeginEvent(self, arg2: str | pxr.Ar.ResolvedPath) -> int: ...
    def BeginEventAtTime(self, arg2: str | pxr.Ar.ResolvedPath, arg3: float) -> None: ...
    def Clear(self) -> None: ...
    def EndEvent(self, arg2: str | pxr.Ar.ResolvedPath) -> int: ...
    def EndEventAtTime(self, arg2: str | pxr.Ar.ResolvedPath, arg3: float) -> None: ...
    def GetLabel(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...

class Reporter(Boost.Python.instance):
    foldRecursiveCalls: bool
    groupByFunction: bool
    shouldAdjustForOverheadAndNoise: Incomplete
    def __init__(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def ClearTree(self) -> None: ...
    def GetLabel(self) -> str: ...
    @overload
    def Report(self, arg2: str | pxr.Ar.ResolvedPath, iterationCount: int = ..., append: bool = ...) -> None: ...
    @overload
    def Report(self, iterationCount: int = ...) -> None: ...
    def ReportChromeTracing(self) -> None: ...
    def ReportChromeTracingToFile(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def ReportTimes(self) -> None: ...
    def UpdateTraceTrees(self) -> None: ...
    @classmethod
    def globalReporter(cls, *args, **kwargs): ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def aggregateTreeRoot(self) -> AggregateNode: ...
    @property
    def expired(self): ...

def GetElapsedSeconds(arg1: int, arg2: int) -> float: ...
def GetTestEventName() -> str: ...
def TestAuto() -> None: ...
def TestCreateEvents() -> None: ...
def TestNesting() -> None: ...
