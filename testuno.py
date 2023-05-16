import time
import paramiko
# conexion con diferentes equipos por ip"
ip_addresses = ["192.168.183.10", "192.168.183.20", "192.168.183.101",
"192.168.183.102", "192.168.183.133"]

username = "pynetauto"
password = "cisco123"

for ip in ip_addresses:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password)
    print("Connected to " + ip + "\n")
    remote_connection = ssh_client.invoke_shell()
    output1 = remote_connection.recv(3000)
    print(output1.decode('ascii'))
    remote_connection.send("show clock detail\n")
    time.sleep(2)
    output2 = remote_connection.recv(6000)
    print((output2).decode('ascii'))
    print("-"*80)

