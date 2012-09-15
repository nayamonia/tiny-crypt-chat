#!/usr/bin/env python
# encoding: utf-8
# author: Gabriel Fernandes - gabrie@duel.com.br

from settings import EXIT_COMMAND, EXIT_COMMAND_ACK, \
    CONNECTION_CLOSE_SERVER, CONNECTION_CLOSE, THREAD_CONN
import base64
import socket
import sys
import threading

class ClientThread(threading.Thread):
    
    def __init__(self, host="127.0.0.1", porta=8001):
        # Pega host e porta
        self.porta = porta
        self.host = host
        threading.Thread.__init__(self)
        
    def run(self):
        # Cria socket
        cliente = socket.socket()
        # Conecta
        cliente.connect((self.host, int(self.porta)))

        # Abre thread e envia conexão ativa para interagir com o servidor 
        conn = ConnectionThread(cliente, self.host)
        conn.setName("%s%s:%s" % (THREAD_CONN, self.host, self.porta))
        conn.start()

        # Fica em loop esperando que alguem digite algo 
        # para enviar ao servidor
        try:
            while True:
                msg = raw_input(">")
                cliente.send(base64.b64encode(msg))
        except:
            pass

class ConnectionThread(threading.Thread):

    def __init__(self, cliente, host):
        # Pega conexao ativa e host
        self.cliente = cliente
        self.host = host
        threading.Thread.__init__(self)
        
    def run(self):
        while True:
            # Fica em loop esperando resposta do cliente
            r = base64.b64decode(self.cliente.recv(1024))
            if r <> "":
                if not r.upper() in (EXIT_COMMAND, EXIT_COMMAND_ACK):
                    # Imprimindo na tela
                    print "%s: %s" % (self.host, r)
                else:
                    # Se entrou aqui é porque o servidor pediu 
                    # para encerrar o chat
                    self.cliente.send(base64.b64encode(EXIT_COMMAND_ACK))
                    self.cliente.close()
                    if r != EXIT_COMMAND_ACK:
                        print CONNECTION_CLOSE_SERVER
                    else:
                        print CONNECTION_CLOSE
                        
                    sys.exit(0)

                