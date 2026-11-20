from flask import Flask, render_template, request
from netmiko import ConnectHandler


app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    error = None


    if request.method == 'POST':
        router_device = {
            'device_type': 'cisco_ios_telnet',
            'ip': '192.168.1.123',
            'port': 32770,
            'username': 'YOUR_USERNAME',
            'password': 'YOUR_PASSWORD',
            'secret': 'YOUR_ENABLE_SECRET'
        }


        command_to_run = [
            'show version',
            'show ip interface brief',
            'show running-config',
        ]


        net_connect = None
        try:
            net_connect = ConnectHandler(**router_device)
            net_connect.enable()


            for command in command_to_run:
                output = net_connect.send_command(command)
                result[command] = output
        except Exception as e:
            error = f"An error occurred: {e}"
        finally:
            if net_connect is not None:
                net_connect.disconnect()


    return render_template('index.html', result=result, error=error)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)