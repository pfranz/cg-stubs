# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
from typing import ClassVar

_moduleInitialized: bool
_platformKind: int

class PlatformKind:
    LINUX: ClassVar[int] = ...
    MAC: ClassVar[int] = ...
    UNKNOWN: ClassVar[int] = ...
    WINDOWS: ClassVar[int] = ...

def GetKatanaTempfile(prefix: str, suffix: str, maxInt: int = ...) -> str: ...
def GetPlatformKind() -> PlatformKind: ...