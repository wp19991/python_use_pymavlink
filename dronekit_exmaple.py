import json
import time

from dronekit import connect

# Connect to the Vehicle (in this case a UDP endpoint)
# https://dronekit-python.readthedocs.io/en/latest/guide/connecting_vehicle.html
vehicle = connect('com11', wait_ready=True)
# MAV_0_CONFIG=6
# http://docs.px4.io/main/en/advanced_config/parameter_reference.html
# 当首次连接到UAV时，DroneKit会下载所有参数（强制参数读取等待,直到下载完成），然后通过监控车辆消息来保持值更新用于对单个参数的更改。
# 此过程可确保读取支持的参数始终是安全的，并且它们的值将与车辆上的信息相匹配。
# 可以使用属性（对象）读取、设置、观察和迭代参数。

# 打印系统状态
print(f"Autopilot Firmware version: {vehicle.version}")
print(f"Autopilot capabilities (supports ftp): {vehicle.capabilities.ftp}")
print(f"Global Location: {vehicle.location.global_frame}")
print(f"Global Location (relative altitude): {vehicle.location.global_relative_frame}")
print(f"Local Location: {vehicle.location.local_frame}")  # NED
print(f"Attitude: {vehicle.attitude}")
print(f"Velocity: {vehicle.velocity}")
print(f"GPS: {vehicle.gps_0}")
print(f"Groundspeed: {vehicle.groundspeed}")
print(f"Airspeed: {vehicle.airspeed}")
print(f"Gimbal status: {vehicle.gimbal}")
print(f"Battery: {vehicle.battery}")
print(f"EKF OK?: {vehicle.ekf_ok}")
print(f"Last Heartbeat: {vehicle.last_heartbeat}")
print(f"Rangefinder: {vehicle.rangefinder}")
print(f"Rangefinder distance: {vehicle.rangefinder.distance}")
print(f"Rangefinder voltage: {vehicle.rangefinder.voltage}")
print(f"Heading: {vehicle.heading}")
print(f"Is Armable?: {vehicle.is_armable}")
print(f"System status: {vehicle.system_status.state}")
print(f"Mode: {vehicle.mode.name}")  # settable
print(f"Armed: {vehicle.armed}")  # settable

# 获取所有参数
param_map = {}
for key, value in vehicle.parameters.items():
    # print(f" Key:{key} Value:{value}")
    param_map[key] = value
# 保存所有参数
with open('param_map_1.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(param_map, ensure_ascii=False, indent=4))

# 修改参数步骤
# 更改值的命令不能保证成功，下面的代码片段轮询属性值，以确认它们已更改，然后再继续。
print(f"change before ATC_RAT_RLL_P={vehicle.parameters['ATC_RAT_RLL_P']}")
vehicle.parameters['ATC_RAT_RLL_P'] = 0.137
while not abs(vehicle.parameters['ATC_RAT_RLL_P'] - 0.137) < 0.001:
    print("changing ...")
    time.sleep(1)
print(f"change after ATC_RAT_RLL_P={vehicle.parameters['ATC_RAT_RLL_P']}")


# 可以观察某个状态发生的变化，如果变化了，会调用回调函数
# 回调函数第一个需要是self，第二个是参数名称，第三个是变化的参数值
def location_callback(self, attr_name, value):
    print(f"location_callback {attr_name}: {value}")


# Add a callback `location_callback` for the `global_frame` attribute.
vehicle.add_attribute_listener('*', location_callback)
# Wait 2s so callback can be notified before the observer is removed
time.sleep(2)
# Remove observer - specifying the attribute and previously registered callback function
vehicle.remove_message_listener('*', location_callback)


# 观察所有mavlink的消息，出现变化的时候调用函数
@vehicle.on_message('*')
def listener(self, name, message):
    print(f'mavlink message: {name} : {message}')


time.sleep(5)
