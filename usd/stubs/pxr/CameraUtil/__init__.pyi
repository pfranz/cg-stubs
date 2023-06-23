import Boost.Python
import pxr.Gf
from typing import Any, ClassVar, overload

Crop: ConformWindowPolicy
DontConform: ConformWindowPolicy
Fit: ConformWindowPolicy
MatchHorizontally: ConformWindowPolicy
MatchVertically: ConformWindowPolicy

class ConformWindowPolicy(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetValueFromName(self, name: object) -> Any: ...
    def __reduce__(self) -> Any: ...

class Framing(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    dataWindow: Any
    displayWindow: Any
    pixelAspectRatio: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: Framing) -> None: ...
    @overload
    def __init__(self, displayWindow: pxr.Gf.Range2f, dataWindow: pxr.Gf.Rect2i, pixelAspectRatio: float = ...) -> None: ...
    @overload
    def __init__(self, dataWindow: pxr.Gf.Rect2i) -> None: ...
    def ApplyToProjectionMatrix(self, projectionMatrix: pxr.Gf.Matrix4d, windowPolicy: ConformWindowPolicy) -> pxr.Gf.Matrix4d: ...
    def ComputeFilmbackWindow(self, cameraAspectRatio: float, windowPolicy: ConformWindowPolicy) -> pxr.Gf.Range2f: ...
    def IsValid(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...

class ScreenWindowParameters(Boost.Python.instance):
    def __init__(self, arg2: Camera) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def fieldOfView(self) -> float: ...
    @property
    def screenWindow(self) -> pxr.Gf.Vec4d: ...
    @property
    def zFacingViewMatrix(self) -> pxr.Gf.Matrix4d: ...

@overload
def ConformWindow(camera: pxr.Gf.Camera, policy: ConformWindowPolicy, targetAspect: float) -> None: ...
@overload
def ConformWindow(frustum: pxr.Gf.Frustum, policy: ConformWindowPolicy, targetAspect: float) -> None: ...
@overload
def ConformedWindow(window: pxr.Gf.Range2d, policy: ConformWindowPolicy, targetAspect: float) -> pxr.Gf.Range2d: ...
@overload
def ConformedWindow(window: pxr.Gf.Vec2d, policy: ConformWindowPolicy, targetAspect: float) -> pxr.Gf.Vec2d: ...
@overload
def ConformedWindow(window: pxr.Gf.Vec4d, policy: ConformWindowPolicy, targetAspect: float) -> pxr.Gf.Vec4d: ...
@overload
def ConformedWindow(window: pxr.Gf.Matrix4d, policy: ConformWindowPolicy, targetAspect: float) -> pxr.Gf.Matrix4d: ...