# scripts

Programa desenvolvido para desempenhar comandos remotos via ssh para todos os caixas das lojas 01 a 06, a fim de automar parte da produção. Comandos incluem:

- setCronjob(): 
  - Objetivo: adicionar um serviço no contrab do sistema.
  - Parâmetros: 
    - (string) nome do arquivo;
    - (string) tempo de crontab;
    - (string) usuário de execução;
    - (array) serviços.
  - Retorno: null;
  - [Exemplo](/ssh_functions/examples/setCronjob.md).

- isPinging(): 
  - Objetivo: verificar se o objeto está pingando.
  - Parâmetros: 
    - (string) IP.
  - Retorno: (int) 1|(int) 0
  - [Exemplo](/ssh_functions/examples/isPinging.md).

- getDatetime(): 
  - Objetivo: retornar as horas do sistema e da BIOS do objeto;
  - Parâmetros: null;
  - Retorno: (string);
  - [Exemplo](/ssh_functions/examples/getDatetime.md).

- getEcf(): 
  - Objetivo: retornar o número de ecf registrado do caixa objeto;
  - Parâmetros: null;
  - Retorno: (string);
  - [Exemplo](/ssh_functions/examples/getEcf.md).

- changePassword(): 
  - Objetivo: mudar a senha do usuário objeto;
  - Parâmetros: 
    - (string) nome de usuário;
    - (string) senha nova;
  - Retorno: null;
  - [Exemplo](/ssh_functions/examples/changePassword.md).

- checkPassword(): 
  - Objetivo: verificar a correspondibilidade da senha do usuário objeto;
  - Parâmetros: 
    - (string) IP;
  - Retorno: (bool)|(string)
  - [Exemplo](/ssh_functions/examples/checkPassword.md).


Você também tem a opção de passar comandos shell sem chamar as funções ou comandos pré-feitos:
  - [Exemplo](/ssh_functions/examples/basic.md).
