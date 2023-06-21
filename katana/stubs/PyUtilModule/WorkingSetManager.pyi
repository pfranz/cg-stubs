# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import Utils as Utils
from PyUtilModule.WorkingSet import WorkingSet as WorkingSet
from _typeshed import Incomplete
from typing import ClassVar

systemWorkingSetName: str

class WorkingSetManager:
    LiveRenderUpdatesWorkingSetName: ClassVar[str] = ...
    RenderWorkingSetName: ClassVar[str] = ...
    ViewerVisibilityWorkingSetName: ClassVar[str] = ...
    _SystemWorkingSetNames: ClassVar[tuple] = ...
    _WorkingSetManager__ClearOnSceneChange: ClassVar[set] = ...
    _WorkingSetManager__OnSceneChangeCallbackRegistered: ClassVar[bool] = ...
    _WorkingSetManager__PersistentWorkingSetNames: ClassVar[set] = ...
    _WorkingSetManager__UserOnSceneChangeCallback: ClassVar[None] = ...
    _WorkingSetManager__WorkingSets: ClassVar[dict] = ...
    @classmethod
    def _WorkingSetManager__onSceneLoadOrNewScene(cls, **kwargs): ...
    @classmethod
    def clearOnSceneChangeCallback(cls): ...
    @classmethod
    def clearWorkingSetOnSceneChange(cls, workingSetName: str): ...
    def deleteWorkingSet(self, name: str): ...
    def getOrCreateWorkingSet(self, name: str, sender: Incomplete | None = ...) -> WorkingSet: ...
    def getPersistentWorkingSetNames(self) -> list[str]: ...
    def getWorkingSetNames(self) -> list[str]: ...
    def isWorkingSetPersistent(self, name: str) -> bool: ...
    @classmethod
    def setOnSceneChangeCallback(cls, callback: Callable): ...
    def setOpArgs(self, op: FnGeolibOp, opArgName: str, workingSetName: str, txn: Incomplete | None = ..., opType: Incomplete | None = ..., opArgs: Incomplete | None = ..., updateOnWorkingSetChanges: bool = ...): ...
    def setWorkingSetPersistent(self, name: str, persistent: bool = ...): ...