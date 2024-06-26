# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Sdf
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
import typing
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class ArticulationRootAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> ArticulationRootAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> ArticulationRootAPI: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class CollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> CollisionAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateCollisionEnabledAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSimulationOwnerRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CollisionAPI: ...
    def GetCollisionEnabledAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetSimulationOwnerRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class CollisionGroup(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def ComputeCollisionGroupTable(stage: pxr.Usd.Stage) -> CollisionGroupTable: ...
    def CreateFilteredGroupsRel(self) -> pxr.Usd.Relationship: ...
    def CreateInvertFilteredGroupsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateMergeGroupNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CollisionGroup: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CollisionGroup: ...
    def GetCollidersCollectionAPI(self) -> pxr.Usd.CollectionAPI: ...
    def GetFilteredGroupsRel(self) -> pxr.Usd.Relationship: ...
    def GetInvertFilteredGroupsAttr(self) -> pxr.Usd.Attribute: ...
    def GetMergeGroupNameAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class CollisionGroupTable(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetGroups(self) -> list: ...
    def IsCollisionEnabled(self, arg2: object, arg3: object) -> bool: ...

class DistanceJoint(Joint):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateMaxDistanceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateMinDistanceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DistanceJoint: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DistanceJoint: ...
    def GetMaxDistanceAttr(self) -> pxr.Usd.Attribute: ...
    def GetMinDistanceAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class DriveAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase, name: object) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim, name: object) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> DriveAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> _CanApplyResult: ...
    def CreateDampingAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateMaxForceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateStiffnessAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateTargetPositionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateTargetVelocityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @overload
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DriveAPI: ...
    @overload
    @staticmethod
    def Get(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> DriveAPI: ...
    @staticmethod
    def GetAll(prim: pxr.Usd.Prim) -> list[DriveAPI]: ...
    def GetDampingAttr(self) -> pxr.Usd.Attribute: ...
    def GetMaxForceAttr(self) -> pxr.Usd.Attribute: ...
    @overload
    @staticmethod
    def GetSchemaAttributeNames(arg1: bool, includeInherited: str | pxr.Ar.ResolvedPath) -> list[str]: ...
    @overload
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetStiffnessAttr(self) -> pxr.Usd.Attribute: ...
    def GetTargetPositionAttr(self) -> pxr.Usd.Attribute: ...
    def GetTargetVelocityAttr(self) -> pxr.Usd.Attribute: ...
    def GetTypeAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def IsPhysicsDriveAPIPath(arg1: pxr.Sdf.Path | str) -> bool: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class FilteredPairsAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> FilteredPairsAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateFilteredPairsRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> FilteredPairsAPI: ...
    def GetFilteredPairsRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class FixedJoint(Joint):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> FixedJoint: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> FixedJoint: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Joint(pxr.UsdGeom.Imageable):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateBody0Rel(self) -> pxr.Usd.Relationship: ...
    def CreateBody1Rel(self) -> pxr.Usd.Relationship: ...
    def CreateBreakForceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateBreakTorqueAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateCollisionEnabledAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateExcludeFromArticulationAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateJointEnabledAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLocalPos0Attr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLocalPos1Attr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLocalRot0Attr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLocalRot1Attr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Joint: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Joint: ...
    def GetBody0Rel(self) -> pxr.Usd.Relationship: ...
    def GetBody1Rel(self) -> pxr.Usd.Relationship: ...
    def GetBreakForceAttr(self) -> pxr.Usd.Attribute: ...
    def GetBreakTorqueAttr(self) -> pxr.Usd.Attribute: ...
    def GetCollisionEnabledAttr(self) -> pxr.Usd.Attribute: ...
    def GetExcludeFromArticulationAttr(self) -> pxr.Usd.Attribute: ...
    def GetJointEnabledAttr(self) -> pxr.Usd.Attribute: ...
    def GetLocalPos0Attr(self) -> pxr.Usd.Attribute: ...
    def GetLocalPos1Attr(self) -> pxr.Usd.Attribute: ...
    def GetLocalRot0Attr(self) -> pxr.Usd.Attribute: ...
    def GetLocalRot1Attr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class LimitAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase, name: object) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim, name: object) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> LimitAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> _CanApplyResult: ...
    def CreateHighAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLowAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @overload
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> LimitAPI: ...
    @overload
    @staticmethod
    def Get(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> LimitAPI: ...
    @staticmethod
    def GetAll(prim: pxr.Usd.Prim) -> list[LimitAPI]: ...
    def GetHighAttr(self) -> pxr.Usd.Attribute: ...
    def GetLowAttr(self) -> pxr.Usd.Attribute: ...
    @overload
    @staticmethod
    def GetSchemaAttributeNames(arg1: bool, includeInherited: str | pxr.Ar.ResolvedPath) -> list[str]: ...
    @overload
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def IsPhysicsLimitAPIPath(arg1: pxr.Sdf.Path | str) -> bool: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class MassAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> MassAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateCenterOfMassAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDensityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDiagonalInertiaAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateMassAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreatePrincipalAxesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MassAPI: ...
    def GetCenterOfMassAttr(self) -> pxr.Usd.Attribute: ...
    def GetDensityAttr(self) -> pxr.Usd.Attribute: ...
    def GetDiagonalInertiaAttr(self) -> pxr.Usd.Attribute: ...
    def GetMassAttr(self) -> pxr.Usd.Attribute: ...
    def GetPrincipalAxesAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class MassUnits(Boost.Python.instance):
    grams: ClassVar[float] = ...  # read-only
    kilograms: ClassVar[float] = ...  # read-only
    slugs: ClassVar[float] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...

class MaterialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> MaterialAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateDensityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDynamicFrictionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateRestitutionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateStaticFrictionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MaterialAPI: ...
    def GetDensityAttr(self) -> pxr.Usd.Attribute: ...
    def GetDynamicFrictionAttr(self) -> pxr.Usd.Attribute: ...
    def GetRestitutionAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetStaticFrictionAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class MeshCollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> MeshCollisionAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateApproximationAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MeshCollisionAPI: ...
    def GetApproximationAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class PrismaticJoint(Joint):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLowerLimitAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateUpperLimitAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PrismaticJoint: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PrismaticJoint: ...
    def GetAxisAttr(self) -> pxr.Usd.Attribute: ...
    def GetLowerLimitAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetUpperLimitAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class RevoluteJoint(Joint):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLowerLimitAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateUpperLimitAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> RevoluteJoint: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> RevoluteJoint: ...
    def GetAxisAttr(self) -> pxr.Usd.Attribute: ...
    def GetLowerLimitAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetUpperLimitAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class RigidBodyAPI(pxr.Usd.APISchemaBase):
    class MassInformation(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        centerOfMass: Incomplete
        inertia: Incomplete
        localPos: Incomplete
        localRot: Incomplete
        volume: Incomplete
        def __init__(self) -> None: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> RigidBodyAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def ComputeMassProperties(self, arg2: MassInformationFn) -> tuple: ...
    def CreateAngularVelocityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateKinematicEnabledAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateRigidBodyEnabledAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSimulationOwnerRel(self) -> pxr.Usd.Relationship: ...
    def CreateStartsAsleepAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateVelocityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> RigidBodyAPI: ...
    def GetAngularVelocityAttr(self) -> pxr.Usd.Attribute: ...
    def GetKinematicEnabledAttr(self) -> pxr.Usd.Attribute: ...
    def GetRigidBodyEnabledAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetSimulationOwnerRel(self) -> pxr.Usd.Relationship: ...
    def GetStartsAsleepAttr(self) -> pxr.Usd.Attribute: ...
    def GetVelocityAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Scene(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateGravityDirectionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateGravityMagnitudeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Scene: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Scene: ...
    def GetGravityDirectionAttr(self) -> pxr.Usd.Attribute: ...
    def GetGravityMagnitudeAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class SphericalJoint(Joint):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateConeAngle0LimitAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateConeAngle1LimitAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SphericalJoint: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SphericalJoint: ...
    def GetAxisAttr(self) -> pxr.Usd.Attribute: ...
    def GetConeAngle0LimitAttr(self) -> pxr.Usd.Attribute: ...
    def GetConeAngle1LimitAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Tokens(Boost.Python.instance):
    PhysicsArticulationRootAPI: ClassVar[str] = ...  # read-only
    PhysicsCollisionAPI: ClassVar[str] = ...  # read-only
    PhysicsCollisionGroup: ClassVar[str] = ...  # read-only
    PhysicsDistanceJoint: ClassVar[str] = ...  # read-only
    PhysicsDriveAPI: ClassVar[str] = ...  # read-only
    PhysicsFilteredPairsAPI: ClassVar[str] = ...  # read-only
    PhysicsFixedJoint: ClassVar[str] = ...  # read-only
    PhysicsJoint: ClassVar[str] = ...  # read-only
    PhysicsLimitAPI: ClassVar[str] = ...  # read-only
    PhysicsMassAPI: ClassVar[str] = ...  # read-only
    PhysicsMaterialAPI: ClassVar[str] = ...  # read-only
    PhysicsMeshCollisionAPI: ClassVar[str] = ...  # read-only
    PhysicsPrismaticJoint: ClassVar[str] = ...  # read-only
    PhysicsRevoluteJoint: ClassVar[str] = ...  # read-only
    PhysicsRigidBodyAPI: ClassVar[str] = ...  # read-only
    PhysicsScene: ClassVar[str] = ...  # read-only
    PhysicsSphericalJoint: ClassVar[str] = ...  # read-only
    acceleration: ClassVar[str] = ...  # read-only
    angular: ClassVar[str] = ...  # read-only
    boundingCube: ClassVar[str] = ...  # read-only
    boundingSphere: ClassVar[str] = ...  # read-only
    colliders: ClassVar[str] = ...  # read-only
    convexDecomposition: ClassVar[str] = ...  # read-only
    convexHull: ClassVar[str] = ...  # read-only
    distance: ClassVar[str] = ...  # read-only
    drive: ClassVar[str] = ...  # read-only
    drive_MultipleApplyTemplate_PhysicsDamping: ClassVar[str] = ...  # read-only
    drive_MultipleApplyTemplate_PhysicsMaxForce: ClassVar[str] = ...  # read-only
    drive_MultipleApplyTemplate_PhysicsStiffness: ClassVar[str] = ...  # read-only
    drive_MultipleApplyTemplate_PhysicsTargetPosition: ClassVar[str] = ...  # read-only
    drive_MultipleApplyTemplate_PhysicsTargetVelocity: ClassVar[str] = ...  # read-only
    drive_MultipleApplyTemplate_PhysicsType: ClassVar[str] = ...  # read-only
    force: ClassVar[str] = ...  # read-only
    kilogramsPerUnit: ClassVar[str] = ...  # read-only
    limit: ClassVar[str] = ...  # read-only
    limit_MultipleApplyTemplate_PhysicsHigh: ClassVar[str] = ...  # read-only
    limit_MultipleApplyTemplate_PhysicsLow: ClassVar[str] = ...  # read-only
    linear: ClassVar[str] = ...  # read-only
    meshSimplification: ClassVar[str] = ...  # read-only
    none: ClassVar[str] = ...  # read-only
    physicsAngularVelocity: ClassVar[str] = ...  # read-only
    physicsApproximation: ClassVar[str] = ...  # read-only
    physicsAxis: ClassVar[str] = ...  # read-only
    physicsBody0: ClassVar[str] = ...  # read-only
    physicsBody1: ClassVar[str] = ...  # read-only
    physicsBreakForce: ClassVar[str] = ...  # read-only
    physicsBreakTorque: ClassVar[str] = ...  # read-only
    physicsCenterOfMass: ClassVar[str] = ...  # read-only
    physicsCollisionEnabled: ClassVar[str] = ...  # read-only
    physicsConeAngle0Limit: ClassVar[str] = ...  # read-only
    physicsConeAngle1Limit: ClassVar[str] = ...  # read-only
    physicsDensity: ClassVar[str] = ...  # read-only
    physicsDiagonalInertia: ClassVar[str] = ...  # read-only
    physicsDynamicFriction: ClassVar[str] = ...  # read-only
    physicsExcludeFromArticulation: ClassVar[str] = ...  # read-only
    physicsFilteredGroups: ClassVar[str] = ...  # read-only
    physicsFilteredPairs: ClassVar[str] = ...  # read-only
    physicsGravityDirection: ClassVar[str] = ...  # read-only
    physicsGravityMagnitude: ClassVar[str] = ...  # read-only
    physicsInvertFilteredGroups: ClassVar[str] = ...  # read-only
    physicsJointEnabled: ClassVar[str] = ...  # read-only
    physicsKinematicEnabled: ClassVar[str] = ...  # read-only
    physicsLocalPos0: ClassVar[str] = ...  # read-only
    physicsLocalPos1: ClassVar[str] = ...  # read-only
    physicsLocalRot0: ClassVar[str] = ...  # read-only
    physicsLocalRot1: ClassVar[str] = ...  # read-only
    physicsLowerLimit: ClassVar[str] = ...  # read-only
    physicsMass: ClassVar[str] = ...  # read-only
    physicsMaxDistance: ClassVar[str] = ...  # read-only
    physicsMergeGroup: ClassVar[str] = ...  # read-only
    physicsMinDistance: ClassVar[str] = ...  # read-only
    physicsPrincipalAxes: ClassVar[str] = ...  # read-only
    physicsRestitution: ClassVar[str] = ...  # read-only
    physicsRigidBodyEnabled: ClassVar[str] = ...  # read-only
    physicsSimulationOwner: ClassVar[str] = ...  # read-only
    physicsStartsAsleep: ClassVar[str] = ...  # read-only
    physicsStaticFriction: ClassVar[str] = ...  # read-only
    physicsUpperLimit: ClassVar[str] = ...  # read-only
    physicsVelocity: ClassVar[str] = ...  # read-only
    rotX: ClassVar[str] = ...  # read-only
    rotY: ClassVar[str] = ...  # read-only
    rotZ: ClassVar[str] = ...  # read-only
    transX: ClassVar[str] = ...  # read-only
    transY: ClassVar[str] = ...  # read-only
    transZ: ClassVar[str] = ...  # read-only
    x: ClassVar[str] = ...  # read-only
    y: ClassVar[str] = ...  # read-only
    z: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...

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

def GetStageKilogramsPerUnit(stage: pxr.Usd.Stage) -> float: ...
def MassUnitsAre(authoredUnits: float, standardUnits: float, epsilon: float = ...) -> bool: ...
def SetStageKilogramsPerUnit(stage: pxr.Usd.Stage, metersPerUnit: float) -> bool: ...
def StageHasAuthoredKilogramsPerUnit(stage: pxr.Usd.Stage) -> bool: ...
