#!/usr/bin/env python
# encoding: utf-8
# author: Gabriel Fernandes - gabrie@duel.com.br

from settings import EXIT_COMMAND_ACK, EXIT_COMMAND, CONNECTION_CLOSE_CLIENT, \
    CONNECTION_CLOSE, THREAD_CONN
import base64
import socket
import sys
import threading

class ServerThread(threading.Thread):
    
    def __init__(self, porta=8001):
        # Pega porta
        self.porta = porta
        # Pega IP
        self.host = socket.gethostbyname(socket.gethostname())
        threading.Thread.__init__(self)
        
    def run(self):
        # Cria socket
        server = socket.socket()
        # Pôe para escutar em host:porta
        server.bind((self.host, int(self.porta)))
        server.listen(1)
        # Passa a aceitar conexão
        # bloqueia até alguem conectar
        sc, addr = server.accept()
        
        # Abre thread e envia conexão ativa para interagir com o cliente 
        conn = ConnectionThread(sc)
        conn.setName("%s%s:%s" % (THREAD_CONN, addr[0], addr[1]))
        conn.start()
        
        while True:
            # Fica em loop esperando resposta do cliente
            r = base64.b64decode(sc.recv(1024))
            if not r.upper() in (EXIT_COMMAND, EXIT_COMMAND_ACK):
                # Imprimindo na tela
                print "%s: %s" % (addr[0], r)
            else:
                # Se entrou aqui é porque o cliente pediu 
                # para encerrar o chat
                sc.send(base64.b64encode(EXIT_COMMAND_ACK))
                sc.close()
                server.close()
                if r != EXIT_COMMAND_ACK:
                    print CONNECTION_CLOSE_CLIENT
                else:
                    print CONNECTION_CLOSE
                    
                sys.exit(0)
        
class ConnectionThread(threading.Thread):

    def __init__(self, sc):
        # Pega conexao ativa
        self.sc = sc
        threading.Thread.__init__(self)
        
    def run(self):
        # Fica em loop esperando que alguem digite algo 
        # para enviar ao cliente
        try:
            
            while True:
                msg = raw_input(">")
                self.sc.send(base64.b64encode(msg))
        except:
            pass