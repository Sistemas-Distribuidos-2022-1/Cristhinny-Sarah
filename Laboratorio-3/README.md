# Sobre o SGBD usado

Eu utilizei o Postgres (PgAdmin4) para gerenciar o Banco de Dados criado para esse laboratório (arquivo `bancodedados.sql`).

Portanto, para funcionar no seu computador, é necessário mudar a senha da conexão com o banco de dados (linha 23 do arquivo `servidorBancoDeDados.py`):

`con = psycopg2.connect(host='localhost', database='SistemasDistribuidos', user='postgres', password='suaSenha')`