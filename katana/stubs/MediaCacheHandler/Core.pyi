# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import MediaCacheHandler.DiskUtil as DiskUtil
import MediaCacheHandler.ImageUtil as ImageUtil
from _typeshed import Incomplete

def CopyElementsToMediaCache(elementList, deletionCB: Incomplete | None = ..., elementProgressCB: Incomplete | None = ..., fileProgressCB: Incomplete | None = ..., logTiming: bool = ...): ...
def DeleteElementFromMediaCache(localMediaElementDir): ...
def GetElementProportionLocal(element): ...
def GetElementsSafeForDeletion(excludeElementDirs: Incomplete | None = ..., initialLocalElements: Incomplete | None = ...): ...
def GetLocalElements(directory: Incomplete | None = ...): ...
def GetMediaCacheFreeSpaceB(): ...
def GetMediaCacheSizeB(): ...
def GetTargetMediaCacheSizeB(): ...
def IsMediaCacheDirectoryFull(directory, minFreeSpaceB: int = ...): ...
def _CopyFileToMediaCache(sourceFile, destFile, logTiming: bool = ...): ...
def _GetElementFiles(element): ...
def _GetGoodMediaCacheDirectories(minFreeSpaceB: int = ..., create: bool = ...): ...
def _GetLocalElementsInDirectory(directory): ...