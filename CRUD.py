from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

# Criando a tela básica
window = Tk()
window.title("CRUD")
window.geometry('500x400')

# Criando a conexão com o banco
bd = mysql.connector.connect (
    host= "bn4l4a4844di7ettfmil-mysql.services.clever-cloud.com",
    user= "uqsnmjvvrpxiaxoi",
    password= "6tEIZJrFhJARGGg3lo6O",
    port= "3306",
    database= "bn4l4a4844di7ettfmil"
)

# Criando o Cursor
cursor = bd.cursor(buffered=True)

# Criando o corpo da aplicação
caixa1 = Entry(window, background="white", width=10,font="Verdana")
caixa1.place(x=50, y=50)

caixa2 = Entry(window, background="white", width=10,font="Verdana")
caixa2.place(x=50, y=100)

caixa3 = Entry(window, background="white", width=10,font="Verdana")
caixa3.place(x=50, y=150)

caixa4 = Entry(window, background="white", width=10,font="Verdana")
caixa4.place(x=50, y=200)

caixa5 = Entry(window, background="white", width=10,font="Verdana")
caixa5.place(x=50, y=250)

label_1 = Label(window, text="ID", font="verdana")
label_1.place(x=50, y= 25 )

label_2 = Label(window, text="Nome", font="verdana")
label_2.place(x=50, y= 75 )

label_3 = Label(window, text="Idade", font="verdana")
label_3.place(x=50, y= 125 )

label_4 = Label(window, text="Sexo", font="verdana")
label_4.place(x=50, y= 175 )

label_5 = Label(window, text="Nacionalidade", font="verdana")
label_5.place(x=50, y= 225 )

# Função Create
def criar():
    id            = caixa1.get()
    nome          = caixa2.get()
    idade         = caixa3.get()
    sexo          = caixa4.get()
    nacionalidade = caixa5.get()

    sql = ("INSERT INTO registros (id,nome,idade,sexo,nacionalidade) VALUES (%s,%s,%s,%s,%s)")
    val = (id,nome,idade,sexo,nacionalidade)
    cursor.execute(sql,val)
    bd.commit()
    messagebox.showinfo("AVISO", "Registro Criado!")

# Função Read
def ler():
    id = caixa1.get()

    cursor.execute(f"SELECT * FROM registros WHERE id = {id}")
    dados = cursor.fetchone()

    caixa2.insert(0, dados[1])
    caixa3.insert(0, dados[2])
    caixa4.insert(0, dados[3])
    caixa5.insert(0, dados[4])
    bd.commit()

# Função update
def atualizar():
    id            = caixa1.get()
    nome          = caixa2.get()
    idade         = caixa3.get()
    sexo          = caixa4.get()
    nacionalidade = caixa5.get()

    cursor.execute (f"""
    UPDATE registros
    SET id=%s, nome=%s, idade=%s, sexo=%s, nacionalidade=%s
    WHERE id = {id} """, (id, nome, idade, sexo, nacionalidade))
    bd.commit()
    messagebox.showinfo("AVISO", "Registro Atualizado!")
    id = caixa1.get()

# Função delete
def deletar():
    id = caixa1.get()

    sql = (f"DELETE FROM registros WHERE id = {id}")
    cursor.execute(sql)
    bd.commit()
    messagebox.showinfo("AVISO", "Registro excluido!")
    
    caixa1.delete(0,END)
    caixa2.delete(0,END)
    caixa3.delete(0,END)
    caixa4.delete(0,END)
    caixa5.delete(0,END)

# Função para limpar campo
def limpar():
    caixa1.delete(0,END)
    caixa2.delete(0,END)
    caixa3.delete(0,END)
    caixa4.delete(0,END)
    caixa5.delete(0,END)

btn_criar = Button(window, text="Criar    ",command=criar)
btn_criar.place(x= 300, y= 50)

btn_ler = Button(window, text="Ler    ",command=ler)
btn_ler.place(x= 300, y= 100)

btn_atualizar = Button(window, text="Atualizar   ",command=atualizar)
btn_atualizar.place(x= 300, y= 150)

btn_deletar = Button(window, text="Deletar   ",command=deletar)
btn_deletar.place(x= 300, y= 200)

btn_limpar = Button(window, text="Limpar  ",command=limpar)
btn_limpar.place(x= 300, y= 250)

window.mainloop()