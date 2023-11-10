from pymavlink import mavutil

the_connection = mavutil.mavlink_connection('com3')
the_connection.wait_heartbeat()
print(f"Heartbeat from system (system {the_connection.target_system} component {the_connection.target_component})")

# 设置参数，包含pid的所有设置
# 设置参数值：https://mavlink.io/zh/messages/common.html#PARAM_SETv
# 需要修改的参数ID，param_id：param_list.json中有mission planner的所有参数，大概有960个
# param_value：数据的值
# 参数值的类型，param_type：https://mavlink.io/zh/messages/common.html#MAV_PARAM_TYPE
the_connection.mav.param_set_send(
    target_system=the_connection.target_system, target_component=the_connection.target_component,
    param_id=b'ATC_RAT_RLL_P',
    param_value=0.137,
    param_type=mavutil.mavlink.MAV_PARAM_TYPE_REAL32
)
