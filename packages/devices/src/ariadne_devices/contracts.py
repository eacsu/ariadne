from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True, slots=True)
class MagnetConfig:
    """描述 Linux GPIO 字符设备中的磁铁高电平输出。"""

    chip_path: Path = Path("/dev/gpiochip0")
    line_offset: int = -1

    def __post_init__(self) -> None:
        """在访问 GPIO 前校验芯片路径和 line offset。"""

        if not isinstance(self.chip_path, Path):
            raise TypeError("chip_path 必须是 pathlib.Path")
        if not str(self.chip_path):
            raise ValueError("chip_path 不能为空")
        if isinstance(self.line_offset, bool) or not isinstance(
            self.line_offset,
            int,
        ):
            raise TypeError("line_offset 必须是整数")
        if self.line_offset < 0:
            raise ValueError("line_offset 必须通过 MOTION_MAGNET_GPIO_LINE 配置")


