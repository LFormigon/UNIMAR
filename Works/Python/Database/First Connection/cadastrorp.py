import mysql.connector

#Cria uma conexão com o banco de dados

conexao = mysql.connector.connect(
    host= "localhost",
    user="root",
    password ="",
    database="loja" #nome do banco de dados a ser utilizado
)


cursor = conexao.cursor()

qtd_camisetas = int(input("Quantas camisetas deseja cadastrar?: "))
marca_camiseta = []
cor_camiseta = []
tamanho_camiseta = []
preco_camiseta = []

for i in range(qtd_camisetas):
    print("Registro de Camisetas", i+1)
    marca = input("Digite a marca da camiseta: ")
    cor = input("Digite a cor da camiseta: ")
    tamanho = input("Digite o tamanho da camiseta: ")
    preco = float(input("Digite o valor da camiseta: "))

    # Adicionando dados a lista

    marca_camiseta.append(marca)
    cor_camiseta.append(cor)
    tamanho_camiseta.append(tamanho)
    preco_camiseta.append(preco)
    
    # Inserindo os dados na tabela

    camis = "INSERT INTO camisetas (marca, cor, tamanho, preco) VALUES (%s, %s, %s, %s)"
    descricao = (marca, cor, tamanho, preco)
    cursor.execute(camis, descricao)
    conexao.commit()

for indice, marca in enumerate(marca_camiseta):
    print("Marca da roupa: ", marca, "\ncor: ", cor_camiseta
    [indice],
            "\nPreço: ", preco_camiseta[indice])
    
#Encerrando conexão

cursor.close()
conexao.close()
    




