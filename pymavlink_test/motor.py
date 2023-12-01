# from pymavlink.dialects.v20 import ardupilotmega
import os
import time

from pymavlink import mavutil

# 设置环境变量
os.environ['MAVLINK_DIALECT'] = "ardupilotmega"
os.environ['MAVLINK20'] = "1"

master = mavutil.mavlink_connection('com11')
master.wait_heartbeat()
print(f"Heartbeat from system (system {master.target_system} component {master.target_component})")

master.mav.command_long_send(
    master.target_system, master.target_component,
    mavutil.mavlink.MAV_CMD_ACTUATOR_TEST, 0,
    0,  # 输出值：1 表示最大正输出，0 表示伺服中心或最小电机推力（预计旋转），
    3,  # 超时，在此之后测试命令到期并且输出恢复到之前的值。出于安全原因，必须设置超时。超时为0表示立即恢复之前的值。
    0,  # 保留（设置为 0）
    0,  # 保留（设置为 0）
    mavutil.mavlink.ACTUATOR_OUTPUT_FUNCTION_MOTOR1,  # 执行器输出功能
    0,  # 保留（设置为 0）
    0  # 保留（设置为 0）
)

time.sleep(5)
