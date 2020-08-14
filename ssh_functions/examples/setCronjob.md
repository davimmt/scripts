```python
[...]
    file_name = '/etc/cron.d/ntpdate'
    cron = '*/30 * * * *'
    user = ' root '
    jobs = [
        'First', 
        'Second', 
        'Third'
    ]

    try:
        print('\033[1m\033[94m[Loja ' + loja + '][' + ssh_hostname + ']\n\033[0m')
        ssh.execute_commands(c.setCronjob(file_name, cron, user, jobs))
        print('---\n')
    except Exception:
        errors.append('Falha na execução do comando com o \033[1m' + ssh_hostname + ' loja0' + loja + '\033[0;0m')
        break
    break
[...]
```