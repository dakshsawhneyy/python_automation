import paramiko

# 1. Setup the Client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Trust new servers automatically

# 2. Connect (Using key is better than password)
key = paramiko.RSAKey.from_private_key_file("/path/to/private_key.pem")
client.connect(hostname="1.2.3.4", username="ubuntu", pkey=key)

# 3. Execute Command
stdin, stdout, stderr = client.exec_command("uptime")
print(stdout.read().decode())

# 4. Close
client.close()
