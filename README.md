# scripts

Programa desenvolvido para desempenhar comandos remotos via ssh para todos os caixas das lojas 01 a 06, a fim de automar parte da produção. Alguns comandos incluem:

- ntpdate(): adicionar um cronjob no sistema;
- getDates(): retorna as horas do sistema e da BIOS do caixa;
- changePassword(): muda a senha dos usuários operários de caixa;
- checkPassword(): verifica a correspondibilidade da senha do usuário caixa;
- isPinging(): verifica se o caixa está ligado na rede;

#### Exemplo de uso da função ntpdate():

```python
lojas = Loja().getPOS() # return @list [loja, [nome, ip, index_senha]] -> index_senha é referente ao arquivo Function.py

if __name__ == '__main__':
    f = Function()
    errors = []

    for loja in lojas:
        password_index = loja[1][2]
        ssh_hostname = loja[1][0]
        ssh_ip = '192.168.' + loja[0] + "." + loja[1][1]

        file_name = '/etc/cron.d/ntpdate'
        cron = '*/30 * * * *'
        user = ' root '
        jobs = [
            'First', 
            'Second', 
            'Third'
        ]

        try:
            ssh.execute_commands(c.ntpdate(file_name, cron, user, jobs))
        except Exception:
            errors.append('Falha na execução do comando com o caixa \033[1m' + ssh_hostname)
            continue

        for error in errors:
            print('\033[91m' + error + '.\n')
```

#### Exemplo de uso da função getDates() em uma só loja:

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
            ssh.execute_commands(c.getDates())
            print('---\n')
        except Exception:
            errors.append('Falha na execução do comando com o caixa \033[1m' + ssh_hostname)
            continue

    for error in errors:
        print('\033[91m' + error + '.\n')
```
