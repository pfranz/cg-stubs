import Boost.Python
from typing import Any, Callable, overload

TraceFunction: Callable
TraceMethod: Callable
TraceScope: Callable

class AggregateNode(Boost.Python.instance):
    expanded: type
    def __init__(self, *args, **kwargs) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def children(self) -> type: ...
    @property
    def count(self) -> type: ...
    @property
    def exclusiveCount(self) -> type: ...
    @property
    def exclusiveTime(self) -> type: ...
    @property
    def expired(self) -> Any: ...
    @property
    def id(self) -> type: ...
    @property
    def inclusiveTime(self) -> type: ...
    @property
    def key(self) -> type: ...

class Collector(Boost.Python.instance):
    enabled: Any
    pythonTracingEnabled: type
    def __init__(self, tupleargs, dictkwds) -> Any: ...
    def BeginEvent(self, arg2: str) -> int: ...
    def BeginEventAtTime(self, arg2: str, arg3: float) -> None: ...
    def Clear(self) -> None: ...
    def EndEvent(self, arg2: str) -> int: ...
    def EndEventAtTime(self, arg2: str, arg3: float) -> None: ...
    def GetLabel(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class Reporter(Boost.Python.instance):
    foldRecursiveCalls: type
    groupByFunction: type
    shouldAdjustForOverheadAndNoise: type
    def __init__(self, arg2: str) -> None: ...
    def ClearTree(self) -> None: ...
    def GetLabel(self) -> str: ...
    @overload
    def Report(self, iterationCount: int = ...) -> None: ...
    @overload
    def Report(self, arg2: str, iterationCount: int = ..., append: bool = ...) -> None: ...
    def ReportChromeTracing(self) -> None: ...
    def ReportChromeTracingToFile(self, arg2: str) -> None: ...
    def ReportTimes(self) -> None: ...
    def UpdateTraceTrees(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def aggregateTreeRoot(self) -> type: ...
    @property
    def expired(self) -> Any: ...
    @property
    def globalReporter(self) -> Any: ...

def GetElapsedSeconds(arg1: int, arg2: int) -> float: ...
def GetTestEventName() -> str: ...
def TestAuto() -> None: ...
def TestCreateEvents() -> None: ...
def TestNesting() -> None: ...