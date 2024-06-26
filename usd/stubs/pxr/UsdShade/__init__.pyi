# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Ndr
import pxr.Sdf
import pxr.Sdr
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
import pxr.UsdSkel
import pxr.Vt
import typing
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class AttributeType(Boost.Python.enum):
    Input: ClassVar[AttributeType] = ...
    Invalid: ClassVar[AttributeType] = ...
    Output: ClassVar[AttributeType] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class ConnectableAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def CanConnect(output: Output, source: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output = ...) -> bool: ...
    @overload
    @staticmethod
    def CanConnect(input: Input, source: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    @staticmethod
    def ClearSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    @staticmethod
    def ClearSources(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    @overload
    @staticmethod
    def ConnectToSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, source: ConnectableAPI, sourceName: object, sourceType: AttributeType = ..., typeName: pxr.Sdf.ValueTypeName = ...) -> bool: ...
    @overload
    @staticmethod
    def ConnectToSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, source: ConnectionSourceInfo, mod: ConnectionModification = ...) -> bool: ...
    @overload
    @staticmethod
    def ConnectToSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, sourcePath: pxr.Sdf.Path | str) -> bool: ...
    @overload
    @staticmethod
    def ConnectToSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, output: Output) -> bool: ...
    @overload
    @staticmethod
    def ConnectToSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, input: Input) -> bool: ...
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Input: ...
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Output: ...
    @staticmethod
    def DisconnectSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, sourceAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output = ...) -> bool: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> ConnectableAPI: ...
    @staticmethod
    def GetConnectedSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> Any: ...
    @staticmethod
    def GetConnectedSources(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> Any: ...
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> Input: ...
    def GetInputs(self, onlyAuthored: bool = ...) -> list[Input]: ...
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> Output: ...
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[Output]: ...
    @staticmethod
    def GetRawConnectedSourcePaths(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> list: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def HasConnectableAPI(schemaType: pxr.Tf.Type) -> bool: ...
    @staticmethod
    def HasConnectedSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    def IsContainer(self) -> bool: ...
    @staticmethod
    def IsSourceConnectionFromBaseMaterial(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    def RequiresEncapsulation(self) -> bool: ...
    @staticmethod
    def SetConnectedSources(arg1: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, arg2: typing.Iterable[ConnectionSourceInfo]) -> bool: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class ConnectionModification(Boost.Python.enum):
    Append: ClassVar[ConnectionModification] = ...
    Prepend: ClassVar[ConnectionModification] = ...
    Replace: ClassVar[ConnectionModification] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class ConnectionSourceInfo(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    source: Incomplete
    sourceName: Incomplete
    sourceType: Incomplete
    typeName: Incomplete
    @overload
    def __init__(self, source: ConnectableAPI, sourceName: str | pxr.Ar.ResolvedPath, sourceType: AttributeType, typeName: pxr.Sdf.ValueTypeName = ...) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Usd.Stage, arg3: pxr.Sdf.Path | str) -> None: ...
    @overload
    def __init__(self, output: Output) -> None: ...
    @overload
    def __init__(self, input: Input) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def IsValid(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class CoordSysAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase, name: object) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim, name: object) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> CoordSysAPI: ...
    def ApplyAndBind(self, name: str | pxr.Ar.ResolvedPath, path: pxr.Sdf.Path | str) -> bool: ...
    @overload
    def Bind(self, name: str | pxr.Ar.ResolvedPath, path: pxr.Sdf.Path | str) -> bool: ...
    @overload
    def Bind(self, path: pxr.Sdf.Path | str) -> bool: ...
    def BlockBinding(self, name: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> _CanApplyResult: ...
    @staticmethod
    def CanContainPropertyName(name: str | pxr.Ar.ResolvedPath) -> bool: ...
    @overload
    def ClearBinding(self, name: str | pxr.Ar.ResolvedPath, removeSpec: bool) -> bool: ...
    @overload
    def ClearBinding(self, removeSpec: bool) -> bool: ...
    def CreateBindingRel(self) -> pxr.Usd.Relationship: ...
    def FindBindingWithInheritance(self) -> pxr.UsdSkel.Binding: ...
    def FindBindingsWithInheritance(self) -> list[pxr.UsdSkel.Binding]: ...
    @staticmethod
    def FindBindingsWithInheritanceForPrim(arg1: pxr.Usd.Prim) -> list[pxr.UsdSkel.Binding]: ...
    @overload
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CoordSysAPI: ...
    @overload
    @staticmethod
    def Get(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> CoordSysAPI: ...
    @staticmethod
    def GetAll(prim: pxr.Usd.Prim) -> list[CoordSysAPI]: ...
    def GetBindingRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def GetCoordSysRelationshipName(coordSysName: str | pxr.Ar.ResolvedPath) -> str: ...
    def GetLocalBinding(self) -> pxr.UsdSkel.Binding: ...
    def GetLocalBindings(self) -> list[pxr.UsdSkel.Binding]: ...
    @staticmethod
    def GetLocalBindingsForPrim(prim: pxr.Usd.Prim) -> list[pxr.UsdSkel.Binding]: ...
    @overload
    @staticmethod
    def GetSchemaAttributeNames(arg1: bool, includeInherited: str | pxr.Ar.ResolvedPath) -> list[str]: ...
    @overload
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def HasLocalBindings(self) -> bool: ...
    @staticmethod
    def HasLocalBindingsForPrim(prim: pxr.Usd.Prim) -> bool: ...
    @staticmethod
    def IsCoordSysAPIPath(arg1: pxr.Sdf.Path | str) -> bool: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Input(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CanConnect(self, source: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    def ClearConnectability(self) -> bool: ...
    def ClearSdrMetadata(self) -> None: ...
    def ClearSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> None: ...
    def ClearSource(self) -> bool: ...
    def ClearSources(self) -> bool: ...
    @overload
    def ConnectToSource(self, source: ConnectableAPI, sourceName: str | pxr.Ar.ResolvedPath, sourceType: AttributeType = ..., typeName: pxr.Sdf.ValueTypeName = ...) -> bool: ...
    @overload
    def ConnectToSource(self, source: ConnectionSourceInfo, mod: ConnectionModification = ...) -> bool: ...
    @overload
    def ConnectToSource(self, sourcePath: pxr.Sdf.Path | str) -> bool: ...
    @overload
    def ConnectToSource(self, output: Output) -> bool: ...
    @overload
    def ConnectToSource(self, input: Input) -> bool: ...
    def DisconnectSource(self, sourceAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output = ...) -> bool: ...
    def Get(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> Any: ...
    def GetAttr(self) -> pxr.Usd.Attribute: ...
    def GetBaseName(self) -> str: ...
    def GetConnectability(self) -> str: ...
    def GetConnectedSource(self) -> tuple[ConnectableAPI, str, AttributeType]: ...
    def GetConnectedSources(self) -> tuple[list[SourceInfo], list[pxr.Sdf.Path]]: ...
    def GetDisplayGroup(self) -> str: ...
    def GetDocumentation(self) -> str: ...
    def GetFullName(self) -> str: ...
    def GetPrim(self) -> pxr.Usd.Prim: ...
    def GetRawConnectedSourcePaths(self) -> list[pxr.Sdf.Path]: ...
    def GetRenderType(self) -> str: ...
    def GetSdrMetadata(self) -> dict[str, str]: ...
    def GetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> str: ...
    def GetTypeName(self) -> pxr.Sdf.ValueTypeName: ...
    def GetValueProducingAttribute(self) -> tuple[pxr.Usd.Attribute, AttributeType]: ...
    def GetValueProducingAttributes(self, shaderOutputsOnly: bool = ...) -> list[Attribute]: ...
    def HasConnectedSource(self) -> bool: ...
    def HasRenderType(self) -> bool: ...
    def HasSdrMetadata(self) -> bool: ...
    def HasSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> bool: ...
    @staticmethod
    def IsInput(arg1: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    @staticmethod
    def IsInterfaceInputName(arg1: str | pxr.Ar.ResolvedPath) -> bool: ...
    def IsSourceConnectionFromBaseMaterial(self) -> bool: ...
    def Set(self, value: object, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool: ...
    def SetConnectability(self, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetConnectedSources(self, arg2: typing.Iterable[ConnectionSourceInfo]) -> bool: ...
    def SetDisplayGroup(self, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetDocumentation(self, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetRenderType(self, renderType: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetSdrMetadata(self, sdrMetadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath]) -> None: ...
    def SetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath, value: str | pxr.Ar.ResolvedPath) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class Material(NodeGraph):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def ClearBaseMaterial(self) -> None: ...
    def ComputeDisplacementSource(self, renderContext: object = ...) -> Any: ...
    def ComputeSurfaceSource(self, renderContext: object = ...) -> Any: ...
    def ComputeVolumeSource(self, renderContext: object = ...) -> Any: ...
    def CreateDisplacementAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDisplacementOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output: ...
    @staticmethod
    def CreateMasterMaterialVariant(masterPrim: pxr.Usd.Prim, materialPrims: typing.Iterable[pxr.Usd.Prim], masterVariantSetName: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def CreateSurfaceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSurfaceOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output: ...
    def CreateVolumeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateVolumeOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Material: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Material: ...
    def GetBaseMaterial(self) -> Material: ...
    def GetBaseMaterialPath(self) -> pxr.Sdf.Path: ...
    def GetDisplacementAttr(self) -> pxr.Usd.Attribute: ...
    def GetDisplacementOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output: ...
    def GetDisplacementOutputs(self) -> list[Output]: ...
    def GetEditContextForVariant(self, materialVariantName: str | pxr.Ar.ResolvedPath, layer: pxr.Sdf.Layer = ...) -> pxr.Usd.EditContext: ...
    def GetMaterialVariant(self) -> pxr.Usd.VariantSet: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetSurfaceAttr(self) -> pxr.Usd.Attribute: ...
    def GetSurfaceOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output: ...
    def GetSurfaceOutputs(self) -> list[Output]: ...
    def GetVolumeAttr(self) -> pxr.Usd.Attribute: ...
    def GetVolumeOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output: ...
    def GetVolumeOutputs(self) -> list[Output]: ...
    def HasBaseMaterial(self) -> bool: ...
    def SetBaseMaterial(self, baseMaterial: Material) -> None: ...
    def SetBaseMaterialPath(self, baseLookPath: pxr.Sdf.Path | str) -> None: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class MaterialBindingAPI(pxr.Usd.APISchemaBase):
    class CollectionBinding(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        @overload
        def __init__(self, collBindingRel: pxr.Usd.Relationship) -> None: ...
        @overload
        def __init__(self) -> None: ...
        def GetBindingRel(self) -> pxr.Usd.Relationship: ...
        def GetCollection(self) -> pxr.Usd.CollectionAPI: ...
        def GetCollectionPath(self) -> pxr.Sdf.Path: ...
        def GetMaterial(self) -> Material: ...
        def GetMaterialPath(self) -> pxr.Sdf.Path: ...
        @staticmethod
        def IsCollectionBindingRel(bindingRel: pxr.Usd.Relationship) -> bool: ...
        def IsValid(self) -> bool: ...

    class DirectBinding(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        @overload
        def __init__(self, bindingRel: pxr.Usd.Relationship) -> None: ...
        @overload
        def __init__(self) -> None: ...
        def GetBindingRel(self) -> pxr.Usd.Relationship: ...
        def GetMaterial(self) -> Material: ...
        def GetMaterialPath(self) -> pxr.Sdf.Path: ...
        def GetMaterialPurpose(self) -> str: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def AddPrimToBindingCollection(self, prim: pxr.Usd.Prim, bindingName: str | pxr.Ar.ResolvedPath, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> MaterialBindingAPI: ...
    @overload
    def Bind(self, collection: pxr.Usd.CollectionAPI, material: Material, bindingName: str | pxr.Ar.ResolvedPath = ..., bindingStrength: str | pxr.Ar.ResolvedPath = ..., materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @overload
    def Bind(self, material: Material, bindingStrength: str | pxr.Ar.ResolvedPath = ..., materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    @staticmethod
    def CanContainPropertyName(name: str | pxr.Ar.ResolvedPath) -> bool: ...
    def ComputeBoundMaterial(self, materialPurpose: object = ..., supportLegacyBindings: bool = ...) -> Any: ...
    @staticmethod
    def ComputeBoundMaterials(prims: typing.Iterable[pxr.Usd.Prim], materialPurpose: str | pxr.Ar.ResolvedPath = ..., supportLegacyBindings: bool = ...) -> tuple[list[Material], list[pxr.Usd.Relationship]]: ...
    def CreateMaterialBindSubset(self, subsetName: str | pxr.Ar.ResolvedPath, indices: pxr.Vt.IntArray | typing.Iterable[int], elementType: str | pxr.Ar.ResolvedPath = ...) -> pxr.UsdGeom.Subset: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MaterialBindingAPI: ...
    def GetCollectionBindingRel(self, bindingName: str | pxr.Ar.ResolvedPath, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Relationship: ...
    def GetCollectionBindingRels(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> list[pxr.Usd.Relationship]: ...
    def GetCollectionBindings(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> list[MaterialBindingAPI.CollectionBinding]: ...
    def GetDirectBinding(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> MaterialBindingAPI.DirectBinding: ...
    def GetDirectBindingRel(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Relationship: ...
    def GetMaterialBindSubsets(self) -> list[pxr.UsdGeom.Subset]: ...
    def GetMaterialBindSubsetsFamilyType(self) -> str: ...
    @staticmethod
    def GetMaterialBindingStrength(bindingRel: pxr.Usd.Relationship) -> str: ...
    @staticmethod
    def GetMaterialPurposes() -> list[str]: ...
    @staticmethod
    def GetResolvedTargetPathFromBindingRel(bindingRel: pxr.Usd.Relationship) -> pxr.Sdf.Path: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def RemovePrimFromBindingCollection(self, prim: pxr.Usd.Prim, bindingName: str | pxr.Ar.ResolvedPath, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def SetMaterialBindSubsetsFamilyType(self, familyType: str | pxr.Ar.ResolvedPath) -> bool: ...
    @staticmethod
    def SetMaterialBindingStrength(arg1: pxr.Usd.Relationship, bindingRel: str | pxr.Ar.ResolvedPath) -> bool: ...
    def UnbindAllBindings(self) -> bool: ...
    def UnbindCollectionBinding(self, bindingName: str | pxr.Ar.ResolvedPath, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def UnbindDirectBinding(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class NodeDefAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> NodeDefAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateIdAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateImplementationSourceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NodeDefAPI: ...
    def GetIdAttr(self) -> pxr.Usd.Attribute: ...
    def GetImplementationSource(self) -> str: ...
    def GetImplementationSourceAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetShaderId(self) -> str: ...
    def GetShaderNodeForSourceType(self, sourceType: str | pxr.Ar.ResolvedPath) -> pxr.Sdr.ShaderNode: ...
    def GetSourceAsset(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> pxr.Sdf.AssetPath: ...
    def GetSourceAssetSubIdentifier(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> str: ...
    def GetSourceCode(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> str: ...
    def GetSourceTypes(self) -> list[str]: ...
    def SetShaderId(self, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetSourceAsset(self, sourceAsset: pxr.Sdf.AssetPath | str, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def SetSourceAssetSubIdentifier(self, subIdentifier: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def SetSourceCode(self, sourceCode: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class NodeGraph(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, connectable: ConnectableAPI) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def ComputeInterfaceInputConsumersMap(self, computeTransitiveConsumers: bool = ...) -> dict: ...
    def ComputeOutputSource(self, outputName: str | pxr.Ar.ResolvedPath) -> tuple[Shader, str, AttributeType]: ...
    def ConnectableAPI(self) -> ConnectableAPI: ...
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Input: ...
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, typeName: pxr.Sdf.ValueTypeName) -> Output: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NodeGraph: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NodeGraph: ...
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> Input: ...
    def GetInputs(self, onlyAuthored: bool = ...) -> list[Input]: ...
    def GetInterfaceInputs(self) -> list[Input]: ...
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> Output: ...
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[Output]: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Output(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CanConnect(self, source: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    def ClearSdrMetadata(self) -> None: ...
    def ClearSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> None: ...
    def ClearSource(self) -> bool: ...
    def ClearSources(self) -> bool: ...
    @overload
    def ConnectToSource(self, source: ConnectableAPI, sourceName: str | pxr.Ar.ResolvedPath, sourceType: AttributeType = ..., typeName: pxr.Sdf.ValueTypeName = ...) -> bool: ...
    @overload
    def ConnectToSource(self, source: ConnectionSourceInfo, mod: ConnectionModification = ...) -> bool: ...
    @overload
    def ConnectToSource(self, sourcePath: pxr.Sdf.Path | str) -> bool: ...
    @overload
    def ConnectToSource(self, sourceOutput: Output) -> bool: ...
    @overload
    def ConnectToSource(self, sourceInput: Input) -> bool: ...
    def DisconnectSource(self, sourceAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output = ...) -> bool: ...
    def GetAttr(self) -> pxr.Usd.Attribute: ...
    def GetBaseName(self) -> str: ...
    def GetConnectedSource(self) -> tuple[ConnectableAPI, str, AttributeType]: ...
    def GetConnectedSources(self) -> tuple[list[SourceInfo], list[pxr.Sdf.Path]]: ...
    def GetFullName(self) -> str: ...
    def GetPrim(self) -> pxr.Usd.Prim: ...
    def GetRawConnectedSourcePaths(self) -> list[pxr.Sdf.Path]: ...
    def GetRenderType(self) -> str: ...
    def GetSdrMetadata(self) -> dict[str, str]: ...
    def GetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> str: ...
    def GetTypeName(self) -> pxr.Sdf.ValueTypeName: ...
    def GetValueProducingAttributes(self, shaderOutputsOnly: bool = ...) -> list[Attribute]: ...
    def HasConnectedSource(self) -> bool: ...
    def HasRenderType(self) -> bool: ...
    def HasSdrMetadata(self) -> bool: ...
    def HasSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> bool: ...
    @staticmethod
    def IsOutput(arg1: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    def IsSourceConnectionFromBaseMaterial(self) -> bool: ...
    def Set(self, value: object, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool: ...
    def SetConnectedSources(self, arg2: typing.Iterable[ConnectionSourceInfo]) -> bool: ...
    def SetRenderType(self, renderType: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetSdrMetadata(self, sdrMetadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath]) -> None: ...
    def SetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath, value: str | pxr.Ar.ResolvedPath) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class Shader(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, connectable: ConnectableAPI) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def ClearSdrMetadata(self) -> None: ...
    def ClearSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> None: ...
    def ConnectableAPI(self) -> ConnectableAPI: ...
    def CreateIdAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateImplementationSourceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Input: ...
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Output: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Shader: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Shader: ...
    def GetIdAttr(self) -> pxr.Usd.Attribute: ...
    def GetImplementationSource(self) -> str: ...
    def GetImplementationSourceAttr(self) -> pxr.Usd.Attribute: ...
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> Input: ...
    def GetInputs(self, onlyAuthored: bool = ...) -> list[Input]: ...
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> Output: ...
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[Output]: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetSdrMetadata(self) -> dict[str, str]: ...
    def GetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> str: ...
    def GetShaderId(self) -> str: ...
    def GetShaderNodeForSourceType(self, sourceType: str | pxr.Ar.ResolvedPath) -> pxr.Sdr.ShaderNode: ...
    def GetSourceAsset(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> pxr.Sdf.AssetPath: ...
    def GetSourceAssetSubIdentifier(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> str: ...
    def GetSourceCode(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> str: ...
    def GetSourceTypes(self) -> list[str]: ...
    def HasSdrMetadata(self) -> bool: ...
    def HasSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetSdrMetadata(self, sdrMetadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath]) -> None: ...
    def SetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath, value: str | pxr.Ar.ResolvedPath) -> None: ...
    def SetShaderId(self, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetSourceAsset(self, sourceAsset: pxr.Sdf.AssetPath | str, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def SetSourceAssetSubIdentifier(self, subIdentifier: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def SetSourceCode(self, sourceCode: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class ShaderDefParserPlugin(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetDiscoveryTypes(self) -> list[str]: ...
    def GetSourceType(self) -> str: ...
    def Parse(self, arg2: pxr.Ndr.NodeDiscoveryResult) -> pxr.Sdr.ShaderNode: ...

class ShaderDefUtils(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def GetNodeDiscoveryResults(shaderDef: Shader, sourceUri: str | pxr.Ar.ResolvedPath) -> list: ...
    @staticmethod
    def GetPrimvarNamesMetadataString(metadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath], shaderDef: ConnectableAPI) -> str: ...
    @staticmethod
    def GetShaderProperties(shaderDef: ConnectableAPI) -> list[[pxr.Ndr.Property]]: ...

class Tokens(Boost.Python.instance):
    ConnectableAPI: ClassVar[str] = ...  # read-only
    CoordSysAPI: ClassVar[str] = ...  # read-only
    Material: ClassVar[str] = ...  # read-only
    MaterialBindingAPI: ClassVar[str] = ...  # read-only
    NodeDefAPI: ClassVar[str] = ...  # read-only
    NodeGraph: ClassVar[str] = ...  # read-only
    Shader: ClassVar[str] = ...  # read-only
    allPurpose: ClassVar[str] = ...  # read-only
    bindMaterialAs: ClassVar[str] = ...  # read-only
    coordSys: ClassVar[str] = ...  # read-only
    coordSys_MultipleApplyTemplate_Binding: ClassVar[str] = ...  # read-only
    displacement: ClassVar[str] = ...  # read-only
    fallbackStrength: ClassVar[str] = ...  # read-only
    full: ClassVar[str] = ...  # read-only
    id: ClassVar[str] = ...  # read-only
    infoId: ClassVar[str] = ...  # read-only
    infoImplementationSource: ClassVar[str] = ...  # read-only
    inputs: ClassVar[str] = ...  # read-only
    interfaceOnly: ClassVar[str] = ...  # read-only
    materialBind: ClassVar[str] = ...  # read-only
    materialBinding: ClassVar[str] = ...  # read-only
    materialBindingCollection: ClassVar[str] = ...  # read-only
    materialVariant: ClassVar[str] = ...  # read-only
    outputs: ClassVar[str] = ...  # read-only
    outputsDisplacement: ClassVar[str] = ...  # read-only
    outputsSurface: ClassVar[str] = ...  # read-only
    outputsVolume: ClassVar[str] = ...  # read-only
    preview: ClassVar[str] = ...  # read-only
    sdrMetadata: ClassVar[str] = ...  # read-only
    sourceAsset: ClassVar[str] = ...  # read-only
    sourceCode: ClassVar[str] = ...  # read-only
    strongerThanDescendants: ClassVar[str] = ...  # read-only
    subIdentifier: ClassVar[str] = ...  # read-only
    surface: ClassVar[str] = ...  # read-only
    universalRenderContext: ClassVar[str] = ...  # read-only
    universalSourceType: ClassVar[str] = ...  # read-only
    volume: ClassVar[str] = ...  # read-only
    weakerThanDescendants: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...

class UdimUtils(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def IsUdimIdentifier(identifier: str | pxr.Ar.ResolvedPath) -> bool: ...
    @staticmethod
    def ReplaceUdimPattern(identifierWithPattern: str | pxr.Ar.ResolvedPath, replacement: str | pxr.Ar.ResolvedPath) -> str: ...
    @staticmethod
    def ResolveUdimPath(udimPath: str | pxr.Ar.ResolvedPath, layer: pxr.Sdf.Layer) -> str: ...
    @staticmethod
    def ResolveUdimTilePaths(udimPath: str | pxr.Ar.ResolvedPath, layer: pxr.Sdf.Layer) -> list[ResolvedPathAndTile]: ...

class Utils(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def GetBaseNameAndType(arg1: str | pxr.Ar.ResolvedPath) -> tuple[str, AttributeType]: ...
    @staticmethod
    def GetConnectedSourcePath(connectionSourceInfo: ConnectionSourceInfo) -> pxr.Sdf.Path: ...
    @staticmethod
    def GetFullName(arg1: str | pxr.Ar.ResolvedPath, arg2: AttributeType) -> str: ...
    @staticmethod
    def GetPrefixForAttributeType(arg1: AttributeType) -> str: ...
    @staticmethod
    def GetType(arg1: str | pxr.Ar.ResolvedPath) -> AttributeType: ...
    @overload
    @staticmethod
    def GetValueProducingAttributes(output: Output, shaderOutputsOnly: bool = ...) -> list[Attribute]: ...
    @overload
    @staticmethod
    def GetValueProducingAttributes(input: Input, shaderOutputsOnly: bool = ...) -> list[Attribute]: ...

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int) -> Any: ...
    def __iter__(self) -> typing.Iterator[Any]: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self): ...
