import Boost.Python
import pxr.Tf
from typing import Any, ClassVar, overload

class AssetInfo(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    assetName: Any
    resolverInfo: Any
    version: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __eq__(self, arg2: AssetInfo) -> Any: ...
    def __hash__(self) -> int: ...
    def __ne__(self, arg2: AssetInfo) -> Any: ...
    def __reduce__(self) -> Any: ...

class DefaultResolver(Resolver):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def SetDefaultSearchPath(cls, searchPath: object) -> None: ...
    def __reduce__(self) -> Any: ...

class DefaultResolverContext(Boost.Python.instance):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, searchPaths: object) -> None: ...
    def GetSearchPath(self) -> Any: ...
    def __eq__(self, arg2: DefaultResolverContext) -> Any: ...
    def __hash__(self) -> int: ...
    def __ne__(self, arg2: DefaultResolverContext) -> Any: ...
    def __reduce__(self) -> Any: ...

class Notice(Boost.Python.instance):
    class ResolverChanged(ResolverNotice):
        def __init__(self, *args, **kwargs) -> None: ...
        def AffectsContext(self, context: ResolverContext) -> bool: ...
        def __reduce__(self) -> Any: ...
    class ResolverNotice(pxr.Tf.Notice):
        def __init__(self, *args, **kwargs) -> None: ...
        def __reduce__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class ResolvedPath(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: object) -> None: ...
    def GetPathString(self) -> str: ...
    def __bool__(self) -> bool: ...
    @overload
    def __eq__(self, arg2: ResolvedPath) -> Any: ...
    @overload
    def __eq__(self, arg2: object) -> Any: ...
    @overload
    def __ge__(self, arg2: ResolvedPath) -> Any: ...
    @overload
    def __ge__(self, arg2: object) -> Any: ...
    @overload
    def __gt__(self, arg2: ResolvedPath) -> Any: ...
    @overload
    def __gt__(self, arg2: object) -> Any: ...
    def __hash__(self) -> int: ...
    @overload
    def __le__(self, arg2: ResolvedPath) -> Any: ...
    @overload
    def __le__(self, arg2: object) -> Any: ...
    @overload
    def __lt__(self, arg2: ResolvedPath) -> Any: ...
    @overload
    def __lt__(self, arg2: object) -> Any: ...
    @overload
    def __ne__(self, arg2: ResolvedPath) -> Any: ...
    @overload
    def __ne__(self, arg2: object) -> Any: ...
    def __reduce__(self) -> Any: ...

class Resolver(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def CanWriteAssetToPath(self, resolvedPath: ResolvedPath) -> _PyAnnotatedBoolResult: ...
    @overload
    def CreateContextFromString(self, contextStr: object) -> ResolverContext: ...
    @overload
    def CreateContextFromString(self, uriScheme: object, contextStr: object) -> ResolverContext: ...
    def CreateContextFromStrings(self, contextStrs: object) -> ResolverContext: ...
    def CreateDefaultContext(self) -> ResolverContext: ...
    def CreateDefaultContextForAsset(self, assetPath: object) -> ResolverContext: ...
    def CreateIdentifier(self, assetPath: object, anchorAssetPath: ResolvedPath = ...) -> str: ...
    def CreateIdentifierForNewAsset(self, assetPath: object, anchorAssetPath: ResolvedPath = ...) -> str: ...
    def GetAssetInfo(self, assetPath: object, resolvedPath: ResolvedPath) -> AssetInfo: ...
    def GetCurrentContext(self) -> ResolverContext: ...
    def GetExtension(self, assetPath: object) -> str: ...
    def GetModificationTimestamp(self, assetPath: object, resolvedPath: ResolvedPath) -> Timestamp: ...
    def IsContextDependentPath(self, assetPath: object) -> bool: ...
    def RefreshContext(self, arg2: ResolverContext) -> None: ...
    def Resolve(self, assetPath: object) -> ResolvedPath: ...
    def ResolveForNewAsset(self, assetPath: object) -> ResolvedPath: ...
    def __reduce__(self) -> Any: ...

class ResolverContext(Boost.Python.instance):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: object) -> Any: ...
    def Get(self) -> list: ...
    def GetDebugString(self) -> str: ...
    def IsEmpty(self) -> bool: ...
    def __eq__(self, arg2: ResolverContext) -> Any: ...
    def __hash__(self) -> int: ...
    def __lt__(self, arg2: ResolverContext) -> Any: ...
    def __ne__(self, arg2: ResolverContext) -> Any: ...
    def __reduce__(self) -> Any: ...

class ResolverContextBinder(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: ResolverContext) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, arg2: object, arg3: object, arg4: object) -> bool: ...
    def __reduce__(self) -> Any: ...

class ResolverScopedCache(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, arg2: object, arg3: object, arg4: object) -> bool: ...
    def __reduce__(self) -> Any: ...

class Timestamp(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: float) -> None: ...
    @overload
    def __init__(self, arg2: Timestamp) -> None: ...
    def GetTime(self) -> float: ...
    def IsValid(self) -> bool: ...
    def __eq__(self, arg2: Timestamp) -> Any: ...
    def __ge__(self, arg2: Timestamp) -> Any: ...
    def __gt__(self, arg2: Timestamp) -> Any: ...
    def __hash__(self) -> int: ...
    def __le__(self, arg2: Timestamp) -> Any: ...
    def __lt__(self, arg2: Timestamp) -> Any: ...
    def __ne__(self, arg2: Timestamp) -> Any: ...
    def __reduce__(self) -> Any: ...

class _PyAnnotatedBoolResult(Boost.Python.instance):
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

def GetResolver() -> Resolver: ...
def GetUnderlyingResolver() -> Resolver: ...
def IsPackageRelativePath(path: object) -> bool: ...
@overload
def JoinPackageRelativePath(paths: object) -> str: ...
@overload
def JoinPackageRelativePath(paths: object) -> str: ...
@overload
def JoinPackageRelativePath(packagePath: object, packagedPath: object) -> str: ...
def SetPreferredResolver(resolverTypeName: object) -> None: ...
def SplitPackageRelativePathInner(path: object) -> Any: ...
def SplitPackageRelativePathOuter(path: object) -> Any: ...
def _TestImplicitConversion(arg1: ResolverContext) -> ResolverContext: ...