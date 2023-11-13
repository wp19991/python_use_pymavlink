# pymavlink
> 使用python连接并且控制无人机的调研与测试

## DroneKit

- DroneKit是由pymavlink更高一级的抽象而来的，使用DroneKit来控制无人机更加容易

### 示例

- 使用DroneKit的示例：[dronekit_exmaple.py](./dronekit_exmaple.py)
    - 无人机的连接
    - 无人机的状态打印
    - 修改无人机参数
    - 添加监听回调函数

## pymavlink

> 使用python通过mavlink读取设置无人机的参数（包含pid的参数等）

> 使用python通过mavlink来控制无人机的的飞行状态

> 目前使用mission planner烧录的固件

- 对pymavlink库的简单介绍：[pymavlink_example.py](./pymavlink_example.py)
- 读取所有参数：[read_all_param.py](./read_all_param.py)
- 设置参数：[set_param.py](./set_param.py)

### 参考连接

- [Pymavlink库 (mavgen)使用指南](https://mavlink.io/zh/mavgen_python/)
- [MAVLINK通用消息集](https://mavlink.io/zh/messages/common.html)
- [pymavlink示例教程](https://www.ardusub.com/developers/pymavlink.html)
- [pymavlink仓库](https://github.com/ArduPilot/pymavlink)