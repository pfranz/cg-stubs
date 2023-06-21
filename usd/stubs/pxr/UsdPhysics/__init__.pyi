import Boost.Python
import pxr.Tf
from typing import Any, ClassVar, overload

class ArticulationRootAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> ArticulationRootAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> ArticulationRootAPI: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class CollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> CollisionAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateCollisionEnabledAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSimulationOwnerRel(self) -> pxr.Usd.Relationship: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> CollisionAPI: ...
    def GetCollisionEnabledAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    def GetSimulationOwnerRel(self) -> pxr.Usd.Relationship: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class CollisionGroup(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def ComputeCollisionGroupTable(cls, stage: pxr.Usd.Stage) -> CollisionGroupTable: ...
    def CreateFilteredGroupsRel(self) -> pxr.Usd.Relationship: ...
    def CreateInvertFilteredGroupsAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateMergeGroupNameAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> CollisionGroup: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> CollisionGroup: ...
    def GetCollidersCollectionAPI(self) -> pxr.Usd.CollectionAPI: ...
    def GetFilteredGroupsRel(self) -> pxr.Usd.Relationship: ...
    def GetInvertFilteredGroupsAttr(self) -> pxr.Usd.Attribute: ...
    def GetMergeGroupNameAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class CollisionGroupTable(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetGroups(self) -> list: ...
    def IsCollisionEnabled(self, arg2: object, arg3: object) -> bool: ...
    def __reduce__(self) -> Any: ...

class DistanceJoint(Joint):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateMaxDistanceAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateMinDistanceAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> DistanceJoint: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> DistanceJoint: ...
    def GetMaxDistanceAttr(self) -> pxr.Usd.Attribute: ...
    def GetMinDistanceAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class DriveAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Usd.Prim, arg3: object) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Usd.SchemaBase, arg3: object) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim, name: object) -> DriveAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim, name: object) -> _CanApplyResult: ...
    def CreateDampingAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateMaxForceAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateStiffnessAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateTargetPositionAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateTargetVelocityAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateTypeAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @overload
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> DriveAPI: ...
    @overload
    @classmethod
    def Get(cls, prim: pxr.Usd.Prim, name: object) -> DriveAPI: ...
    @classmethod
    def GetAll(cls, prim: pxr.Usd.Prim) -> list: ...
    def GetDampingAttr(self) -> pxr.Usd.Attribute: ...
    def GetMaxForceAttr(self) -> pxr.Usd.Attribute: ...
    @overload
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @overload
    @classmethod
    def GetSchemaAttributeNames(cls, arg1: bool, includeInherited: object) -> list: ...
    def GetStiffnessAttr(self) -> pxr.Usd.Attribute: ...
    def GetTargetPositionAttr(self) -> pxr.Usd.Attribute: ...
    def GetTargetVelocityAttr(self) -> pxr.Usd.Attribute: ...
    def GetTypeAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def IsPhysicsDriveAPIPath(cls, arg1: pxr.Sdf.Path) -> bool: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class FilteredPairsAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> FilteredPairsAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateFilteredPairsRel(self) -> pxr.Usd.Relationship: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> FilteredPairsAPI: ...
    def GetFilteredPairsRel(self) -> pxr.Usd.Relationship: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class FixedJoint(Joint):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> FixedJoint: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> FixedJoint: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class Joint(pxr.UsdGeom.Imageable):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateBody0Rel(self) -> pxr.Usd.Relationship: ...
    def CreateBody1Rel(self) -> pxr.Usd.Relationship: ...
    def CreateBreakForceAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateBreakTorqueAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateCollisionEnabledAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateExcludeFromArticulationAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateJointEnabledAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLocalPos0Attr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLocalPos1Attr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLocalRot0Attr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLocalRot1Attr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Joint: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Joint: ...
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
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class LimitAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Usd.Prim, arg3: object) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Usd.SchemaBase, arg3: object) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim, name: object) -> LimitAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim, name: object) -> _CanApplyResult: ...
    def CreateHighAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLowAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @overload
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> LimitAPI: ...
    @overload
    @classmethod
    def Get(cls, prim: pxr.Usd.Prim, name: object) -> LimitAPI: ...
    @classmethod
    def GetAll(cls, prim: pxr.Usd.Prim) -> list: ...
    def GetHighAttr(self) -> pxr.Usd.Attribute: ...
    def GetLowAttr(self) -> pxr.Usd.Attribute: ...
    @overload
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @overload
    @classmethod
    def GetSchemaAttributeNames(cls, arg1: bool, includeInherited: object) -> list: ...
    @classmethod
    def IsPhysicsLimitAPIPath(cls, arg1: pxr.Sdf.Path) -> bool: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class MassAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> MassAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateCenterOfMassAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDensityAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDiagonalInertiaAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateMassAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreatePrincipalAxesAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> MassAPI: ...
    def GetCenterOfMassAttr(self) -> pxr.Usd.Attribute: ...
    def GetDensityAttr(self) -> pxr.Usd.Attribute: ...
    def GetDiagonalInertiaAttr(self) -> pxr.Usd.Attribute: ...
    def GetMassAttr(self) -> pxr.Usd.Attribute: ...
    def GetPrincipalAxesAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class MassUnits(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def grams(self) -> Any: ...
    @property
    def kilograms(self) -> Any: ...
    @property
    def slugs(self) -> Any: ...

class MaterialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> MaterialAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateDensityAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDynamicFrictionAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateRestitutionAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateStaticFrictionAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> MaterialAPI: ...
    def GetDensityAttr(self) -> pxr.Usd.Attribute: ...
    def GetDynamicFrictionAttr(self) -> pxr.Usd.Attribute: ...
    def GetRestitutionAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    def GetStaticFrictionAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class MeshCollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> MeshCollisionAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateApproximationAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> MeshCollisionAPI: ...
    def GetApproximationAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class PrismaticJoint(Joint):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateAxisAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLowerLimitAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateUpperLimitAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> PrismaticJoint: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> PrismaticJoint: ...
    def GetAxisAttr(self) -> pxr.Usd.Attribute: ...
    def GetLowerLimitAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    def GetUpperLimitAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class RevoluteJoint(Joint):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateAxisAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLowerLimitAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateUpperLimitAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> RevoluteJoint: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> RevoluteJoint: ...
    def GetAxisAttr(self) -> pxr.Usd.Attribute: ...
    def GetLowerLimitAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    def GetUpperLimitAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class RigidBodyAPI(pxr.Usd.APISchemaBase):
    class MassInformation(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        centerOfMass: Any
        inertia: Any
        localPos: Any
        localRot: Any
        volume: Any
        def __init__(self) -> None: ...
        def __reduce__(self) -> Any: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> RigidBodyAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def ComputeMassProperties(self, arg2: object) -> tuple: ...
    def CreateAngularVelocityAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateKinematicEnabledAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateRigidBodyEnabledAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSimulationOwnerRel(self) -> pxr.Usd.Relationship: ...
    def CreateStartsAsleepAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateVelocityAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> RigidBodyAPI: ...
    def GetAngularVelocityAttr(self) -> pxr.Usd.Attribute: ...
    def GetKinematicEnabledAttr(self) -> pxr.Usd.Attribute: ...
    def GetRigidBodyEnabledAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    def GetSimulationOwnerRel(self) -> pxr.Usd.Relationship: ...
    def GetStartsAsleepAttr(self) -> pxr.Usd.Attribute: ...
    def GetVelocityAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class Scene(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateGravityDirectionAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateGravityMagnitudeAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Scene: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Scene: ...
    def GetGravityDirectionAttr(self) -> pxr.Usd.Attribute: ...
    def GetGravityMagnitudeAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class SphericalJoint(Joint):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateAxisAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateConeAngle0LimitAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateConeAngle1LimitAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> SphericalJoint: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> SphericalJoint: ...
    def GetAxisAttr(self) -> pxr.Usd.Attribute: ...
    def GetConeAngle0LimitAttr(self) -> pxr.Usd.Attribute: ...
    def GetConeAngle1LimitAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class Tokens(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def PhysicsArticulationRootAPI(self) -> Any: ...
    @property
    def PhysicsCollisionAPI(self) -> Any: ...
    @property
    def PhysicsCollisionGroup(self) -> Any: ...
    @property
    def PhysicsDistanceJoint(self) -> Any: ...
    @property
    def PhysicsDriveAPI(self) -> Any: ...
    @property
    def PhysicsFilteredPairsAPI(self) -> Any: ...
    @property
    def PhysicsFixedJoint(self) -> Any: ...
    @property
    def PhysicsJoint(self) -> Any: ...
    @property
    def PhysicsLimitAPI(self) -> Any: ...
    @property
    def PhysicsMassAPI(self) -> Any: ...
    @property
    def PhysicsMaterialAPI(self) -> Any: ...
    @property
    def PhysicsMeshCollisionAPI(self) -> Any: ...
    @property
    def PhysicsPrismaticJoint(self) -> Any: ...
    @property
    def PhysicsRevoluteJoint(self) -> Any: ...
    @property
    def PhysicsRigidBodyAPI(self) -> Any: ...
    @property
    def PhysicsScene(self) -> Any: ...
    @property
    def PhysicsSphericalJoint(self) -> Any: ...
    @property
    def acceleration(self) -> Any: ...
    @property
    def angular(self) -> Any: ...
    @property
    def boundingCube(self) -> Any: ...
    @property
    def boundingSphere(self) -> Any: ...
    @property
    def colliders(self) -> Any: ...
    @property
    def convexDecomposition(self) -> Any: ...
    @property
    def convexHull(self) -> Any: ...
    @property
    def distance(self) -> Any: ...
    @property
    def drive(self) -> Any: ...
    @property
    def drive_MultipleApplyTemplate_PhysicsDamping(self) -> Any: ...
    @property
    def drive_MultipleApplyTemplate_PhysicsMaxForce(self) -> Any: ...
    @property
    def drive_MultipleApplyTemplate_PhysicsStiffness(self) -> Any: ...
    @property
    def drive_MultipleApplyTemplate_PhysicsTargetPosition(self) -> Any: ...
    @property
    def drive_MultipleApplyTemplate_PhysicsTargetVelocity(self) -> Any: ...
    @property
    def drive_MultipleApplyTemplate_PhysicsType(self) -> Any: ...
    @property
    def force(self) -> Any: ...
    @property
    def kilogramsPerUnit(self) -> Any: ...
    @property
    def limit(self) -> Any: ...
    @property
    def limit_MultipleApplyTemplate_PhysicsHigh(self) -> Any: ...
    @property
    def limit_MultipleApplyTemplate_PhysicsLow(self) -> Any: ...
    @property
    def linear(self) -> Any: ...
    @property
    def meshSimplification(self) -> Any: ...
    @property
    def none(self) -> Any: ...
    @property
    def physicsAngularVelocity(self) -> Any: ...
    @property
    def physicsApproximation(self) -> Any: ...
    @property
    def physicsAxis(self) -> Any: ...
    @property
    def physicsBody0(self) -> Any: ...
    @property
    def physicsBody1(self) -> Any: ...
    @property
    def physicsBreakForce(self) -> Any: ...
    @property
    def physicsBreakTorque(self) -> Any: ...
    @property
    def physicsCenterOfMass(self) -> Any: ...
    @property
    def physicsCollisionEnabled(self) -> Any: ...
    @property
    def physicsConeAngle0Limit(self) -> Any: ...
    @property
    def physicsConeAngle1Limit(self) -> Any: ...
    @property
    def physicsDensity(self) -> Any: ...
    @property
    def physicsDiagonalInertia(self) -> Any: ...
    @property
    def physicsDynamicFriction(self) -> Any: ...
    @property
    def physicsExcludeFromArticulation(self) -> Any: ...
    @property
    def physicsFilteredGroups(self) -> Any: ...
    @property
    def physicsFilteredPairs(self) -> Any: ...
    @property
    def physicsGravityDirection(self) -> Any: ...
    @property
    def physicsGravityMagnitude(self) -> Any: ...
    @property
    def physicsInvertFilteredGroups(self) -> Any: ...
    @property
    def physicsJointEnabled(self) -> Any: ...
    @property
    def physicsKinematicEnabled(self) -> Any: ...
    @property
    def physicsLocalPos0(self) -> Any: ...
    @property
    def physicsLocalPos1(self) -> Any: ...
    @property
    def physicsLocalRot0(self) -> Any: ...
    @property
    def physicsLocalRot1(self) -> Any: ...
    @property
    def physicsLowerLimit(self) -> Any: ...
    @property
    def physicsMass(self) -> Any: ...
    @property
    def physicsMaxDistance(self) -> Any: ...
    @property
    def physicsMergeGroup(self) -> Any: ...
    @property
    def physicsMinDistance(self) -> Any: ...
    @property
    def physicsPrincipalAxes(self) -> Any: ...
    @property
    def physicsRestitution(self) -> Any: ...
    @property
    def physicsRigidBodyEnabled(self) -> Any: ...
    @property
    def physicsSimulationOwner(self) -> Any: ...
    @property
    def physicsStartsAsleep(self) -> Any: ...
    @property
    def physicsStaticFriction(self) -> Any: ...
    @property
    def physicsUpperLimit(self) -> Any: ...
    @property
    def physicsVelocity(self) -> Any: ...
    @property
    def rotX(self) -> Any: ...
    @property
    def rotY(self) -> Any: ...
    @property
    def rotZ(self) -> Any: ...
    @property
    def transX(self) -> Any: ...
    @property
    def transY(self) -> Any: ...
    @property
    def transZ(self) -> Any: ...
    @property
    def x(self) -> Any: ...
    @property
    def y(self) -> Any: ...
    @property
    def z(self) -> Any: ...

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

def GetStageKilogramsPerUnit(stage: pxr.Usd.Stage) -> float: ...
def MassUnitsAre(authoredUnits: float, standardUnits: float, epsilon: float = ...) -> bool: ...
def SetStageKilogramsPerUnit(stage: pxr.Usd.Stage, metersPerUnit: float) -> bool: ...
def StageHasAuthoredKilogramsPerUnit(stage: pxr.Usd.Stage) -> bool: ...