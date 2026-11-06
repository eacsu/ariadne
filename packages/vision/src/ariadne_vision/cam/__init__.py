"""公开 FFmpeg 相机采集模块的稳定契约与实现。"""

from ariadne_vision.cam.contracts import (
    CameraCaptureError,
    CameraConfig,
    CameraFrame,
    CameraSource,
    CameraTimeoutError,
)
from ariadne_vision.cam.ffmpeg_camera import FFmpegCamera

__all__ = [
    "CameraCaptureError",
    "CameraConfig",
    "CameraFrame",
    "CameraSource",
    "CameraTimeoutError",
    "FFmpegCamera",
]
