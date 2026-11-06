# EC26E 迁移验收

源提交：16094397734adcd477a57cba47a33db237872750。原仓库未改，Git历史不导入。

## Python 3.10 基线

使用实际 Python 3.10.20、同一依赖集合对旧版和迁移版运行测试。旧版302通过/17失败；迁移版：求解28通过/2失败、视觉60通过、设备48通过、应用167通过/15失败（新增资源路径测试1项）。原有用例仍302通过/17失败，失败用例集合一致，未屏蔽断言。早期3.12排查结果不作为基线。

注意 Poetry 创建的带 py3.10 名称环境曾实际指向3.12，最终以 `python3.10 -m venv .venv` 创建并核验版本。

## 已有失败用例

- `tests/unit/cam/test_camera_cli_config.py::CameraCliConfigTest::test_detected_video_cli_overrides_environment_resolutions`
- `tests/unit/cam/test_camera_cli_config.py::CameraCliConfigTest::test_detected_video_reads_device_and_resolutions_from_environment`
- `tests/unit/cam/test_camera_cli_config.py::CameraCliConfigTest::test_invalid_a4_ratio_fails_before_device_query`
- `tests/unit/control/test_planner.py::FixedPlannerTest::test_fixed_plan_is_complete_and_on_lower_half`
- `tests/unit/control/test_planner.py::FixedPlannerTest::test_fixed_plan_uses_gapped_non_overlapping_final_layout`
- `tests/unit/test_command_cli.py::CommandCliTest::test_draw_setting_is_passed_through_global_context`
- `tests/unit/test_command_cli.py::CommandCliTest::test_env_option_only_changes_environment_source`
- `tests/unit/test_command_cli.py::CommandCliTest::test_expected_task_failure_exits_one`
- `tests/unit/test_command_cli.py::CommandCliTest::test_explicit_task_selection_is_forwarded_without_other_overrides`
- `tests/unit/test_command_cli.py::CommandCliTest::test_keyboard_interrupt_exits_130`
- `tests/unit/test_command_cli.py::CommandCliTest::test_no_arguments_runs_env_selected_task`
- `tests/unit/test_command_cli.py::CommandCliTest::test_preview_cancellation_exits_130`
- `tests/unit/test_command_cli.py::CommandCliTest::test_retryable_task_failure_uses_temporary_exit_code`
- `tests/unit/test_command_cli.py::CommandCliTest::test_selection_or_json_failures_exit_two_before_run`
- `tests/unit/test_task1_config.py::Task1ConfigContractTest::test_official_json_is_complete_fixed_configuration`
- `tests/unit/test_task2_config.py::Task2ConfigTest::test_official_configuration_is_random_white_paper_task`
- `tests/integration/tasks/test_task1_pipeline.py::Task1PipelineIntegrationTest::test_structured_detect1_results_run_real_fixed_planner`

失败主要涉及旧配置预期、CLI默认调度与固定拼图尺寸/间隙。此次仅迁移，不改变这些行为。完整检查继续返回非零。

## 外部验收

C++纯预处理/后处理2项通过。真实模型、VIPLite SDK、相机、电机与GPIO未提供，未进行实机验证。迁移后新增的资源路径由调用方传入；板端需重新构建原生库并配置模型路径。

## 依赖与所有权

视觉拥有相机和NPU；求解拥有几何契约；设备拥有串口和GPIO；应用拥有坐标转换、计划编译、执行生命周期、任务和配置。三个基础项目互不导入。Task1/Task2公共流程位于应用 tasks/puzzle。

## 文件去向

详细见 [文件清单](files.md)。诊断工具迁到应用包的diagnostics，求解评估工具保留在引擎内，旧生成物不迁入。

四个项目均构建 sdist/wheel；轮子安装至仓库外目录验证导入。默认检查不跳过既有失败。
