import PySide2.QtCore
import _typeshed
import collections
import shiboken2
import typing
T = typing.TypeVar('T')
import typing_extensions

class QScxmlCompiler(shiboken2.Object):
    class Loader(shiboken2.Object):
        def __init__(self) -> None: ...
        def load(self, name: str, baseDir: str) -> typing.Tuple[PySide2.QtCore.QByteArray, typing.List[str]]: ...
    def __init__(self, xmlReader: PySide2.QtCore.QXmlStreamReader) -> None: ...
    def compile(self) -> QScxmlStateMachine: ...
    def errors(self) -> typing.List[QScxmlError]: ...
    def fileName(self) -> str: ...
    def loader(self) -> QScxmlCompiler.Loader: ...
    def setFileName(self, fileName: str) -> None: ...
    def setLoader(self, newLoader: QScxmlCompiler.Loader) -> None: ...

class QScxmlCppDataModel(QScxmlDataModel):
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, parent: PySide2.QtCore.QObject | None = ..., destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ...) -> None: ...
    def evaluateAssignment(self, id: int) -> bool: ...
    def evaluateForeach(self, id: int, body: QScxmlDataModel.ForeachLoopBody) -> bool: ...
    def evaluateInitialization(self, id: int) -> bool: ...
    def hasScxmlProperty(self, name: str) -> bool: ...
    def inState(self, stateName: str) -> bool: ...
    def scxmlEvent(self) -> QScxmlEvent: ...
    def scxmlProperty(self, name: str) -> typing.Any: ...
    def setScxmlEvent(self, scxmlEvent: QScxmlEvent) -> None: ...
    def setScxmlProperty(self, name: str, value: typing.Any, context: str) -> bool: ...
    def setup(self, initialDataValues: typing.Dict[str, typing.Any]) -> bool: ...

class QScxmlDataModel(PySide2.QtCore.QObject):
    class ForeachLoopBody(shiboken2.Object):
        def __init__(self) -> None: ...
        def run(self) -> bool: ...
    stateMachineChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, parent: PySide2.QtCore.QObject | None = ..., destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ...) -> None: ...
    def evaluateAssignment(self, id: int) -> bool: ...
    def evaluateForeach(self, id: int, body: QScxmlDataModel.ForeachLoopBody) -> bool: ...
    def evaluateInitialization(self, id: int) -> bool: ...
    def evaluateToBool(self, id: int) -> typing.Tuple[bool, bool]: ...
    def evaluateToString(self, id: int) -> typing.Tuple[str, bool]: ...
    def evaluateToVariant(self, id: int) -> typing.Tuple[typing.Any, bool]: ...
    def evaluateToVoid(self, id: int) -> bool: ...
    def hasScxmlProperty(self, name: str) -> bool: ...
    def scxmlProperty(self, name: str) -> typing.Any: ...
    def setScxmlEvent(self, event: QScxmlEvent) -> None: ...
    def setScxmlProperty(self, name: str, value: typing.Any, context: str) -> bool: ...
    def setStateMachine(self, stateMachine: QScxmlStateMachine) -> None: ...
    def setup(self, initialDataValues: typing.Dict[str, typing.Any]) -> bool: ...
    def stateMachine(self) -> QScxmlStateMachine: ...

class QScxmlDynamicScxmlServiceFactory(QScxmlInvokableServiceFactory):
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, invokeInfo: QScxmlExecutableContent.InvokeInfo, names: typing.List[int], parameters: typing.List[QScxmlExecutableContent.ParameterInfo], parent: PySide2.QtCore.QObject | None = ..., destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ...) -> None: ...
    def invoke(self, parentStateMachine: QScxmlStateMachine) -> QScxmlInvokableService: ...

class QScxmlEcmaScriptDataModel(QScxmlDataModel):
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, parent: PySide2.QtCore.QObject | None = ..., destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ..., stateMachine: typing.Any = ..., stateMachineChanged: typing.Callable = ...) -> None: ...
    def evaluateAssignment(self, id: int) -> bool: ...
    def evaluateForeach(self, id: int, body: QScxmlDataModel.ForeachLoopBody) -> bool: ...
    def evaluateInitialization(self, id: int) -> bool: ...
    def evaluateToBool(self, id: int) -> typing.Tuple[bool, bool]: ...
    def evaluateToString(self, id: int) -> typing.Tuple[str, bool]: ...
    def evaluateToVariant(self, id: int) -> typing.Tuple[typing.Any, bool]: ...
    def evaluateToVoid(self, id: int) -> bool: ...
    def hasScxmlProperty(self, name: str) -> bool: ...
    def scxmlProperty(self, name: str) -> typing.Any: ...
    def setScxmlEvent(self, event: QScxmlEvent) -> None: ...
    def setScxmlProperty(self, name: str, value: typing.Any, context: str) -> bool: ...
    def setup(self, initialDataValues: typing.Dict[str, typing.Any]) -> bool: ...

class QScxmlError(shiboken2.Object):
    @typing.overload
    def __init__(self, fileName: str, line: int, column: int, description: str) -> None: ...
    @typing.overload
    def __init__(self, arg__1: QScxmlError) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def column(self) -> int: ...
    def description(self) -> str: ...
    def fileName(self) -> str: ...
    def isValid(self) -> bool: ...
    def line(self) -> int: ...
    def toString(self) -> str: ...
    def __copy__(self) -> None: ...

class QScxmlEvent(shiboken2.Object):
    class EventType:
        ExternalEvent: typing.ClassVar[QScxmlEvent.EventType] = ...
        InternalEvent: typing.ClassVar[QScxmlEvent.EventType] = ...
        PlatformEvent: typing.ClassVar[QScxmlEvent.EventType] = ...
        values: typing.ClassVar[dict] = ...
        name: _typeshed.Incomplete
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QScxmlEvent.EventType: ...
        def __and__(self, other: typing.SupportsInt) -> QScxmlEvent.EventType: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QScxmlEvent.EventType: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QScxmlEvent.EventType: ...
        def __pos__(self): ...
        def __radd__(self, other: typing.SupportsInt) -> QScxmlEvent.EventType: ...
        def __rand__(self, other: typing.SupportsInt) -> QScxmlEvent.EventType: ...
        def __rmul__(self, other: typing.SupportsInt) -> QScxmlEvent.EventType: ...
        def __ror__(self, other: typing.SupportsInt) -> QScxmlEvent.EventType: ...
        def __rsub__(self, other: typing.SupportsInt) -> QScxmlEvent.EventType: ...
        def __rxor__(self, other: typing.SupportsInt) -> QScxmlEvent.EventType: ...
        def __sub__(self, other: typing.SupportsInt) -> QScxmlEvent.EventType: ...
        def __xor__(self, other: typing.SupportsInt) -> QScxmlEvent.EventType: ...
    ExternalEvent: typing.ClassVar[QScxmlEvent.EventType] = ...
    InternalEvent: typing.ClassVar[QScxmlEvent.EventType] = ...
    PlatformEvent: typing.ClassVar[QScxmlEvent.EventType] = ...
    @typing.overload
    def __init__(self, other: QScxmlEvent) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def clear(self) -> None: ...
    def data(self) -> typing.Any: ...
    def delay(self) -> int: ...
    def errorMessage(self) -> str: ...
    def eventType(self) -> QScxmlEvent.EventType: ...
    def invokeId(self) -> str: ...
    def isErrorEvent(self) -> bool: ...
    def name(self) -> str: ...
    def origin(self) -> str: ...
    def originType(self) -> str: ...
    def scxmlType(self) -> str: ...
    def sendId(self) -> str: ...
    def setData(self, data: typing.Any) -> None: ...
    def setDelay(self, delayInMiliSecs: int) -> None: ...
    def setErrorMessage(self, message: str) -> None: ...
    def setEventType(self, type: QScxmlEvent.EventType) -> None: ...
    def setInvokeId(self, invokeId: str) -> None: ...
    def setName(self, name: str) -> None: ...
    def setOrigin(self, origin: str) -> None: ...
    def setOriginType(self, originType: str) -> None: ...
    def setSendId(self, sendId: str) -> None: ...

class QScxmlExecutableContent(shiboken2.Object):
    class AssignmentInfo(shiboken2.Object):
        context: _typeshed.Incomplete
        dest: _typeshed.Incomplete
        expr: _typeshed.Incomplete
        @typing.overload
        def __init__(self, AssignmentInfo: QScxmlExecutableContent.AssignmentInfo) -> None: ...
        @typing.overload
        def __init__(self) -> None: ...
        def __copy__(self) -> None: ...

    class EvaluatorInfo(shiboken2.Object):
        context: _typeshed.Incomplete
        expr: _typeshed.Incomplete
        @typing.overload
        def __init__(self, EvaluatorInfo: QScxmlExecutableContent.EvaluatorInfo) -> None: ...
        @typing.overload
        def __init__(self) -> None: ...
        def __copy__(self) -> None: ...

    class ForeachInfo(shiboken2.Object):
        array: _typeshed.Incomplete
        context: _typeshed.Incomplete
        index: _typeshed.Incomplete
        item: _typeshed.Incomplete
        @typing.overload
        def __init__(self, ForeachInfo: QScxmlExecutableContent.ForeachInfo) -> None: ...
        @typing.overload
        def __init__(self) -> None: ...
        def __copy__(self) -> None: ...

    class InvokeInfo(shiboken2.Object):
        autoforward: _typeshed.Incomplete
        context: _typeshed.Incomplete
        expr: _typeshed.Incomplete
        finalize: _typeshed.Incomplete
        id: _typeshed.Incomplete
        location: _typeshed.Incomplete
        prefix: _typeshed.Incomplete
        @typing.overload
        def __init__(self, InvokeInfo: QScxmlExecutableContent.InvokeInfo) -> None: ...
        @typing.overload
        def __init__(self) -> None: ...
        def __copy__(self) -> None: ...

    class ParameterInfo(shiboken2.Object):
        expr: _typeshed.Incomplete
        location: _typeshed.Incomplete
        name: _typeshed.Incomplete
        @typing.overload
        def __init__(self, ParameterInfo: QScxmlExecutableContent.ParameterInfo) -> None: ...
        @typing.overload
        def __init__(self) -> None: ...
        def __copy__(self) -> None: ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...

class QScxmlInvokableService(PySide2.QtCore.QObject):
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, parentStateMachine: QScxmlStateMachine, parent: QScxmlInvokableServiceFactory, destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ...) -> None: ...
    def id(self) -> str: ...
    def name(self) -> str: ...
    def parentStateMachine(self) -> QScxmlStateMachine: ...
    def postEvent(self, event: QScxmlEvent) -> None: ...
    def start(self) -> bool: ...

class QScxmlInvokableServiceFactory(PySide2.QtCore.QObject):
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, invokeInfo: QScxmlExecutableContent.InvokeInfo, names: typing.List[int], parameters: typing.List[QScxmlExecutableContent.ParameterInfo], parent: PySide2.QtCore.QObject | None = ..., destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ...) -> None: ...
    def invoke(self, parentStateMachine: QScxmlStateMachine) -> QScxmlInvokableService: ...
    def invokeInfo(self) -> QScxmlExecutableContent.InvokeInfo: ...
    def names(self) -> typing.List[int]: ...
    def parameters(self) -> typing.List[QScxmlExecutableContent.ParameterInfo]: ...

class QScxmlNullDataModel(QScxmlDataModel):
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, parent: PySide2.QtCore.QObject | None = ..., destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ..., stateMachine: typing.Any = ..., stateMachineChanged: typing.Callable = ...) -> None: ...
    def evaluateAssignment(self, id: int) -> bool: ...
    def evaluateForeach(self, id: int, body: QScxmlDataModel.ForeachLoopBody) -> bool: ...
    def evaluateInitialization(self, id: int) -> bool: ...
    def evaluateToBool(self, id: int) -> typing.Tuple[bool, bool]: ...
    def evaluateToString(self, id: int) -> typing.Tuple[str, bool]: ...
    def evaluateToVariant(self, id: int) -> typing.Tuple[typing.Any, bool]: ...
    def evaluateToVoid(self, id: int) -> bool: ...
    def hasScxmlProperty(self, name: str) -> bool: ...
    def scxmlProperty(self, name: str) -> typing.Any: ...
    def setScxmlEvent(self, event: QScxmlEvent) -> None: ...
    def setScxmlProperty(self, name: str, value: typing.Any, context: str) -> bool: ...
    def setup(self, initialDataValues: typing.Dict[str, typing.Any]) -> bool: ...

class QScxmlStateMachine(PySide2.QtCore.QObject):
    dataModelChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    finished: typing.ClassVar[PySide2.QtCore.Signal] = ...
    initialValuesChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    initializedChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    invokedServicesChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    loaderChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    log: typing.ClassVar[PySide2.QtCore.Signal] = ...
    reachedStableState: typing.ClassVar[PySide2.QtCore.Signal] = ...
    runningChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    tableDataChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    def __init__(self, metaObject: PySide2.QtCore.QMetaObject, parent: PySide2.QtCore.QObject | None = ..., destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ...) -> None: ...
    def activeStateNames(self, compress: bool = ...) -> typing.List[str]: ...
    def cancelDelayedEvent(self, sendId: str) -> None: ...
    def connectToEvent(self, scxmlEventSpec: str, receiver: PySide2.QtCore.QObject, method: bytes, type: PySide2.QtCore.Qt.ConnectionType = ...) -> PySide2.QtCore.QMetaObject.Connection: ...
    def connectToState(self, scxmlStateName: str, receiver: PySide2.QtCore.QObject, method: bytes, type: PySide2.QtCore.Qt.ConnectionType = ...) -> PySide2.QtCore.QMetaObject.Connection: ...
    def dataModel(self) -> QScxmlDataModel: ...
    @staticmethod
    def fromData(data: PySide2.QtCore.QIODevice, fileName: str = ...) -> QScxmlStateMachine: ...
    @staticmethod
    def fromFile(fileName: str) -> QScxmlStateMachine: ...
    def init(self) -> bool: ...
    def initialValues(self) -> typing.Dict[str, typing.Any]: ...
    def invokedServices(self) -> typing.List[QScxmlInvokableService]: ...
    @typing.overload
    def isActive(self, stateIndex: int) -> bool: ...
    @typing.overload
    def isActive(self, scxmlStateName: str) -> bool: ...
    def isDispatchableTarget(self, target: str) -> bool: ...
    def isInitialized(self) -> bool: ...
    def isInvoked(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def loader(self) -> QScxmlCompiler.Loader: ...
    def name(self) -> str: ...
    def parseErrors(self) -> typing.List[QScxmlError]: ...
    def sessionId(self) -> str: ...
    def setDataModel(self, model: QScxmlDataModel) -> None: ...
    def setInitialValues(self, initialValues: typing.Dict[str, typing.Any]) -> None: ...
    def setLoader(self, loader: QScxmlCompiler.Loader) -> None: ...
    def setRunning(self, running: bool) -> None: ...
    def setTableData(self, tableData: QScxmlTableData) -> None: ...
    def start(self) -> None: ...
    def stateNames(self, compress: bool = ...) -> typing.List[str]: ...
    def stop(self) -> None: ...
    @typing.overload
    def submitEvent(self, eventName: str, data: typing.Any) -> None: ...
    @typing.overload
    def submitEvent(self, eventName: str) -> None: ...
    @typing.overload
    def submitEvent(self, event: QScxmlEvent) -> None: ...
    def tableData(self) -> QScxmlTableData: ...

class QScxmlStaticScxmlServiceFactory(QScxmlInvokableServiceFactory):
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, metaObject: PySide2.QtCore.QMetaObject, invokeInfo: QScxmlExecutableContent.InvokeInfo, nameList: typing.List[int], parameters: typing.List[QScxmlExecutableContent.ParameterInfo], parent: PySide2.QtCore.QObject | None = ..., destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ...) -> None: ...
    def invoke(self, parentStateMachine: QScxmlStateMachine) -> QScxmlInvokableService: ...

class QScxmlTableData(shiboken2.Object):
    def __init__(self) -> None: ...
    def assignmentInfo(self, assignmentId: int) -> QScxmlExecutableContent.AssignmentInfo: ...
    def dataNames(self) -> typing.Tuple[typing.List[int], int]: ...
    def evaluatorInfo(self, evaluatorId: int) -> QScxmlExecutableContent.EvaluatorInfo: ...
    def foreachInfo(self, foreachId: int) -> QScxmlExecutableContent.ForeachInfo: ...
    def initialSetup(self) -> int: ...
    def instructions(self) -> typing.List[int]: ...
    def name(self) -> str: ...
    def serviceFactory(self, id: int) -> QScxmlInvokableServiceFactory: ...
    def stateMachineTable(self) -> typing.List[int]: ...
    def string(self, id: int) -> str: ...
