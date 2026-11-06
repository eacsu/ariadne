from pathlib import Path
from unittest.mock import patch
from ec_26_e.vision_factory import create_production_detector
from ariadne_vision import Detect1Config


def test_explicit_assets_reach_vision_factory():
    with patch.dict('os.environ', {'EC_VISION_MODEL_PATH': '/tmp/test.nb', 'EC_VISION_LIBRARY_PATH': '/tmp/test.so'}), patch('ec_26_e.vision_factory.factory.create_production_detector') as factory:
        config = Detect1Config()
        result = create_production_detector(config)
        factory.assert_called_once_with(config, model_path=Path('/tmp/test.nb'), library_path=Path('/tmp/test.so'))
        assert result is factory.return_value
