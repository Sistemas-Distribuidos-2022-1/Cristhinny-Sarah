from xmlrpc.server import SimpleXMLRPCServer

PORT = 8000
HOST = "localhost"

def salarios(nome, cargo, salario):
  salario = float(salario)
  
  # Fazendo o reajuste do salario
  if cargo == "operador":
    salario += (salario*20)/100
  if cargo == "programador":
    salario += (salario*18)/100
  mensagem = "Salario atualizado de " + nome + ": " + str(salario)
  return mensagem

def maioridade(nome, sexo, idade):
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
  return mensagem

def media(N1, N2, N3):
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
  return mensagem

def pesoIdeal(altura, sexo):
  pesoIdeal = 0.00

  # Analisando o peso ideal
  if sexo == "feminino":
    pesoIdeal = (62.1*float(altura)) - 44.7
  else:
    pesoIdeal = (72.7*float(altura)) - 58

  mensagem = "Peso ideal para o sexo " + sexo + " e altura " + str(altura) + ": " + str(pesoIdeal)
  return mensagem

def categoria(idade):
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
  return mensagem

def salarioLiquido(nome, nivel, salarioBruto, numeroDeDependentes):
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
  return mensagem

def aposentadoria(idade, tempoDeServico):
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
  return mensagem

def saldoMedio(saldoMedio):
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
  return mensagem

server = SimpleXMLRPCServer((HOST, PORT))

print("Escutando a porta 8000...")

server.register_function(salarios, "salarios")
server.register_function(maioridade, "maioridade")
server.register_function(media, "media")
server.register_function(pesoIdeal, "pesoIdeal")
server.register_function(categoria, "categoria")
server.register_function(salarioLiquido, "salarioLiquido")
server.register_function(aposentadoria, "aposentadoria")
server.register_function(saldoMedio, "saldoMedio")

server.serve_forever()