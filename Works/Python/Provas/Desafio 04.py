# -*- coding: utf-8 -*-
"""Cópia de Olá, este é o Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SN-qqVxWgZlUNsY7mDPbxUMwXr330XOy
"""



estoque = {}

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição: ")
    preco = input("Digite o preço do produto: ")
    quantidade = input("Digite a quantidade disponivel em estoque do produto: ")
    estoque[nome] = {"descricao": descricao, "preco": preco, "quantidade": quantidade}
    print("Produto adicionado")

def remover_produto():
    nome = input("Digite o nome do produto que deseja retirar: ")
    if nome in estoque:
        del estoque[nome]
        print("Produto retirado")
   
    else:
        print("Produto não encontrado no estoque")

def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ")
    if nome in estoque:
        opcao = input("O que você deseja alterar? \n1 para descrição \n2 preço  \n3 quantidade ")
        if opcao == "1":
            descricao = input("Digite a nova descrição do produto: ")
            estoque[nome]["descricao"] = descricao
        elif opcao == "2":
            preco = input("Digite o novo preço do produto: ")
            estoque[nome]["preco"] = preco
        elif opcao == "3":
            quantidade = input("Digite a nova quantidade em estoque do produto: ")
            estoque[nome]["quantidade"] = quantidade
       
        else:
            print("Opção inválida. Tente novamente.")
        print("Produto atualizado com sucesso")
   
    else:
        print("Produto não encontrado no estoque.")

def exibir_produtos():
    print("Lista de produtos:")
    for nome, produto in estoque.items():
        print("Nome:", nome)
        print("Descrição:", produto["descricao"])
        print("Preço:", produto["preco"])
        print("Quantidade em estoque:", produto["quantidade"])

opcoes = {
    "1": adicionar_produto,
    "2": remover_produto,
    "3": atualizar_produto,
    "4": exibir_produtos,
    "5": exit
}

while True:
    print("Selecione uma opção:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Atualizar produto")
    print("4. Exibir produtos")
    print("5. Sair")
    
    opcao = input("Opção: ")
    
    func = opcoes.get(opcao)
    if func:
        func()
    
    else:
        print("Opção inválida")