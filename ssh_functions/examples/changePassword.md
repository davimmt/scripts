```python
[...]
    try:
        print('\033[1m\033[94m[Loja ' + loja + '][' + ssh_hostname + ']\n\033[0m')
        ssh.execute_commands(c.changePassword(ssh_hostname, new_password))
        print('---\n')
    except Exception:
        errors.append('Falha na execução do comando com o \033[1m' + ssh_hostname + ' loja0' + loja + '\033[0;0m')
        break
    break
[...]
```