import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
hostname = '127.0.0.1'
uname = 'gaurav'
passwd = 'gaurav'
port = 5679
ssh_client.connect(hostname=hostname,username=uname,password=passwd,port=port)

stdin,stdout,stderr = ssh_client.exec_command('hostname')
outlines=stdout.read()
print(outlines)
err = stderr.read().decode()
print(err)

# inp = stdin.read()
# print(inp)

