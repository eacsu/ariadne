"""公开蓝色 A4 工作区定位和透视校正接口。"""

from ariadne_vision.resize.contracts import ResizeConfig, ResizeResult
from ariadne_vision.resize.resizer import Resize

__all__ = ["Resize", "ResizeConfig", "ResizeResult"]
