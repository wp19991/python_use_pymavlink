from pymavlink import mavutil

master = mavutil.mavlink_connection('com11')
master.wait_heartbeat()
print(f"Heartbeat from system (system {master.target_system} component {master.target_component})")

# Get some information !
while True:
    try:
        t_data: dict = master.recv_match().to_dict()
        show_str = ""
        if t_data['mavpackettype'] == 'LOCAL_POSITION_NED':
            show_str = f"LOCAL_POSITION_NED:{t_data['time_boot_ms']}," \
                       f"x:{t_data['x']:.2f},y:{t_data['y']:.2f},z:{t_data['z']:.2f}," \
                       f"vx:{t_data['vx']:.2f},vy:{t_data['vy']:.2f},vz:{t_data['vz']:.2f}"
        elif t_data['mavpackettype'] == 'ATTITUDE':
            show_str = f"          ATTITUDE:{t_data['time_boot_ms']}," \
                       f"roll:{t_data['roll']:.2f},pitch:{t_data['pitch']:.2f},yaw:{t_data['yaw']:.2f}," \
                       f"{t_data['rollspeed']:.2f},{t_data['pitchspeed']:.2f},{t_data['yawspeed']:.2f}"
        # elif t_data['mavpackettype'] == 'ATTITUDE':
        #     pass
        # else:
        #     show_str = str(t_data)
        print(show_str)
    except:
        pass
    # time.sleep(0.1)
