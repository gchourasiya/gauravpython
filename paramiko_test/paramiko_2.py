import sys

import paramiko

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    hostname = '127.0.0.1'
    uname = 'gaurav'
    passwd = 'gaurav'
    port = 5679
    ssh.connect(username=uname,password=passwd,hostname=hostname,port=port)
    stdin,stdout,stderr = ssh.exec_command('ls -l anything')

    # stdin.write("gaurav\n")
    # stdin.write("\x04")

    print(stderr.read().decode())
    out = stdout.read().decode()
    if out:
        print(out)

except paramiko.AuthenticationException:
    print("Authentication exception")
    sys.exit(1)
except:
    print("Exception")
<<<<<<< HEAD
=======
    #End of code.
>>>>>>> 56f5cf0 (First code push)


