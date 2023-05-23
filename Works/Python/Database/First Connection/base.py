import mysql.connector

#Cria uma conexão com o banco de dados
conexao = mysql.connector.connect(
    host= "localhost",
    user="root",
    password ="",
    database="loja" #nome do banco de dados a ser utilizado
)

#Criar um Cursos para executar comandos SQL

'''cursor = conexao.cursor()'''

#Criar uma tabela
'''cursor.execute("CREATE TABLE camisetas (id INT AUTO_INCREMENT PRIMARY KEY,marca VARCHAR(50),cor VARCHAR(50),tamanho VARCHAR(10),preco DECIMAL(8, 2))")
'''
