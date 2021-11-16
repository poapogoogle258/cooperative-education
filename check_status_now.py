import paramiko

def main():
    list_ssh_conneting = [
        {
            'host' : '139.5.147.36',
            'username' : "user01",
            'password' : "admin@123"
        }
    ]

    id = 1
    for user in list_ssh_conneting:
        p = paramiko.SSHClient()
        p.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # This script doesn't work for me unless this line is added!
        try:
            p.connect(user['host'], port=22, username=user['username'], password=user['password'],timeout=3)
            stdin, stdout, stderr = p.exec_command("python3.8 test.py")
            stdout = stdout.readline()
        except Exception:
            stdout = 'Down...'
            
        #Display host : cpu : memory
        print("#{} host: {}, {}".format(id,user['host'],stdout))
        id += 1


if __name__ == "__main__":
    main()


