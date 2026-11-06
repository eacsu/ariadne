# ec_26_e

Ariadne 的 app 独立项目。

```bash
poetry install
poetry run pytest
poetry build
```

模型、SDK、相机与电机为外部资源。默认测试不访问真实设备。

## Python 基线

使用 Python 3.10。执行 `python3.10 -m venv .venv`，再执行 `VIRTUAL_ENV="$PWD/.venv" poetry install`。验证 `.venv/bin/python --version` 后运行 `VIRTUAL_ENV="$PWD/.venv" poetry run pytest`。

## 运行与部署

在本目录运行 `poetry run ec-26-e --help`。复制 `.env.example` 为 `.env` 后按机器填写配置；任务JSON在 `configs/tasks`。运行默认会访问真实硬件。

模型和动态库需从原板端提供，运行前导出 `EC_VISION_MODEL_PATH` 与 `EC_VISION_LIBRARY_PATH` 为绝对路径。这两个资源变量当前读取进程环境；普通任务参数仍使用原有环境/JSON加载器。

诊断使用模块形式，例如 `poetry run python -m ec_26_e.diagnostics.motion.control_axes --help`；现场标定使用 `poetry run python -m ec_26_e.calibration_console`。需要 Tk、FFmpeg、板端驱动和桌面环境。

`poetry run python deploy/render.py --output /tmp/ec26e-deploy` 生成用户级服务和桌面配置，检查后自行安装。不自动启动服务。必须从本应用目录运行；工作目录承担默认配置和输出位置，不再从源码层级推算。
