from SSH import SSH
from Loja import Loja
from Command import Command
from Function import Function

lojas = Loja().getPOS() # return @list [loja, [nome, ip, index_senha]]
loja1 = Loja().getLoja01POS() # return @list [nome, ip, index_senha]
loja2 = Loja().getLoja02POS()
loja3 = Loja().getLoja03POS()
loja4 = Loja().getLoja04POS()
loja5 = Loja().getLoja05POS()
loja6 = Loja().getLoja06POS()

if __name__ == '__main__':
    f = Function()
    errors = []
    
    for caixa in loja1:
        password_index = caixa[2]
        ssh_hostname = caixa[0]
        ssh_ip = '192.168.' + caixa[1]

        c = Command(password_index)
        ssh_password = f.getBaseVariables('password')[password_index]

        try:
            ssh = SSH(ssh_ip, ssh_hostname, ssh_password)
        except Exception:
            errors.append('Falha na conexão SSH com o caixa \033[1m' + ssh_hostname)
            continue

        try:
            print('\033[1m\033[94m[' + ssh_hostname + ']\n\033[0m')
            ssh.execute_commands(c.changePassword(ssh_hostname, f.getBaseVariables('password')[4]))
            # ssh.execute_commands(c.checkPassword(f.getBaseVariables('password')[4]))
            print('---\n')
        except Exception:
            errors.append('Falha na execução do comando com o caixa \033[1m' + ssh_hostname + '\033[0;0m')
            continue

    for error in errors:
        print('\033[91m' + error + '.\033[0;0m\n')

