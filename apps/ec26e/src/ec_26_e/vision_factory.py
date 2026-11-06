"""装配显式部署资源与现有生产视觉参数。"""
import os
from pathlib import Path
from ariadne_vision import factory

def create_production_detector(config):
    return factory.create_production_detector(config,
        model_path=Path(os.environ.get("EC_VISION_MODEL_PATH", "model-bin/puzzle_seg_yolo11n_640_pcq_a733.nb")).resolve(),
        library_path=Path(os.environ.get("EC_VISION_LIBRARY_PATH", "native/yolo11_seg_npu/build/libyolo11_seg_npu.so")).resolve())
