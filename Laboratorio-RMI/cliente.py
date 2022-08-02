import Pyro5.api

problemas = Pyro5.api.Proxy("PYRONAME:exemplos.problemas")

while True:
  print("\nEscolha um problema: ")
  print("1: Reajuste de Salario")
  print("2: Maioridade")
  print("3: Media de Notas")
  print("4: Peso Ideal")
  print("5: Classificar Nadadores")
  print("6: Salario Liquido")
  print("7: Aposentadoria")
  print("8: Credito Especial")
  problema = input("0: Sair\n")
  problema = int(problema)

  if problema == 0:
    break
  
  if problema == 1:
    # coletando informações do usuário
    nome = input("Entre com o nome: ")
    cargo = input("Entre com o cargo: ")
    salario = int(input("Entre com o salario: "))
    
    mensagem = problemas.salarios(nome, cargo, salario)
    print(mensagem)
  
  if problema == 2:
    # coletando informações do usuário
    nome = input("Entre com o nome: ")
    sexo = input("Entre com o sexo: ")
    idade = int(input("Entre com a idade: "))

    mensagem = problemas.maioridade(nome, sexo, idade)
    print(mensagem)

  if problema == 3:
    # coletando informações do usuário
    N1 = float(input("Entre com a N1: "))
    N2 = float(input("Entre com a N2: "))
    N3 = float(input("Entre com a N3: "))

    mensagem = problemas.media(N1, N2, N3)
    print(mensagem)

  if problema == 4:
    # coletando informações do usuário
    altura = input("Entre com a altura da pessoa: ")
    sexo = input("Entre com o sexo da pessoa: ")

    mensagem = problemas.pesoIdeal(altura, sexo)
    print(mensagem)
  
  if problema == 5:
    # coletando informações do usuário
    idade = int(input("Entre com a idade da pessoa: "))
    
    mensagem = problemas.categoria(idade)
    print(mensagem)
  
  if problema == 6:
    # coletando informações do usuário
    nome = input("Entre com o nome: ")
    nivel = input("Entre com o nivel: ")
    salarioBruto = float(input("Entre com o salario bruto: "))
    numeroDeDependentes = int(input("Entre com o números de dependentes do funcionário: "))
    
    mensagem = problemas.salarioLiquido(nome, nivel, salarioBruto, numeroDeDependentes)
    print(mensagem)

  if problema == 7:
    # coletando informações do usuário
    idade = int(input("Entre com a idade do funcionario: "))
    tempoDeServico = int(input("Entre com o tempo de serviço em anos: "))
    
    mensagem = problemas.aposentadoria(idade, tempoDeServico)
    print(mensagem)

  if problema == 8:
    # coletando informações do usuário
    saldoMedio = float(input("Entre com o saldo medio do cliente: "))
    
    mensagem = problemas.saldoMedio(saldoMedio)
    print(mensagem)