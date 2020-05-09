from SSH import SSH
from Loja import Loja
from Command import Command
from Function import Function

lojas = Loja().getPOS()

for loja in lojas:
    print('Loja: 0' + str(loja[0]) + '\nCaixa: ' + loja[1][0] + '\nIP: 192.168.10' + str(loja[0]) + "." + loja[1][1] + '\n\n---\n')

# if __name__ == '__main__':
#     c = Command()
#     f = Function()

#     ssh_password = f.getBaseVariables('password')[2]
#     ssh = SSH('192.168.0.18', 'vanessa', ssh_password)

#     file_name = '/etc/cron.d/ntpdate'
#     cron = '*/30 * * * *'
#     user = ' root '
#     jobs = ['First', 'Second', 'Third']

#     ssh.execute_commands(c.ntpdate(file_name, cron, user, jobs))


