from SSH import SSH
from Loja import Loja
from Command import Command
from Function import Function

loja = [2] # Mude as LOJAS alvo aqui

lojas = []
for item in loja:
    loja_index = item - 1
    lojas.append(Loja().getAllPOS()[loja_index])

if __name__ == '__main__':
    f = Function()
    errors = []

    for loja_list in lojas:
        caixas_list = loja_list[1]

        for caixas in caixas_list:
            for caixa in caixas:
                loja           = loja_list[0]
                ssh_ip         = '192.168.' + caixas[1]
                ssh_hostname   = caixas[0]
                password_index = caixas[2]

                c = Command(password_index)
                ssh_password = f.getBaseVariables('password')[password_index]
                
                try:
                    ssh = SSH(ssh_ip, ssh_hostname, ssh_password)
                except Exception:
                    errors.append('Falha na conexão SSH com o \033[1m' + ssh_hostname + ' loja0' + loja + '\033[0;0m')
                    break

                try:
                    print('\033[1m\033[94m[Loja ' + loja + '][' + ssh_hostname + ']\n\033[0m')
                    # Insira os COMANDOS/FUNÇÕES aqui
                    c.isPinging(ssh_ip)
                    #
                    print('---\n')
                except Exception:
                    errors.append('Falha na execução do comando com o \033[1m' + ssh_hostname + ' loja0' + loja + '\033[0;0m')
                    break
                break

    for error in errors:
        print('\033[91m' + error + '.\033[0;0m\n')

