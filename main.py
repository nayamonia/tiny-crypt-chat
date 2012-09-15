# encoding: utf-8
"""
The MIT License (MIT)

Copyright (c) 2012 Gabriel Fernandes

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

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
