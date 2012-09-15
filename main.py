#!/usr/bin/env python
# encoding: utf-8
# author: Gabriel Fernandes - gabrie@duel.com.br

from client import ClientThread
from server import ServerThread
from settings import THREAD_SERVER, THREAD_CLIENT
import sys

if __name__ == "__main__":

    if len(sys.argv) > 1:
        if sys.argv[1] == "-c" or sys.argv[1] == "--cliente":
            # Se entrou aqui é porque deve subir um cliente
            if len(sys.argv) == 3:
                # Pega argumentos ip:porta da linha de comando
                server = sys.argv[2]
                server = server.split(":")
                # Cria thread cliente para ip:porta informados
                # na linha de comando
                server = ClientThread(server[0],server[1])
                server.setName(THREAD_CLIENT)
                server.start()
            else:
                print "forneça ip:porta do servidor."
            
        elif sys.argv[1] == "-s" or sys.argv[1] == "--servidor":
            # Se entrou aqui é porque deve subir um servidor    
            if len(sys.argv) == 3:
                # Pega argumento porta da linha de comando
                porta = sys.argv[2]
                # Cria thread servidor para port
                server = ServerThread(porta)
                server.setName(THREAD_SERVER)
                server.start()
            else:
                print "forneça uma porta para escutar."
                
    else:
        print \
        """

            Ajuda para executar o chat_socket:
            
            Como Cliente: 
            python main.py --cliente IP_SERVIDOR:PORTA
            
            Como Servidor: 
            python main.py --servidor PORTA
            
        """
