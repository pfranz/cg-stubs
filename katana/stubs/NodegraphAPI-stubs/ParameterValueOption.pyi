# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import ClassVar

class ParameterValueOption:
    __hash__: ClassVar[None] = ...
    def __init__(self, *values): ...
    def __eq__(self, value: str) -> bool: ...
    def __ne__(self, value: str) -> bool: ...