# YOLO11n-seg A733 C ABI

本目录把 `puzzle_seg_yolo11n_640_pcq_a733.nb` 封装为一个不暴露 C++ ABI 的共享库。模型契约固定为 `UINT8 3×640×640` 输入，三组 `64/1/32` 检测头和 `FP32 160×160×32` prototype。

构建与测试：

```bash
cmake -S native/yolo11_seg_npu -B native/yolo11_seg_npu/build -DCMAKE_BUILD_TYPE=Release
cmake --build native/yolo11_seg_npu/build -j4
(cd native/yolo11_seg_npu/build && ctest --output-on-failure)
```

`yolo_seg_infer_bgr` 接收任意尺寸、可带行跨度的 BGR 图，原生层完成 letterbox、DFL、NMS、mask 重建和逆映射。调用方为每个实例提供一张源图大小的连续 `uint8` mask。VIPLite 当前限制同一进程只有一个上下文，并要求创建、推理和销毁发生在同一线程。

Python 入口是 `ariadne_vision`。普通主机测试使用 `-DYOLO_BUILD_VIPLITE=OFF` 配置CMake；板端构建通过 `-DAI_SDK_ROOT=...` 指定SDK。Python包不包含模型或已编译动态库，调用者通过工厂参数提供资源路径。
