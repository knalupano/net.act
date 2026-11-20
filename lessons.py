from netmiko import ConnectHandler


router_device = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.1.123',
    'port': 32770,
    'username': 'admin',
    'password': 'eve123',
    'secret': 'eve123'
}


try:
    print("Connecting to the router...")
    net_connect = ConnectHandler(**router_device)
    net_connect.enable()


    command_to_run = [
        'show version',
        'show ip interface brief',
        'show running-config',
    ]


    for command in command_to_run:
        print(f"\n--- output for: {command} ---")
        output = net_connect.send_command(command)
        print(output)


    net_connect.disconnect()
    print("Disconnected from the router successfully.")
except Exception as e:
    print(f"An error occurred: {e}")