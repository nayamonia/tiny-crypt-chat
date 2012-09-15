tiny-crypt-chat
===============

Exemplo de chat seguro usando sockets

Este é um exemplo de como utilizar sockets para desenvolver um chat seguro em Python

O código está comentado em português e é uma boa oportunidade de aprendizado para aqueles 
que estão começando seus estudos sobre sockets.

Para executar o servidor existem as opções -s ou --servidor, como o exemplo que segue:

$ python main.py --servidor 8000

O comando acima põe o servidor para escutar na porta 8000.

O servidor permite apenas um cliente e, para executar o programa como cliente, usa-se a 
opção -c ou --cliente. Exemplo:

$ python main.py --cliente 127.0.0.1:8000

Este comando procura um servidor que esteja escutando pela porta 8000 no 127.0.0.1.

Atenção: Execute em modo servidor antes de executar em modo cliente no outro 
terminal ou computador