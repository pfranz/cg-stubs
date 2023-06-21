# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Version.Registry as Registry
import NodegraphAPI.Xio as Xio

localVersion: tuple

def UpgradeGenericCreate(node, nodeType): ...
def UpgradeKstdAssign(node, nodeType): ...
def UpgradeKstdBake(node, nodeType): ...
def UpgradeKstdDetective(node, nodeType): ...
def UpgradeKstdLightAndConstraintManager(node, nodeType): ...
def UpgradeKstdMaterialsOut(node, nodeType): ...
def UpgradeKstdMultiBake(node, nodeType): ...
def UpgradeKstdResolve(node, nodeType): ...
def UpgradeKstdRootAssign(node, nodeType): ...
def UpgradeKstdRootAssignBaseType(node, nodeType): ...
def UpgradeKstd_In(node, nodeType): ...
def UpgradeStickyNote(node, nodeType): ...
def update(document): ...