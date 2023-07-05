# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"


class ResolutionTable:
    def __init__(self, filename: str = ...) -> None: ...
    def addEntries(self, arg0: list[ResolutionTableEntry]) -> int: ...
    def clear(self) -> None: ...
    def createResolution(self, width: int = ..., height: int = ..., name: str = ..., groupName: str = ..., pixelAspect: float = ...) -> ResolutionTableEntry: ...
    def extractValidResolutionName(self, arg0: str) -> str: ...
    def findResolution(self, width: int = ..., height: int = ..., aspect: float = ...) -> ResolutionTableEntry: ...
    def findResolutionByName(self, arg0: str) -> ResolutionTableEntry: ...
    def getEntries(self) -> list[ResolutionTableEntry]: ...
    def getEntriesForGroup(self, group: str) -> list[ResolutionTableEntry]: ...
    def getFilename(self) -> str: ...
    def getGroups(self) -> list[str]: ...
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
def GetResolutionTable(*args, **kwargs): ...