import json
import sys

from pymavlink import mavutil

the_connection = mavutil.mavlink_connection('com11')
the_connection.wait_heartbeat()
print(f"Heartbeat from system (system {the_connection.target_system} component {the_connection.target_component})")

the_connection.mav.param_request_list_send(target_system=the_connection.target_system,
                                           target_component=the_connection.target_component)
# ATC_RAT_RLL_P 软件里面改为了 0.136
param_list = []
while True:
    # time.sleep(0.01)
    if len(param_list) > 1500:
        break
    try:
        message: dict = the_connection.recv_match(blocking=True).to_dict()
        for k in message.keys():
            message[k] = str(message[k])
        print(f"{len(param_list)}-{message['mavpackettype']}-{message.get('param_id', '')}".ljust(50, '='))
        if message is None or message == {} or message == '':
            break
        # print(message)
        param_list.append(message)
    except Exception as error:
        print(error)
        sys.exit(0)

with open('param_list_px4.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(param_list, indent=4))
