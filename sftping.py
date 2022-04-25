import paramiko

def main():
    host = "myserver"
    port = 22
    username = "vannia"
    password = "passowrd"

    local_path = "/home/f1/f2/file.txt"
    remote_path = "/home/fx/file.txt"

    transport = paramiko.Transport((host,port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, remote_path)

    transport.close()

main() 