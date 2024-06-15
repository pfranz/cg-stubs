# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from _typeshed import Incomplete
from typing import Set, Tuple

AnisotropicParamHints: dict
BloomAmountParamHints: dict
BloomEnableParamHints: dict
BloomGroupParamHints: dict
BloomModeParamHints: dict
BloomThresholdParamHints: dict
BorderExtendParamHints: dict
BorderOverscanParamHints: dict
ClampOutputParamHints: dict
DownFilterParamHints: dict
FilterParamHints: dict
GroupFilterParamHints: dict
HighlightCompensationParamHints: dict
MotionBlurEnableParamHints: dict
MotionBlurGroupParamHints: dict
MotionBlurNumSamplesParamHints: dict
MotionBlurOnlyApplyMotionParamHints: dict
MotionBlurShutterParamHints: dict
PremultiplyToggleHints: dict
UpFilterParamHints: dict

def AddCommon2DToNodeHints(d): ...
def AddDictToNodeHints(origHints, additionalHints, prefix): ...
def GetAngleNumberDict(**kwargs): ...
def GetAspectRatioNumberDict(**kwargs): ...
def GetBoundsParamDict(paramName): ...
def GetCameraLensMmNumberDict(**kwargs): ...
def GetCapsuleRgbaDict(exclusive: bool = ..., help: Incomplete | None = ..., label: Incomplete | None = ...): ...
def GetChannelCapsuleColor(channel): ...
def GetCineonOffsetNumberDict(**kwargs): ...
def GetContrastNumberDict(**kwargs): ...
def GetExposureNumberDict(**kwargs): ...
def GetFgBgCombinerStringDict(**kwargs): ...
def GetFilmbackStringDict(**kwargs): ...
def GetGainNumberDict(**kwargs): ...
def GetGammaNumberDict(**kwargs): ...
def GetHueAngleOffsetNumberDict(**kwargs): ...
def GetNormalizedCenterNumberDict(**kwargs): ...
def GetNormalizedNumberDict(**kwargs): ...
def GetOffsetNumberDict(**kwargs): ...
def GetPivotNumberDict(**kwargs): ...
def GetPixelNumberDict(**kwargs): ...
def GetPolygonSidesDict(**kwargs): ...
def GetPositivePixelNumberDict(**kwargs): ...
def GetSaturationNumberDict(**kwargs): ...
def GetSmallPositivePixelNumberDict(**kwargs): ...