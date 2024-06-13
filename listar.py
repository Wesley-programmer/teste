import bd
import conexaobd
conbd = conexaobd.conexao()

def MenuListar():
    while True:
            print("1. Menu Listar")
            print("2. Listar Produtos")
            print("3. Listar Fornecedores")
            print("4. Listar Promoções")
            print("5. Listar Funcionários")
            print("6. Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                bd.Listarprodutos(conbd)
            elif opcao == '2':
                bd.Listarfornecedores(conbd)
            elif opcao == '3':
                bd.Listarclientes(conbd)
            elif opcao == '4':
                bd.Listarpromocoes(conbd)
            elif opcao == '5':
                bd.Listarfuncionarios(conbd)   
            else:
                print("Opção Inválida!")



MenuListar()
            