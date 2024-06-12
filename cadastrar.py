import b
import conexaobd
import tkinter as tk
from datetime import datetime, date
hoje = date.today()
produtos = []
conbd = conexaobd.conexao()

while True:
    print("Menu")
    print("1. Cadastrar o Produto")
    print("2. Cadastrar o Fornecedor")
    print("3. Cadastrar o Cliente")
    print("4. Cadastrar o Funcionario")
    print("5. Cadastrar a Promoção")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        Nome = input("Digite o nome do produto: ")
        Descricao = input("Digite a descrição do produto: ")
        Preco = float(input("Digite o preço do produto: "))
        Quantidade = int(input("Digite a quantidade do produto: "))
        bd.cadprodutos(conbd,Nome,Descricao,Preco,Quantidade)
        print("Hoje: ")
    
    elif opcao == '2':
        Nome = input("Digite o nome do fornecedor: ")
        Contato = input("Digite o contato do fornecedor: ")
        Endereco = input("Digite o endereço do fornecedor: ")
        bd.cadfornecedores(conbd,Nome,Contato,Endereco)
    
    elif opcao == '3':
        Nome = input("Digite o nome do cliente: ")
        Sobrenome = input("Digite o sobrenome do cliente: ")
        Endereco = input("Digite o endereço do cliente: ")
        Cidade = input("Digite o nome da cidade do cliente: ")
        CodigoPostal = input("Digite o Código Postal: ")
        bd.cadclientes(conbd,Nome,Sobrenome,Endereco,Cidade,CodigoPostal)
    
    elif opcao == '4':
        Nome = input("Digite o nome do funcionário: ")
        Cargo = input("Digite o cargo do funcionário: ")
        Departamento = input("Digite o endereço do departamento do funcionário: ")
        bd.cadfuncionarios(conbd,Nome,Cargo,Departamento)
        
    elif opcao == '5':
        Nome = input("Digite o nome da promoção: ")
        Descricao = input("Digite a descrição: ")
        DataInicio = input("Digite a data inicial: ")
        DataFim = input("Digita a data de encerramento: ")
        DataInicio = datetime.strptime(DataInicio, '%d-%m-%y').strftime('%y-%m-%d')
        DataFim = datetime.strptime(DataFim, '%d-%m-%y').strftime('%y-%m-%d')                                                            
        print(DataInicio)
        print(DataFim)
        bd.cadpromocoes(conbd,Nome,Descricao,DataInicio,DataFim)
    else:
        print("Opção inválida! Tente novamente.")
