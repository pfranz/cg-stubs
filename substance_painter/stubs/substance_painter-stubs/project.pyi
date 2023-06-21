import enum
from . import event as event
from _typeshed import Incomplete
from typing import Any, Callable, List, Optional, Tuple

from _substance_painter.project import ProjectSaveMode as ProjectSaveMode
from _substance_painter.project import NormalMapFormat as NormalMapFormat
from _substance_painter.project import TangentSpace as TangentSpace
from _substance_painter.project import ProjectWorkflow as ProjectWorkflow

class Settings:
    default_save_path: str
    normal_map_format: NormalMapFormat
    tangent_space_mode: TangentSpace
    project_workflow: ProjectWorkflow
    export_path: str
    default_texture_resolution: int
    import_cameras: bool
    mesh_unit_scale: float
    def __init__(self, default_save_path, normal_map_format, tangent_space_mode, project_workflow, export_path, default_texture_resolution, import_cameras, mesh_unit_scale) -> None: ...

class MeshReloadingSettings:
    import_cameras: bool
    preserve_strokes: bool
    def __init__(self, import_cameras, preserve_strokes) -> None: ...

class _ActionLock:
    def __enter__(self): ...
    def __exit__(self, err_type, err_value, traceback) -> None: ...

def name() -> Optional[str]: ...
def file_path() -> Optional[str]: ...
def close() -> None: ...
def open(project_file_path: str) -> None: ...
def is_open() -> bool: ...
def needs_saving() -> bool: ...
def is_in_edition_state() -> bool: ...
def is_busy() -> bool: ...
def execute_when_not_busy(callback: Callable[[], None]) -> None: ...
def save_as(project_file_path: str, mode: ProjectSaveMode = ...) -> None: ...
def save(mode: ProjectSaveMode = ...) -> None: ...
def save_as_copy(backup_file_path: str, mode: ProjectSaveMode = ...) -> None: ...
def save_as_template(template_file_path: str, texture_set_name: str) -> ProjectSaveMode: ...
def create(mesh_file_path: str, mesh_map_file_paths: List[str] = ..., template_file_path: str = ..., settings: Settings = ...): ...
def last_imported_mesh_path() -> str: ...
def last_saved_substance_painter_version() -> Optional[Tuple[int, int, int]]: ...

class ReloadMeshStatus(enum.Enum):
    SUCCESS: int
    ERROR: int

def reload_mesh(mesh_file_path: str, settings: MeshReloadingSettings, loading_status_cb: Callable[[ReloadMeshStatus], Any]): ...

class Metadata:
    def __init__(self, context: str) -> None: ...
    def list(self) -> list: ...
    def get(self, key: str): ...
    def set(self, key: str, value): ...