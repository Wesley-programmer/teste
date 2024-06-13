from mysql.connector import Error
import tkinter as tk
from datetime import datetime, date




def cadprodutos(conbd,Nome,Descricao,Preco,quantEstoque):
    
    mycursor= conbd.cursor()
    
    sql = "INSERT INTO produtos(Nome,Descricao,Preco) values(%s,%s,%s)"
    val = (Nome,Descricao,Preco)    
    mycursor.execute(sql,val)

    ID_Produto = mycursor.lastrowid
    sql1 = "INSERT INTO estoque (ID_Produto, quantidade) VALUES (%s,%s)"
    val1 = (ID_Produto, quantEstoque)
    
    mycursor.execute(sql1, val1) 
    conbd.commit()
    print("Produto Cadastrado com Sucesso: ")
    mycursor.close()



def cadfornecedores(conbd,Nome,Contato,Endereco):
    
    mycursor= conbd.cursor()
    
    sql = "INSERT INTO fornecedores (Nome,Contato,Endereco) values(%s,%s,%s)"
    val = (Nome,Contato,Endereco)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('Fornecedor cadastrado com sucesso')
    mycursor.close()

def cadclientes(conbd,Nome,Sobrenome,Endereco,Cidade,CodigoPostal):
    
    mycursor= conbd.cursor()
    
    sql = "INSERT INTO clientes(Nome,Sobrenome,Endereco,Cidade,CodigoPostal) values(%s,%s,%s,%s,%s)"
    val = (Nome,Sobrenome,Endereco,Cidade,CodigoPostal)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('Cliente cadastrado com sucesso')
    mycursor.close()

def cadpromocoes(conbd,Nome,Descricao,DataInicio,DataFim):
    mycursor = conbd.cursor()
    sql = "INSERT INTO promocoes(Nome,Descricao,DataInicio,DataFim) values (%s,%s,%s,%s)"
    valores=(Nome,Descricao,DataInicio,DataFim)
    mycursor.execute(sql, valores)
    conbd.commit()
    print("promoções cadastrado com sucesso")

    mycursor.close()

def cadfuncionarios(conbd,Nome,Cargo,Departamento):
    
    mycursor= conbd.cursor()
    
    sql = "INSERT INTO funcionarios(Nome,Cargo,Departamento) values(%s,%s,%s)"
    val = (Nome,Cargo,Departamento)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('Funcionario cadastrado com sucesso')
    mycursor.close()

    
def obterprodutosID(conbd, nome):
    try:
        with conbd.cursor() as cursor:
            sql = 'SELECT ID_Produto FROM produtos WHERE Nome = %s'
            cursor.execute(sql, (nome,))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]
            else:
                print(f"Produto com nome '{nome}' não encontrado.")
                return None
    except Error as e:
        print(f"Ocorreu um erro ao obter o ID do produto: {e}")
        return None


def deletarprodutos(conbd, nome_produto):
    try:
        produto_id = obterprodutosID(conbd, nome_produto)
        if not produto_id:
            return
        
        conbd.start_transaction()
        with conbd.cursor() as cursor:
            sql_detalhes_pedido = 'DELETE FROM detalhespedido WHERE ID_Produto = %s'
            cursor.execute(sql_detalhes_pedido, (produto_id,))
        with conbd.cursor() as cursor:
            sql_estoque = 'DELETE FROM estoque WHERE ID_Produto = %s'
            cursor.execute(sql_estoque, (produto_id,))
        with conbd.cursor() as cursor:
            sql_produto = 'DELETE FROM produtos WHERE ID_Produto = %s'
            cursor.execute(sql_produto, (produto_id,))
        conbd.commit()
        print("Produto e suas referências deletadas com sucesso")

    except Error as e:
        conbd.rollback()
        print(f"Ocorreu um erro ao deletar o produto: {e}")

    finally:
        conbd.close()


def delfornecedores(conbd,Nome):
    
    mycursor= conbd.cursor()
    
    sql = "DELETE FROM fornecedores WHERE Nome = %s"
    val = (Nome,)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('Fornecedor deletado com sucesso')
    mycursor.close()

def delclientes(conbd,Nome):
    
    mycursor= conbd.cursor()
    
    sql = "DELETE FROM clientes WHERE Nome = %s"
    val = (Nome,)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('Cliente deletado com sucesso')
    mycursor.close()

def delpromocoes(conbd,Nome):
    
    mycursor= conbd.cursor()
    
    sql = "DELETE FROM promocoes WHERE Nome = %s"
    val = (Nome,)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('Cliente deletado com sucesso')
    mycursor.close()

def delfuncionarios(conbd,Nome):
    
    mycursor= conbd.cursor()
    
    sql = "DELETE FROM funcionarios WHERE Nome = %s"
    val = (Nome,)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('Funcionario deletado com sucesso')
    mycursor.close()



def atualizarprodutos(conbd,Nome,Descricao,Preco,novoNome):
    mycursor = conbd.cursor()
    sql = "UPDATE produtos SET Nome = %s, Descricao = %s, Preco = %s  WHERE Nome = %s"  
    valores = (Nome,Descricao,Preco,novoNome)  
    mycursor.execute(sql, valores)
    conbd.commit()
    print("Produto atualizado com sucesso")
   
    mycursor.close()

def atualizarclientes(conbd, Nome, Sobrenome, Endereco, Cidade, CodigoPostal, novoNome):
    mycursor = conbd.cursor()
    sql = "UPDATE clientes SET Nome = %s, Sobrenome = %s, Endereco = %s, Cidade = %s, CodigoPostal = %s  WHERE Nome = %s"  
    valores = (Nome, Sobrenome, Endereco, Cidade, CodigoPostal, novoNome)  
    mycursor.execute(sql, valores)
    conbd.commit()
    print("Cliente atualizado com sucesso")
   
    mycursor.close()

def atualizarfuncionarios(conbd, Nome, Cargo, Departamento, novoNome):
    mycursor = conbd.cursor()
    sql = "UPDATE funcionarios SET Nome = %s, Cargo = %s, Departamento = %s WHERE Nome = %s"  
    valores = (Nome, Cargo, Departamento, novoNome)  
    mycursor.execute(sql, valores)
    conbd.commit()
    print("Funcionário atualizado com sucesso")
   
    mycursor.close()

def atualizarfornecedores(conbd, Nome, Contato, Endereco, novoNome):
    mycursor = conbd.cursor()
    sql = "UPDATE fornecedores SET Nome = %s, Contato = %s, Endereco = %s WHERE Nome = %s"  
    valores = (Nome, Contato, Endereco, novoNome)  
    mycursor.execute(sql, valores)
    conbd.commit()
    print("Fornecedor atualizado com sucesso")
   
    mycursor.close()

def atualizarpromocoes(conbd, Nome, Descricao, DataInicio, DataFim, novoNome):
    mycursor = conbd.cursor() 
    sql = "UPDATE promocoes SET Nome = %s, Descricao = %s, DataInicio = %s, DataFim = %s  WHERE Nome = %s"  
    valores = (Nome, Descricao, DataInicio, DataFim, novoNome)  
    mycursor.execute(sql, valores)
    conbd.commit()
    print("Promoção atualizada com sucesso")
    mycursor.close()


def Listarprodutos(conbd):
    mycursor = conbd.cursor()
    sql = "SELECT * FROM produtos" 
    mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in (listagem):
        print(i)
    mycursor.close()

def Listarclientes(conbd):
    mycursor = conbd.cursor()
    sql = "SELECT * FROM clientes" 
    mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in (listagem):
        print(i)
    mycursor.close()

def Listarfornecedores(conbd):
    mycursor = conbd.cursor()
    sql = "SELECT * FROM fronecedores" 
    mycursor. execute(sql)
    listagem = mycursor.fetchall()
    for i in (listagem):
        print(i)
    mycursor.close()

def Listarpromocoes(conbd):
    mycursor = conbd.cursor()
    sql = "SELECT * FROM promocoes" 
    mycursor. execute(sql)
    listagem = mycursor.fetchall()
    for i in (listagem):
        print(i)
    mycursor.close()

def Listarfuncionarios(conbd):
    mycursor = conbd.cursor()
    sql = "SELECT * FROM funcionarios" 
    mycursor. execute(sql)
    listagem = mycursor.fetchall()
    for i in (listagem):
        print(i)
    mycursor.close()