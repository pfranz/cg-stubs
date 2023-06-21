import Boost.Python
import pxr.Usd
from typing import Any, ClassVar, overload

class MaterialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, material: pxr.UsdShade.Material) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> MaterialAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def ComputeInterfaceInputConsumersMap(self, computeTransitiveConsumers: bool = ...) -> dict: ...
    def CreateDisplacementAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSurfaceAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateVolumeAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> MaterialAPI: ...
    def GetDisplacement(self, ignoreBaseMaterial: bool = ...) -> pxr.UsdShade.Shader: ...
    def GetDisplacementAttr(self) -> pxr.Usd.Attribute: ...
    def GetDisplacementOutput(self) -> pxr.UsdShade.Output: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    def GetSurface(self, ignoreBaseMaterial: bool = ...) -> pxr.UsdShade.Shader: ...
    def GetSurfaceAttr(self) -> pxr.Usd.Attribute: ...
    def GetSurfaceOutput(self) -> pxr.UsdShade.Output: ...
    def GetVolume(self, ignoreBaseMaterial: bool = ...) -> pxr.UsdShade.Shader: ...
    def GetVolumeAttr(self) -> pxr.Usd.Attribute: ...
    def GetVolumeOutput(self) -> pxr.UsdShade.Output: ...
    def SetDisplacementSource(self, arg2: pxr.Sdf.Path) -> bool: ...
    def SetSurfaceSource(self, arg2: pxr.Sdf.Path) -> bool: ...
    def SetVolumeSource(self, arg2: pxr.Sdf.Path) -> bool: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class RenderPassAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> RenderPassAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> RenderPassAPI: ...
    def GetCameraVisibilityCollectionAPI(self) -> pxr.Usd.CollectionAPI: ...
    def GetMatteCollectionAPI(self) -> pxr.Usd.CollectionAPI: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class SplineAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Usd.Prim, arg3: object, arg4: pxr.Sdf.ValueTypeName, arg5: bool) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Usd.SchemaBase, arg3: object, arg4: pxr.Sdf.ValueTypeName, arg5: bool) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> SplineAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateInterpolationAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreatePositionsAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateValuesAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> SplineAPI: ...
    def GetInterpolationAttr(self) -> pxr.Usd.Attribute: ...
    def GetPositionsAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    def GetValuesAttr(self) -> pxr.Usd.Attribute: ...
    def GetValuesTypeName(self) -> pxr.Sdf.ValueTypeName: ...
    def Validate(self) -> tuple: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class StatementsAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> StatementsAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    @overload
    def CreateRiAttribute(self, name: object, riType: object, nameSpace: object = ...) -> pxr.Usd.Attribute: ...
    @overload
    def CreateRiAttribute(self, name: object, tfType: pxr.Tf.Type, nameSpace: object = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> StatementsAPI: ...
    def GetCoordinateSystem(self) -> str: ...
    def GetModelCoordinateSystems(self) -> list: ...
    def GetModelScopedCoordinateSystems(self) -> list: ...
    def GetRiAttribute(self, name: object, nameSpace: object = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetRiAttributeName(cls, prop: Property) -> Any: ...
    @classmethod
    def GetRiAttributeNameSpace(cls, prop: Property) -> Any: ...
    def GetRiAttributes(self, nameSpace: object = ...) -> list: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    def GetScopedCoordinateSystem(self) -> str: ...
    def HasCoordinateSystem(self) -> bool: ...
    def HasScopedCoordinateSystem(self) -> bool: ...
    @classmethod
    def IsRiAttribute(cls, prop: Property) -> bool: ...
    @classmethod
    def MakeRiAttributePropertyName(cls, attrName: object) -> str: ...
    def SetCoordinateSystem(self, coordSysName: object) -> None: ...
    def SetScopedCoordinateSystem(self, coordSysName: object) -> None: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class Tokens(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def RiMaterialAPI(self) -> Any: ...
    @property
    def RiRenderPassAPI(self) -> Any: ...
    @property
    def RiSplineAPI(self) -> Any: ...
    @property
    def StatementsAPI(self) -> Any: ...
    @property
    def bspline(self) -> Any: ...
    @property
    def cameraVisibility(self) -> Any: ...
    @property
    def catmullRom(self) -> Any: ...
    @property
    def collectionCameraVisibilityIncludeRoot(self) -> Any: ...
    @property
    def constant(self) -> Any: ...
    @property
    def interpolation(self) -> Any: ...
    @property
    def linear(self) -> Any: ...
    @property
    def matte(self) -> Any: ...
    @property
    def outputsRiDisplacement(self) -> Any: ...
    @property
    def outputsRiSurface(self) -> Any: ...
    @property
    def outputsRiVolume(self) -> Any: ...
    @property
    def positions(self) -> Any: ...
    @property
    def renderContext(self) -> Any: ...
    @property
    def spline(self) -> Any: ...
    @property
    def values(self) -> Any: ...

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object) -> None: ...
    def __bool__(self) -> bool: ...
    @overload
    def __eq__(self, arg2: bool) -> Any: ...
    @overload
    def __eq__(self, arg2: bool) -> Any: ...
    def __getitem__(self, arg2: int) -> Any: ...
    @overload
    def __ne__(self, arg2: bool) -> Any: ...
    @overload
    def __ne__(self, arg2: bool) -> Any: ...
    def __reduce__(self) -> Any: ...
    @property
    def whyNot(self) -> Any: ...

def ConvertFromRManFaceVaryingLinearInterpolation(arg1: int) -> Any: ...
def ConvertFromRManInterpolateBoundary(arg1: int) -> Any: ...
def ConvertToRManFaceVaryingLinearInterpolation(arg1: object) -> int: ...
def ConvertToRManInterpolateBoundary(arg1: object) -> int: ...