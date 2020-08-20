```python
[...]
    try:
        print('\033[1m\033[94m[Loja ' + loja + '][' + ssh_hostname + ']\n\033[0m')
        ssh.execute_commands([
            "ping 192.168.101.10 || echo 'Fail!' && echo 'Success'",
            "echo 'Done'"
        ])
        print('---\n')
    except Exception:
        errors.append('Falha na execução do comando com o \033[1m' + ssh_hostname + ' loja0' + loja + '\033[0;0m')
        break
    break
[...]
```