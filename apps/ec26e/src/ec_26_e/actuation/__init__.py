"""公开 MovePlan 运动适配层的稳定契约和真实能力工厂。"""

from ec_26_e.actuation.compiler import compile_move_plan
from ariadne_devices.contracts import MagnetConfig
from ec_26_e.actuation.contracts import (
    ActuationConfig,
    ActuationError,
    ActuationExecutionError,
    ActuationResult,
    ActuationShutdownError,
    ActuationValidationError,
    CompletionIndicator,
    MotionLifecycleState,
    RotationAxis,
    TransferCycle,
)
from ariadne_devices.led import GpiodCompletionLedOutput
from ariadne_devices.magnet import GpiodMagnetOutput

__all__ = [
    "ActuationConfig",
    "ActuationError",
    "ActuationExecutionError",
    "ActuationResult",
    "ActuationShutdownError",
    "ActuationValidationError",
    "CompletionIndicator",
    "GpiodCompletionLedOutput",
    "GpiodMagnetOutput",
    "MagnetConfig",
    "MotionLifecycleState",
    "RotationAxis",
    "TransferCycle",
    "compile_move_plan",
]
