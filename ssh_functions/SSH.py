import paramiko
from paramiko import SSHClient

class SSH:
    def __init__(self, hn, us, pw):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname = hn, username = us, password = pw)
    
    def execute_commands(self, commands):
        for cmd in commands:
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            stdout.channel.recv_exit_status()
            response = stdout.readlines()
            if response:
                for line in response:
                    print(f'INPUT: {cmd} | OUTPUT: {line}')
            else:
                print('No response.\n')