"""
QGroundControl进行电机测试，是使用MAV_CMD_ACTUATOR_TEST进行的
QGroundControl电机测试代码：
https://github.com/mavlink/qgroundcontrol/tree/master/src/Vehicle/Actuators/ActuatorTesting.cc
mavlink命令：
https://mavlink.io/en/messages/common.html#MAV_CMD_ACTUATOR_TEST
https://mavlink.io/en/messages/common.html#ACTUATOR_OUTPUT_FUNCTION_MOTOR1
Actuator output function. Values greater or equal to 1000 are autopilot-specific.

有些mavlink命令，pymavlink没有定义，例如MAV_CMD_ACTUATOR_TEST

没有定义的命令，可以使用数字来代替，原因是pymavlink没有把全部的命令给映射为全局变量，导致不能使用
"""
from pymavlink import mavutil
from pymavlink.dialects.v20 import ardupilotmega as mavlink

master1 = mavutil.mavlink_connection('com11')
master1.wait_heartbeat()
print(f"Heartbeat from system (system {master1.target_system} component {master1.target_component})")

master = mavlink.MAVLink(master1)
master.command_long_send(
    master1.target_system, master1.target_component,
    310, 0,
    0,  # 输出值：1 表示最大正输出，0 表示伺服中心或最小电机推力（预计旋转），
    3,  # 超时，在此之后测试命令到期并且输出恢复到之前的值。出于安全原因，必须设置超时。超时为0表示立即恢复之前的值。
    0,  # 保留（设置为 0）
    0,  # 保留（设置为 0）
    1,  # 电机1
    0,  # 保留（设置为 0）
    0  # 保留（设置为 0）
)
master.command_long_send(
    master1.target_system, master1.target_component,
    310, 0,
    0,  # 输出值：1 表示最大正输出，0 表示伺服中心或最小电机推力（预计旋转），
    3,  # 超时，在此之后测试命令到期并且输出恢复到之前的值。出于安全原因，必须设置超时。超时为0表示立即恢复之前的值。
    0,  # 保留（设置为 0）
    0,  # 保留（设置为 0）
    2,  # 电机1
    0,  # 保留（设置为 0）
    0  # 保留（设置为 0）
)
master.command_long_send(
    master1.target_system, master1.target_component,
    310, 0,
    0,  # 输出值：1 表示最大正输出，0 表示伺服中心或最小电机推力（预计旋转），
    3,  # 超时，在此之后测试命令到期并且输出恢复到之前的值。出于安全原因，必须设置超时。超时为0表示立即恢复之前的值。
    0,  # 保留（设置为 0）
    0,  # 保留（设置为 0）
    3,  # 电机1
    0,  # 保留（设置为 0）
    0  # 保留（设置为 0）
)
master.command_long_send(
    master1.target_system, master1.target_component,
    310, 0,
    0,  # 输出值：1 表示最大正输出，0 表示伺服中心或最小电机推力（预计旋转），
    3,  # 超时，在此之后测试命令到期并且输出恢复到之前的值。出于安全原因，必须设置超时。超时为0表示立即恢复之前的值。
    0,  # 保留（设置为 0）
    0,  # 保留（设置为 0）
    4,  # 电机1
    0,  # 保留（设置为 0）
    0  # 保留（设置为 0）
)

# time.sleep(5)
