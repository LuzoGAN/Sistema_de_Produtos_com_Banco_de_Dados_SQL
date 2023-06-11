# Importar o modulo pyodbc para conexão com banco de dados
import pyodbc

# Importar o módulo tkinter para construção de interfaces gráficas
from tkinter import *

# Importar a classe ttk do módulo tkinter
from tkinter import ttk
janela_principal = Tk()
janela_principal.configure(bg="#F5F5F5")

dadosconexao = ("Driver={SQLite3 ODBC Driver}; Server=localhost; Database=Projeto_compras.db")
conexao = pyodbc.connect(dadosconexao)
#Ferramenta para executar os comandos em SQL
cursor = conexao.cursor()


conexao = pyodbc.connect(dadosconexao)
cursor = conexao.cursor()

print("Conectado com sucesso!")


# Função para cadastrar o Produto
def cadastrar():
    # criar uma nova janela para cadastrar o produto
    janela_cadastrar = Toplevel(janela)
    janela_cadastrar.title("Cadastrar Produto")

    janela_cadastrar.configure(bg="#F5F5F5")

    largura_janela = 450
    altura_janela = 300

    largura_tela = janela_cadastrar.winfo_screenwidth()
    altura_tela = janela_cadastrar.winfo_screenheight()

    pos_x = (largura_janela // 2) - (largura_janela // 2)
    pos_y = (altura_janela // 2) - (altura_janela // 2)

    janela_cadastrar.geometry("{}x{}+{}+{}".format(largura_janela, altura_janela, pos_x, pos_y))

    # Adiciona boradas para cada campo de entrada
    estilo_borda = {"borderwidth": 2, "relief": "groove"}

    Label(janela_cadastrar, text="Nome do Produto: ", font=("Arial", 12), bg="#FFFFFF").grid(row=0, column=0, padx=10,
                                                                                             pady=10, stick="W")
    nome_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
    nome_produto_cadastrar.grid(row=0, column=1, padx=10, pady=10)

    Label(janela_cadastrar, text="Descrição: ", font=("Arial", 12), bg="#FFFFFF").grid(row=1, column=0, padx=10,
                                                                                       pady=10, stick="W")
    descricao_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
    descricao_produto_cadastrar.grid(row=1, column=1, padx=10, pady=10)

    Label(janela_cadastrar, text="Preço do Produto: ", font=("Arial", 12), bg="#FFFFFF").grid(row=2, column=0, padx=10,
                                                                                              pady=10, stick="W")
    preço_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
    preço_produto_cadastrar.grid(row=2, column=1, padx=10, pady=10)

    def salvar_dados():
        # Cria um tupla com os valores
        novo_prodouto_cadastrar = (
        nome_produto_cadastrar.get(), descricao_produto_cadastrar.get(), preço_produto_cadastrar.get())
        cursor.execute("INSERT INTO Produtos (Produto, Descricao, Preco) Values (?, ?, ?)", novo_prodouto_cadastrar)
        conexao.commit()

        print("Dados Cadastrados com sucesso!")

        cursor.close()
        conexao.close()

        janela_cadastrar.destroy()

    botao_salvar_dados = Button(janela_cadastrar, text="Salvar", font=("Arial", 12), command=salvar_dados)
    botao_salvar_dados.grid(row=3, column=0, columnspan=2, padx=10, pady=10, stick="NSEW")


# Criando uma janela tkinter com o título 'cadastro de produtos'
janela = Tk()
janela.title("Cadastro de Produtos")

# Definindo a cor de fundo para a janela
janela.configure(bg="#F5F5F5")

janela.attributes("-fullscreen", True)

# Configurando a janela para utilizar a barra de menus criada
menu_barra = Menu(janela)
janela.configure(menu=menu_barra)

# Cria o menu Chamado Arquivo
menu_arquivo = Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Arquivo", menu=menu_arquivo)

# Cria uma opão no menu Arquivo chamada cadastrar
menu_arquivo.add_command(label="Cadastrar", command=cadastrar)

# Cria uma opção Sair
menu_arquivo.add_command(label="Sair", command=janela.destroy)

# Inicia a janela Tkinter
janela_principal.mainloop()