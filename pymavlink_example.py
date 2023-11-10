import json

from pymavlink import mavutil

# 可以使用这个库，利用python来控制无人机的运动状态
# https://mavlink.io/zh/mavgen_python/
# 下面连接usb后，使用这个库，通过mavlink来获取无人机的状态信息

# https://mavlink.io/zh/mavgen_python/#connection_string
# 连接无人机的方式，下面是windows端口连接
# mission planner的固件，端口是com3
# qgroundcontrol的固件，端口是com16
the_connection = mavutil.mavlink_connection('com3')

# 在发送接接受指令前，需要获得心跳信息
the_connection.wait_heartbeat()
print(f"Heartbeat from system (system {the_connection.target_system} component {the_connection.target_component})")

# 请求获得所有信息流
# https://mavlink.io/zh/mavgen_python/#specific_messages
# https://mavlink.io/zh/messages/common.html#REQUEST_DATA_STREAM
the_connection.mav.request_data_stream_send(target_system=the_connection.target_system,
                                            target_component=the_connection.target_component,
                                            req_stream_id=mavutil.mavlink.MAV_DATA_STREAM_ALL,
                                            # 获得所有信息
                                            # The ID of the requested data stream
                                            req_message_rate=1,  # 接收信息的比率 1表示1秒完整的获取26组参数一次
                                            start_stop=1  # 1 to start sending, 0 to stop sending.
                                            )

# mission planner的固件可以获得26组参数，里面包含无人机的状态信息
t_type_1 = {'VIBRATION', 'SERVO_OUTPUT_RAW', 'SCALED_PRESSURE', 'TIMESYNC', 'SYSTEM_TIME', 'RAW_IMU', 'RC_CHANNELS',
            'AHRS2', 'VFR_HUD', 'POWER_STATUS', 'EKF_STATUS_REPORT', 'MEMINFO', 'PARAM_VALUE', 'STATUSTEXT',
            'SYS_STATUS', 'MISSION_CURRENT', 'SCALED_IMU2', 'GLOBAL_POSITION_INT', 'AHRS', 'TERRAIN_REPORT',
            'ATTITUDE', 'MCU_STATUS', 'NAV_CONTROLLER_OUTPUT', 'HEARTBEAT', 'BATTERY_STATUS', 'GPS_RAW_INT'}
# 示例的参数信息在 t_type_res_1.json 中
t_type = set()
t_res = []
run_num = 0  # 获取100次就停止获取，关闭程序
while True:
    run_num += 1
    if run_num > 100:
        break
    print('=' * 50)
    # 可以用下面的type，来指定获得特定type参数
    # msg = the_connection.recv_match(type='RAW_IMU', blocking=True)
    msg = the_connection.recv_match(blocking=True).to_dict()
    print(msg)
    if msg['mavpackettype'] not in t_type:
        t_type.add(msg['mavpackettype'])
        t_res.append(msg)

print(t_type)
with open('t_type_res_1.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(t_res, ensure_ascii=False, indent=4))

# 其他更多的例子：https://www.ardusub.com/developers/pymavlink.html
# 通过串行连接到计算机的 Autopilot
# 在 Surface 计算机上运行 pyMavlink
# 在配套计算机上运行 pyMavlink
# 发送消息至 QGroundControl
# 布防/撤防车辆
# 更改飞行模式
# 发送 RC（操纵杆）
# 发送手动控制
# 读取所有参数
# 读取和写入参数
# 接收数据并按消息类型进行筛选
# 请求消息间隔
# 控制相机云台
# 设置舵机PWM
# 高级伺服/夹持器示例
# 设置目标深度/姿态
# 发送 GPS 位置
# 将测距仪/计算机视觉距离测量发送到自动驾驶仪
