# ariadne_vision

Ariadne 的 vision 独立项目。

```bash
poetry install
poetry run pytest
poetry build
```

模型、SDK、相机与电机为外部资源。默认测试不访问真实设备。

## Python 基线

使用 Python 3.10。执行 `python3.10 -m venv .venv`，再执行 `VIRTUAL_ENV="$PWD/.venv" poetry install`。验证 `.venv/bin/python --version` 后运行 `VIRTUAL_ENV="$PWD/.venv" poetry run pytest`。
