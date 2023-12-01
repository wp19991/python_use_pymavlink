import time

from pymavlink import mavutil

master = mavutil.mavlink_connection('com11')
master.wait_heartbeat()
print(f"Heartbeat from system (system {master.target_system} component {master.target_component})")

message = master.mav.command_long_encode(
    master.target_system,  # Target system ID
    master.target_component,  # Target component ID
    mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST,  # ID of command to send
    0,  # Confirmation
    1,  # 电机实例编号（从 1 到车辆上电机的最大数量）。
    1,  # 油门类型（param3中的Throttle Value是否为百分比、PWM值等）
    1000,  # 油门值。
    3,  # 按顺序运行的测试之间的超时。
    1,  # 电机数。按顺序测试的电机数量：0/1=一个电机，2=两个电机等。超时（参数 4）用于测试之间。
    0,  # 电机测试订单。
    0  # 保留（设置为 0）
)

# Send the COMMAND_LONG
master.mav.send(message)

print('电机')
time.sleep(5)
