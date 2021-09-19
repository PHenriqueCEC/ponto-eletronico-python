from tkinter import *
from firebase import firebase

firebase = firebase.FirebaseApplication('https://ponto-eletronico-9a5bb.firebaseio.com/', None)

menu_inicial = Tk() #criamos um objeto associado ao tkinter, root é a tela principal

Nome = StringVar()
Email = StringVar()
Matricula = StringVar()
Categoria = StringVar()
Cargo = StringVar()

#Passando as medidas e configurações da tela
#menu_inicial.geometry("600x400")
menu_inicial.title("Gerenciador de membros Rinobot Team")
menu_inicial.configure(background='red')

def coloca_erro(data):
    data['Nome'] = "xxxxxxx"
    data['Email'] = "xxxxxxx"
    data['Categoria'] = "xxxxxxx"
    data['Cargo'] = "xxxxxxx"
    return data

def atualizarDados():
    result = firebase.get('/ponto-eletronico-9a5bb/Cadastro', '')
    for pessoa in result:
        dados = result[pessoa]
        if dados['Matricula'] == Matricula.get():
            cod_att = pessoa
            break
    data = {
        'Nome': Nome.get(),
        'Email': Email.get(),
        'Matricula': Matricula.get(),
        'Categoria': Categoria.get(),
        'Cargo': Cargo.get()
    }
    for dado in data:
        print(dado)
        print(data[dado])
        firebase.put('/ponto-eletronico-9a5bb/Cadastro/' + cod_att, dado, data[dado])

def buscarMembro():
    result = firebase.get('/ponto-eletronico-9a5bb/Cadastro', '')
    for membro in result:
        data = result[membro]
        if data['Matricula'] == Matricula.get():
             Nome.set(data['Nome'])
             Email.set(data['Email'])
             Categoria.set(data['Categoria'])
             Cargo.set(data['Cargo'])
             print(data)
        elif data['Matricula'] != Matricula.get():
            coloca_erro(data)
            Nome.set(data['Nome'])
            Email.set(data['Email'])
            Categoria.set(data['Categoria'])
            Cargo.set(data['Cargo'])
            print("Membro não encontrado!")
            break

def cadastrarMembro():
    data = {
        'Nome': Nome.get(),
        'Email': Email.get(),
        'Matricula': Matricula.get(),
        'Categoria': Categoria.get(),
        'Cargo': Cargo.get()
    }
    # Criar uma função para verificar se o membro já está cadastrado
    result = firebase.post('/ponto-eletronico-9a5bb/Cadastro', data)
    print(result)

#label1 = Label(menu_inicial, text="Gerenciador de membros Rinobot team", bg="red", fg="white", font="arial 18 bold", width=40)
#label1.grid(row=0, column=1)
# print(label1.keys()) util para vermos oq podemos usar na label1


labelNome = Label(menu_inicial, text="Nome: ", bg="red", fg="white", font="arial 18 bold").grid(row=0, column=0, stick=E)
textNome = Entry(menu_inicial, textvariable=Nome, width=40).grid(row=0, column=1)

labelEmail = Label(menu_inicial, text="Email: ", bg="red", fg="white", font="arial 18 bold").grid(row=1, column=0, stick=E)
textEmail = Entry(menu_inicial, textvariable=Email, width=40).grid(row=1, column=1, padx=8, stick=E)

labelMatricula = Label(menu_inicial, text="Matricula: ", bg="red", fg="white", font="arial 18 bold").grid(row=2, column=0, stick=E)
textMatricula = Entry(menu_inicial, textvariable=Matricula, width=20).grid(row=2, padx=80, columnspan=2)

labelCategoria = Label(menu_inicial, text="Categoria: ", bg="red", fg="white", font="arial 18 bold").grid(row=3, column=0, stick=E)
textCategoria = Entry(menu_inicial, textvariable=Categoria, width=20).grid(row=3, columnspan=2)

labelCargo = Label(menu_inicial, text="Cargo: ", bg="red", fg="white", font="arial 18 bold").grid(row=4, column=0, stick=E)
textCargo = Entry(menu_inicial, textvariable=Cargo, width=20).grid(row=4, columnspan=2)





'''
labelNome = Label(menu_inicial, text="Nome: ", bg="red", fg="white", font="arial 18 bold").grid(row=0, column=0)
textNome = Entry(menu_inicial, width=50).grid(row=0, column=1)
'''

#botao
cmdBuscar = Button(menu_inicial, text="Buscar membro", command=buscarMembro)
cmdBuscar.grid(row=0, column=2, padx=5, sticky=W)

cmdCadastrar = Button(menu_inicial, text="Cadastrar novo membro", command=cadastrarMembro)
cmdCadastrar.grid(row=5, columnspan=1,padx=5)

cmdRemover = Button(menu_inicial, text="Remover membro", command=coloca_erro)
cmdRemover.grid(row=5, column=1, padx=0)

cmdAtualizar = Button(menu_inicial, text="Atualizar dados", command=atualizarDados)
cmdAtualizar.grid(row=5, column=2)

"""
cmdListarMembros= Button(menu_inicial, text="Listar Membros", command=cmd_Click)
cmdListarMembros.grid(row=6, columnspan=1)
"""

# Dimensões da janela
largura = 600
altura = 400

# Resolucao do sistema
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()

# Posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/1.9

# Definir a geometry
#menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))




'''
#criando o frame do topo
Top = Frame(root, width=1350, height=60)
Top.pack(side=TOP)

Left = Frame(root, width=900, height=635)
Left.pack(side=LEFT)

Right = Frame(root, width=445, height=635)
Right.pack(side=RIGHT)
Right.configure(background='white')

lblTitulo = Label(Top, font=('arial', 35, 'bold'), text="Gerenciamento de membros Rinobot", width=50)
lblTitulo.grid(row=0, column=0)

#Frames secundários
RightP1t = Frame(Right, width=445, height=535)
RightP1t.pack(side=TOP)
RightP1t.configure(background='red')

RightP1b = Frame(Right, width=445, height=100)
RightP1b.pack(side=BOTTOM)
RightP1b.configure(background='black')
'''


menu_inicial.mainloop()



