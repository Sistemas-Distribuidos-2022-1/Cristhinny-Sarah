import socket
import _thread

HOST = 'localhost'     # Endereco IP do Servidor
PORT = 50000            # Porta que o Servidor está

mensagem = ''

# Função chamada quando uma nova thread for iniciada
def conectado(conexao, cliente):
  print('\nCliente conectado: ', cliente)

  # Recebendo as mensagens através da conexão
  dados = conexao.recv(4096).decode()
 
  print('\nCliente..:', cliente)
  print('Mensagem recebida:', dados)
  if dados == None:
    return
  # para o cliente em python, comentar a linha seguinte
  dados = dados[2:]
  
  if int(dados[0]) == 1:
    problema, nome, cargo, salario = dados.split('$')
    salario = float(salario)
    
    # Fazendo o reajuste do salario
    if cargo == "operador":
      salario += (salario*20)/100
    if cargo == "programador":
      salario += (salario*18)/100
    mensagem = "Salario atualizado de " + nome + ": " + str(salario)
  
  if int(dados[0]) == 2:
    problema, nome, sexo, idade = dados.split('$')
    
    # Analisando a maioridade
    if sexo == "feminino":
      if int(idade) >= 21:
        mensagem = "Maioridade atingida!"
      else:
        mensagem = "Maioridade nao atingida ainda!"
    else:
      if int(idade) >= 18:
        mensagem = "Maioridade atingida!"
      else:
        mensagem = "Maioridade não atingida ainda!"
  
  if int(dados[0]) == 3:
    problema, N1, N2, N3 = dados.split('$')
    mediaN1N2 = (float(N1) + float(N2))/2 

    # Analisando se o aluno foi aprovado
    if mediaN1N2 >= 7.0:
      mensagem = "O aluno foi aprovado!"
    else:
      if mediaN1N2 > 3.0 and mediaN1N2 < 7.0:
        if (mediaN1N2 + float(N3))/2 >= 5.0:
          mensagem = "O aluno foi aprovado!"
        else:
          mensagem = "O aluno foi reprovado!"
      else:
        mensagem = "O aluno foi reprovado!"

  if int(dados[0]) == 4:    
    problema, altura, sexo = dados.split('$')
    pesoIdeal = 0.00

    # Analisando o peso ideal
    if sexo == "feminino":
      pesoIdeal = (62.1*float(altura)) - 44.7
    else:
      pesoIdeal = (72.7*float(altura)) - 58

    mensagem = "Peso ideal para o sexo " + sexo + " e altura " + altura + ": " + str(pesoIdeal)
  
  if int(dados[0]) == 5:
    problema, idade = dados.split('$')
    idade = int(idade)
    
    # Analisando a categoria da pessoa
    if idade >= 0 and idade <= 4:
      mensagem = "Sem categoria!"
    else:
      if idade >= 5 and idade <= 7:
        mensagem = "Categoria: Infantil A"
      else:
        if idade >= 8 and idade <= 10:
          mensagem = "Categoria: Infantil B"
        else:
          if idade >= 11 and idade <= 13:
            mensagem = "Categoria: Juvenil A"
          else:
            if idade >= 14 and idade <= 17:
              mensagem = "Categoria: Juvenil B"
            else:
              mensagem = "Categoria: Adulto"

  if int(dados[0]) == 6:
    problema, nome, nivel, salarioBruto, numeroDeDependentes = dados.split('$')
    salarioBruto = float(salarioBruto)
    numeroDeDependentes = int(numeroDeDependentes)
    salarioLiquido = 0.00

    # Fazendo o reajuste do salario
    if nivel == "A":
      if numeroDeDependentes != 0:
        salarioLiquido = salarioBruto - (salarioBruto*8)/100
      else:
        salarioLiquido = salarioBruto - (salarioBruto*3)/100

    if nivel == "B":
      if numeroDeDependentes != 0:
        salarioLiquido = salarioBruto - (salarioBruto*10)/100
      else:
        salarioLiquido = salarioBruto - (salarioBruto*5)/100

    if nivel == "C":
      if numeroDeDependentes != 0:
        salarioLiquido = salarioBruto - (salarioBruto*15)/100
      else:
        salarioLiquido = salarioBruto - (salarioBruto*8)/100

    if nivel == "D":
      if numeroDeDependentes != 0:
        salarioLiquido = salarioBruto - (salarioBruto*17)/100
      else:
        salarioLiquido = salarioBruto - (salarioBruto*10)/100         
    
    mensagem = "Salario Liquido: " + str(salarioLiquido)

  if int(dados[0]) == 7:
    problema, idade, tempoDeServico = dados.split('$')
    idade = int(idade)
    tempoDeServico = int(tempoDeServico)

    # Analisando se o Funcionario pode aposentar
    if idade >= 60 and tempoDeServico >= 25:
      mensagem = "O funcinario pode se aposentar!"
    else:
      if idade >= 65 and tempoDeServico >= 30:
        mensagem = "O funcinario pode se aposentar!"
      else:
        mensagem = "O funcinario nao pode se aposentar ainda!"

  if int(dados[0]) == 8:
    problema, saldoMedio = dados.split('$')
    saldoMedio = float(saldoMedio)
    credito = 0.00

    # Analisando se o cliente receberá crédito
    if saldoMedio >= 0 and saldoMedio <= 200:
      credito = 0.00
    else:
      if saldoMedio >= 201 and saldoMedio <= 400:
        credito = (saldoMedio*20)/100
      else:
        if saldoMedio >= 401 and saldoMedio <= 600:
          credito = (saldoMedio*30)/100
        else:
          credito = (saldoMedio*40)/100
    
    mensagem = "O Banco aprovou um credito especial de " + str(credito) + "!"

  # enviando a mensagem para o cliente
  conexao.send(str(mensagem).encode())
  print('\nFinalizando conexao do cliente ', cliente)
  conexao.close()
  _thread.exit()

# Para criar o socket precisamos passar a família de protocolos
# AF_INET = IPV4
# sock_STREAM = TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# o servidor estará linkado com a respectiva porta e HOST definidas anteriormente
server.bind((HOST, PORT))

# colocando o Socket em modo passivo
server.listen(1)

print('\nServidor TCP concorrente iniciado no IP', HOST, 'na porta', PORT)

while True:
  # Aceitando uma nova conexão
  conexao, endereco = server.accept()
  print('\nNova thread iniciada para essa conexão')
  
  # Abrindo uma thread para a conexão
  _thread.start_new_thread(conectado, tuple([conexao, endereco]))

# Fechando a conexão com o Socket
tcp.close()