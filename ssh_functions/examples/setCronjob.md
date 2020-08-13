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
            ssh.execute_commands(c.setCronjob(file_name, cron, user, jobs))
        except Exception:
            errors.append('Falha na execução do comando com o caixa \033[1m' + ssh_hostname)
            continue

        for error in errors:
            print('\033[91m' + error + '.\n')
```