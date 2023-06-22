import Boost.Python
import pxr.Sdf
import types
from typing import Any, ClassVar, overload

ArcTypeInherit: ArcType
ArcTypePayload: ArcType
ArcTypeReference: ArcType
ArcTypeRelocate: ArcType
ArcTypeRoot: ArcType
ArcTypeSpecialize: ArcType
ArcTypeVariant: ArcType
DependencyTypeAncestral: DependencyType
DependencyTypeAnyIncludingVirtual: DependencyType
DependencyTypeAnyNonVirtual: DependencyType
DependencyTypeDirect: DependencyType
DependencyTypeNonVirtual: DependencyType
DependencyTypeNone: DependencyType
DependencyTypePartlyDirect: DependencyType
DependencyTypePurelyDirect: DependencyType
DependencyTypeRoot: DependencyType
DependencyTypeVirtual: DependencyType
ErrorType_ArcCapacityExceeded: ErrorType
ErrorType_ArcCycle: ErrorType
ErrorType_ArcNamespaceDepthCapacityExceeded: ErrorType
ErrorType_ArcPermissionDenied: ErrorType
ErrorType_InconsistentAttributeType: ErrorType
ErrorType_InconsistentAttributeVariability: ErrorType
ErrorType_InconsistentPropertyType: ErrorType
ErrorType_IndexCapacityExceeded: ErrorType
ErrorType_InternalAssetPath: ErrorType
ErrorType_InvalidAssetPath: ErrorType
ErrorType_InvalidExternalTargetPath: ErrorType
ErrorType_InvalidInstanceTargetPath: ErrorType
ErrorType_InvalidPrimPath: ErrorType
ErrorType_InvalidReferenceOffset: ErrorType
ErrorType_InvalidSublayerOffset: ErrorType
ErrorType_InvalidSublayerOwnership: ErrorType
ErrorType_InvalidSublayerPath: ErrorType
ErrorType_InvalidTargetPath: ErrorType
ErrorType_InvalidVariantSelection: ErrorType
ErrorType_OpinionAtRelocationSource: ErrorType
ErrorType_PrimPermissionDenied: ErrorType
ErrorType_PropertyPermissionDenied: ErrorType
ErrorType_SublayerCycle: ErrorType
ErrorType_TargetPermissionDenied: ErrorType
ErrorType_UnresolvedPrimPath: ErrorType

class ArcType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetValueFromName(self, name: object) -> Any: ...
    def __reduce__(self) -> Any: ...

class Cache(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, layerStackIdentifier: LayerStackIdentifier, fileFormatTarget: object = ..., usd: bool = ...) -> None: ...
    def ComputeAttributeConnectionPaths(self, relPath: pxr.Sdf.Path, localOnly: bool = ..., stopProperty: pxr.Sdf.Spec = ..., includeStopProperty: bool = ...) -> tuple: ...
    def ComputeLayerStack(self, arg2: LayerStackIdentifier) -> tuple: ...
    def ComputePrimIndex(self, arg2: pxr.Sdf.Path) -> tuple: ...
    def ComputePropertyIndex(self, arg2: pxr.Sdf.Path) -> tuple: ...
    def ComputeRelationshipTargetPaths(self, relPath: pxr.Sdf.Path, localOnly: bool = ..., stopProperty: pxr.Sdf.Spec = ..., includeStopProperty: bool = ...) -> tuple: ...
    def FindAllLayerStacksUsingLayer(self, arg2: pxr.Sdf.Layer) -> list[LayerStack]: ...
    def FindPrimIndex(self, arg2: pxr.Sdf.Path) -> PrimIndex: ...
    def FindPropertyIndex(self, arg2: pxr.Sdf.Path) -> PropertyIndex: ...
    def FindSiteDependencies(self, siteLayerStack: LayerStack, sitePath: pxr.Sdf.Path, dependencyType: int = ..., recurseOnSite: bool = ..., recurseOnIndex: bool = ..., filterForExistingCachesOnly: bool = ...) -> list: ...
    def GetDynamicFileFormatArgumentDependencyData(self, arg2: pxr.Sdf.Path) -> DynamicFileFormatDependencyData: ...
    def GetLayerStackIdentifier(self) -> LayerStackIdentifier: ...
    def GetMutedLayers(self) -> list[str]: ...
    def GetUsedLayers(self) -> list[pxr.Sdf.Layer]: ...
    def GetUsedLayersRevision(self) -> int: ...
    def GetVariantFallbacks(self) -> dict: ...
    def HasAnyDynamicFileFormatArgumentDependencies(self) -> bool: ...
    def HasRootLayerStack(self, arg2: LayerStack) -> bool: ...
    def IsInvalidAssetPath(self, arg2: str) -> bool: ...
    def IsInvalidSublayerIdentifier(self, arg2: str) -> bool: ...
    def IsLayerMuted(self, layerIdentifier: object) -> bool: ...
    def IsPayloadIncluded(self, arg2: pxr.Sdf.Path) -> bool: ...
    def IsPossibleDynamicFileFormatArgumentField(self, arg2: str) -> bool: ...
    def PrintStatistics(self) -> None: ...
    def Reload(self) -> None: ...
    def RequestLayerMuting(self, layersToMute: list[str], layersToUnmute: list[str]) -> None: ...
    def RequestPayloads(self, arg2: pxr.Sdf.PathSet, arg3: pxr.Sdf.PathSet) -> None: ...
    def SetVariantFallbacks(self, arg2: dict) -> None: ...
    def UsesLayerStack(self, arg2: LayerStack) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def fileFormatTarget(self) -> type: ...
    @property
    def layerStack(self) -> type: ...

class Dependency(Boost.Python.instance):
    indexPath: Any
    mapFunc: Any
    sitePath: Any
    def __init__(self, arg2: pxr.Sdf.Path, arg3: pxr.Sdf.Path, arg4: MapFunction) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...

class DependencyType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetValueFromName(self, name: object) -> Any: ...
    def __reduce__(self) -> Any: ...

class DynamicFileFormatDependencyData(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def CanFieldChangeAffectFileFormatArguments(self, arg2: str, arg3: Any, arg4: Any) -> bool: ...
    def GetRelevantFieldNames(self) -> list: ...
    def IsEmpty(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class ErrorArcCycle(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorArcPermissionDenied(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorBase(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def errorType(self) -> Any: ...

class ErrorCapacityExceeded(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInconsistentAttributeType(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInconsistentAttributeVariability(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInconsistentPropertyType(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInvalidAssetPath(ErrorInvalidAssetPathBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInvalidAssetPathBase(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInvalidExternalTargetPath(ErrorTargetPathBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInvalidInstanceTargetPath(ErrorTargetPathBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInvalidPrimPath(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInvalidReferenceOffset(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInvalidSublayerOffset(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInvalidSublayerOwnership(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInvalidSublayerPath(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorInvalidTargetPath(ErrorTargetPathBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorMutedAssetPath(ErrorInvalidAssetPathBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorOpinionAtRelocationSource(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorPrimPermissionDenied(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorPropertyPermissionDenied(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorSublayerCycle(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorTargetPathBase(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorTargetPermissionDenied(ErrorTargetPathBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ErrorType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetValueFromName(self, name: object) -> Any: ...
    def __reduce__(self) -> Any: ...

class ErrorUnresolvedPrimPath(ErrorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class InstanceKey(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, primIndex: PrimIndex) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...

class LayerStack(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...
    @property
    def identifier(self) -> type: ...
    @property
    def incrementalRelocatesSourceToTarget(self) -> type: ...
    @property
    def incrementalRelocatesTargetToSource(self) -> type: ...
    @property
    def layerOffsets(self) -> Any: ...
    @property
    def layerTree(self) -> type: ...
    @property
    def layers(self) -> type: ...
    @property
    def localErrors(self) -> type: ...
    @property
    def mutedLayers(self) -> type: ...
    @property
    def pathsToPrimsWithRelocates(self) -> type: ...
    @property
    def relocatesSourceToTarget(self) -> type: ...
    @property
    def relocatesTargetToSource(self) -> type: ...

class LayerStackIdentifier(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, rootLayer: pxr.Sdf.Layer, sessionLayer: pxr.Sdf.Layer = ..., pathResolverContext: pxr.Ar.ResolverContext = ...) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def pathResolverContext(self) -> Any: ...
    @property
    def rootLayer(self) -> Any: ...
    @property
    def sessionLayer(self) -> Any: ...

class LayerStackSite(Boost.Python.instance):
    layerStack: Any
    path: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class MapExpression(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def AddRootIdentity(self) -> MapExpression: ...
    def Compose(self, arg2: MapExpression) -> MapExpression: ...
    @classmethod
    def Constant(cls, arg1: MapFunction) -> MapExpression: ...
    def Evaluate(self) -> MapFunction: ...
    @classmethod
    def Identity(cls) -> MapExpression: ...
    def Inverse(self) -> MapExpression: ...
    def MapSourceToTarget(self, path: pxr.Sdf.Path) -> pxr.Sdf.Path: ...
    def MapTargetToSource(self, path: pxr.Sdf.Path) -> pxr.Sdf.Path: ...
    def __reduce__(self) -> Any: ...
    @property
    def isIdentity(self) -> type: ...
    @property
    def isNull(self) -> type: ...
    @property
    def timeOffset(self) -> type: ...

class MapFunction(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: MapFunction) -> None: ...
    @overload
    def __init__(self, sourceToTargetMap: dict, timeOffset: pxr.Sdf.LayerOffset = ...) -> None: ...
    def Compose(self, arg2: MapFunction) -> MapFunction: ...
    def ComposeOffset(self, offset: pxr.Sdf.LayerOffset) -> MapFunction: ...
    def GetInverse(self) -> MapFunction: ...
    @classmethod
    def Identity(cls) -> MapFunction: ...
    @classmethod
    def IdentityPathMap(cls) -> dict: ...
    def MapSourceToTarget(self, path: pxr.Sdf.Path) -> pxr.Sdf.Path: ...
    def MapTargetToSource(self, path: pxr.Sdf.Path) -> pxr.Sdf.Path: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def isIdentity(self) -> type: ...
    @property
    def isIdentityPathMapping(self) -> type: ...
    @property
    def isNull(self) -> type: ...
    @property
    def sourceToTargetMap(self) -> type: ...
    @property
    def timeOffset(self) -> type: ...

class NodeRef(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def CanContributeSpecs(self) -> bool: ...
    def GetDepthBelowIntroduction(self) -> int: ...
    def GetIntroPath(self) -> pxr.Sdf.Path: ...
    def GetOriginRootNode(self) -> NodeRef: ...
    def GetPathAtIntroduction(self) -> pxr.Sdf.Path: ...
    def GetRootNode(self) -> NodeRef: ...
    def IsDueToAncestor(self) -> bool: ...
    def IsRootNode(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def arcType(self) -> type: ...
    @property
    def children(self) -> Any: ...
    @property
    def hasSpecs(self) -> type: ...
    @property
    def hasSymmetry(self) -> type: ...
    @property
    def isCulled(self) -> type: ...
    @property
    def isInert(self) -> type: ...
    @property
    def isRestricted(self) -> type: ...
    @property
    def layerStack(self) -> type: ...
    @property
    def mapToParent(self) -> type: ...
    @property
    def mapToRoot(self) -> type: ...
    @property
    def namespaceDepth(self) -> type: ...
    @property
    def origin(self) -> Any: ...
    @property
    def parent(self) -> Any: ...
    @property
    def path(self) -> type: ...
    @property
    def permission(self) -> type: ...
    @property
    def siblingNumAtOrigin(self) -> type: ...
    @property
    def site(self) -> type: ...

class PrimIndex(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def ComposeAuthoredVariantSelections(self) -> dict: ...
    def ComputePrimChildNames(self) -> tuple: ...
    def ComputePrimPropertyNames(self) -> list: ...
    def DumpToDotGraph(self, filename: str, includeInheritOriginInfo: bool = ..., includeMaps: bool = ...) -> None: ...
    def DumpToString(self, includeInheritOriginInfo: bool = ..., includeMaps: bool = ...) -> str: ...
    @overload
    def GetNodeProvidingSpec(self, primSpec: pxr.Sdf.PrimSpec) -> NodeRef: ...
    @overload
    def GetNodeProvidingSpec(self, layer: pxr.Sdf.Layer, path: pxr.Sdf.Path) -> NodeRef: ...
    def GetSelectionAppliedForVariantSet(self, arg2: str) -> str: ...
    def IsInstanceable(self) -> bool: ...
    def IsValid(self) -> bool: ...
    def PrintStatistics(self) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def hasAnyPayloads(self) -> Any: ...
    @property
    def localErrors(self) -> type: ...
    @property
    def primStack(self) -> Any: ...
    @property
    def rootNode(self) -> type: ...

class PropertyIndex(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def localErrors(self) -> type: ...
    @property
    def localPropertyStack(self) -> Any: ...
    @property
    def propertyStack(self) -> Any: ...

class Site(Boost.Python.instance):
    layerStack: Any
    path: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class _TestChangeProcessor(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: Cache) -> None: ...
    def GetPrimChanges(self) -> list: ...
    def GetSignificantChanges(self) -> list: ...
    def GetSpecChanges(self) -> list: ...
    def __enter__(self) -> _TestChangeProcessor: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType) -> None: ...
    def __reduce__(self) -> Any: ...

def TranslatePathFromNodeToRoot(arg1: NodeRef, sourceNode: pxr.Sdf.Path) -> pxr.Sdf.Path: ...
def TranslatePathFromRootToNode(arg1: NodeRef, destNode: pxr.Sdf.Path) -> pxr.Sdf.Path: ...