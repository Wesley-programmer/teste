from datetime import datetime
produtos = []
conbd = conexaobd.conexao()

while True:
        print("Menu")
        print("1. Atualizar Produto")
        print("2. Atualizar Fornecedor")
        print("3. Atualizar Cliente")
        print("4. Atualizar Funcionário")
        print("5. Atualizar a Promoção")
        print("6. Voltar ao Menu Principal")

        atualizar_opcao = input("Escolha uma opção: ")

        if atualizar_opcao == '1':
            Nome = input("Digite o novo nome do produto: ")
            Descricao = input("Digite a nova descrição do produto: ")
            Preco = float(input("Digite o novo preço do produto: "))
            novoNome = input("Digite o nome do produto: ")
            bd.atualizarprodutos(conbd, Nome, Descricao, Preco, novoNome)


        elif atualizar_opcao == '2':
            Nome = input("Digite o novo nome do Fornecedor: ")
            Contato = input("Digite o novo contato do Fornecedor: ")
            Endereco = input("Digite o novo endereço do Fornecedor: ")
            novoNome = input("Digite o nome do Fornecedor: ")
            bd.atualizarfornecedores(conbd, Nome, Contato, Endereco, novoNome)

        elif atualizar_opcao == '3':
            Nome = input("Digite o novo nome do Cliente: ")
            Sobrenome = input("Digite o novo sobrenome do Cliente: ")
            Endereco = input("Digite o novo endereço do Cliente: ")
            Cidade = input("Digite o novo nome da cidade: ")
            CodigoPostal = input("Digite o código postal: ")
            novoNome = input("Digite o nome do Cliente: ")
            bd.atualizarclientes(conbd, Nome, Sobrenome, Endereco, Cidade, CodigoPostal, novoNome)
           
        elif atualizar_opcao == '4':
            Nome = input("Digite o novo nome do funcionário: ")
            Cargo = input("Digite o novo cargo do funcionário: ")
            Departamento = input("Digite o novo departamento do funcionário: ")
            novoNome = input("Digite o nome do Funcionário: ")
            bd.atualizarfuncionarios(conbd, Nome, Cargo, Departamento, novoNome)
            
        elif atualizar_opcao == '5':
            Nome = input("Digite o novo nome da promoção: ")
            Descricao = input("Digite a descrição: ")
            DataInicio = input("Digite a data inicial: ")
            DataFim = input("Digite a data final: ")
            novoNome = input("Digite o nome da promoção: ")
            DataInicio = datetime.strptime(DataInicio, '%d-%m-%y').strftime('%y-%m-%d')
            DataFim = datetime.strptime(DataFim, '%d-%m-%y').strftime('%y-%m-%d') 
            bd.atualizarpromocoes(conbd, Nome, Descricao, DataInicio, DataFim, novoNome)

        else:
            print("Opção inválida! Tente novamente.")

        #comentário
