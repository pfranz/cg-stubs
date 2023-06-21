import Boost.Python
import pxr.UsdAppUtils.cameraArgs as cameraArgs
import pxr.UsdAppUtils.colorArgs as colorArgs
import pxr.UsdAppUtils.complexityArgs as complexityArgs
import pxr.UsdAppUtils.framesArgs as framesArgs
import pxr.Usd
import pxr.UsdAppUtils.rendererArgs as rendererArgs
from typing import Any, ClassVar, overload

class FrameRecorder(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: bool) -> None: ...
    def GetCurrentRendererId(self) -> Any: ...
    def Record(self, stage: pxr.Usd.Stage, usdCamera: Camera, timeCode: TimeCode, outputImagePath: object) -> bool: ...
    def SetColorCorrectionMode(self, arg2: object) -> None: ...
    def SetComplexity(self, arg2: float) -> None: ...
    def SetImageWidth(self, arg2: int) -> None: ...
    def SetIncludedPurposes(self, purposes: object) -> None: ...
    def SetRendererPlugin(self, arg2: object) -> bool: ...
    def __reduce__(self) -> Any: ...

def GetCameraAtPath(stage: pxr.Usd.Stage, cameraPath: pxr.Sdf.Path) -> Camera: ...