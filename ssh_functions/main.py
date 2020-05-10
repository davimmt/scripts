from SSH import SSH
from Loja import Loja
from Command import Command
from Function import Function

vms = Loja().getVM() # return @list [loja, [nome, ip, index_senha]] -> index_senha é referente ao arquivo Function.py

if __name__ == '__main__':
    f = Function()

    for vm in vms:
        password_index = vm[1][2]

        c = Command(password_index)

        ssh_hostname = vm[1][0]
        ssh_ip = '192.168.' + str(vm[0]) + "." + vm[1][1]
        ssh_password = f.getBaseVariables('password')[password_index]

        ssh = SSH(ssh_ip, ssh_hostname, ssh_password)

        file_name = '/etc/cron.d/ntpdate'
        cron = '*/30 * * * *'
        user = ' root '
        jobs = ['First', 'Second', 'Third']

        ssh.execute_commands(c.ntpdate(file_name, cron, user, jobs))
