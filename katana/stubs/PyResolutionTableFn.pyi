# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import Any
from typing import List

class ResolutionTable:
    def __init__(self, filename: str = ...) -> None: ...
    def addEntries(self, arg0: List[ResolutionTableEntry]) -> int: ...
    def clear(self) -> None: ...
    def createResolution(self, width: int = ..., height: int = ..., name: str = ..., groupName: str = ..., pixelAspect: float = ...) -> ResolutionTableEntry: ...
    def extractValidResolutionName(self, arg0: str) -> str: ...
    def findResolution(self, width: int = ..., height: int = ..., aspect: float = ...) -> ResolutionTableEntry: ...
    def findResolutionByName(self, arg0: str) -> ResolutionTableEntry: ...
    def getEntries(self) -> List[ResolutionTableEntry]: ...
    def getEntriesForGroup(self, group: str) -> List[ResolutionTableEntry]: ...
    def getFilename(self) -> str: ...
    def getGroups(self) -> List[str]: ...
    def getResolution(self, name: str) -> ResolutionTableEntry: ...
    def hasResolution(self, name: str) -> bool: ...
    def makeResolution(self, width: int = ..., height: int = ..., aspect: float = ..., name: str = ..., fullName: str = ..., proxyName: str = ..., groupName: str = ...) -> ResolutionTableEntry: ...

class ResolutionTableEntry:
    def __init__(self, *args, **kwargs) -> None: ...
    def aspectRatio(self) -> float: ...
    def fullname(self) -> str: ...
    def groupname(self) -> str: ...
    def name(self) -> str: ...
    def proxyname(self) -> str: ...
    def xres(self) -> int: ...
    def yres(self) -> int: ...

class ResolutionTableException(Exception): ...

def Flush() -> None: ...
def GetResolutionTable(*args, **kwargs) -> Any: ...