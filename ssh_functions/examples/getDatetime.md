```python
loja4 = Loja().getLoja04POS() # return @list [nome, ip, index_senha] -> index_senha é referente ao arquivo Function.py

if __name__ == '__main__':
    f = Function()
    errors = []
    
    for caixa in loja4:
        password_index = caixa[2]
        ssh_hostname = caixa[0]
        ssh_ip = '192.168.104.' + caixa[1]

        c = Command(password_index)
        ssh_password = f.getBaseVariables('password')[password_index]

        try:
            ssh = SSH(ssh_ip, ssh_hostname, ssh_password)
        except Exception:
            errors.append('Falha na conexão SSH com o caixa \033[1m' + ssh_hostname)
            continue

        try:
            print('\033[1m\033[94m[' + ssh_hostname + ']\n\033[0m')
            ssh.execute_commands(c.getDatetime())
            print('---\n')
        except Exception:
            errors.append('Falha na execução do comando com o caixa \033[1m' + ssh_hostname)
            continue

    for error in errors:
        print('\033[91m' + error + '.\n')
```