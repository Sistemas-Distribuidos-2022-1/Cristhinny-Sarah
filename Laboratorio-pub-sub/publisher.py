import zmq, time

HOST = '127.0.0.1'    # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor está
loop = True

contexto = zmq.Context()
socket = contexto.socket(zmq.PUB)
conexao = "tcp://" + HOST + ":" + str(PORT)

socket.bind(conexao)

print("Servidor funcionando!")
print("Iniciar envio de mensagens? 0 (sim), 1 (nao)")
resposta = input() 

if(resposta == 1):
    loop = False 

while(loop):
    time.sleep(5)
    print("Publicando problema 1")
    socket.send_string("SALARIOS " + "Joao " + "programador " + str(1000))

    time.sleep(5)
    print("Publicando problema 2")
    socket.send_string("MAIORIDADE " + "Maria " + "feminino " + str(12))

    time.sleep(5)
    print("Publicando problema 3")
    socket.send_string("MEDIA " + str(7.1) + " " + str(8.0) + " " + str(1.5))

    time.sleep(5)
    print("Publicando problema 4")
    socket.send_string("PESOIDEAL " + str(2.75) + " " + "masculino")

    time.sleep(5)
    print("Publicando problema 5")
    socket.send_string("CATEGORIA " + str(30))

    time.sleep(5)
    print("Publicando problema 6")
    socket.send_string("SALARIOBRUTO " + "Julinho " + "A " + str(5000) + " " + str(20))

    time.sleep(5)
    print("Publicando problema 7")
    socket.send_string("APOSENTADORIA " + str(50) + " " + str(15))

    time.sleep(5)
    print("Publicando problema 8")
    socket.send_string("SALDOMEDIO " + str(10000))
#--------------------------------------------------------------------------

socket.close()
contexto.term()