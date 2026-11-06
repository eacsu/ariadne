"""公开唯一的 A4 校正、YOLO语义门控、传统精修和稳定检测接口。"""

from ariadne_vision.contracts import (
    Detect1Config,
    Detect1Result,
    NativeTiming,
    PieceDetection,
    SegInstance,
    StableVisionConfig,
    VisionConfig,
    VisionDiagnostics,
)
from ariadne_vision.detector import VisionDetector
from ariadne_vision.factory import create_production_detector
from ariadne_vision.npu import NpuYolo11SegInferencer
from ariadne_vision.resize import Resize, ResizeConfig, ResizeResult
from ariadne_vision.stabilizer import StableVisionDetector

__all__ = [
    "Detect1Config",
    "Detect1Result",
    "NativeTiming",
    "NpuYolo11SegInferencer",
    "PieceDetection",
    "Resize",
    "ResizeConfig",
    "ResizeResult",
    "SegInstance",
    "StableVisionConfig",
    "StableVisionDetector",
    "VisionConfig",
    "VisionDetector",
    "VisionDiagnostics",
    "create_production_detector",
]
