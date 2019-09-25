#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.geometry('500x400')
root.title("Ferramenta")

lista = ''
top = ''
base = 'cadastro.db'

def add () :
    if entry_1.get() is '' or entry_2.get() is '' or entry_3.get() is '' :
        
        messagebox.showinfo("Alerta", "Preencha todos os campos!!!")
        return
    
    con = sqlite3.connect(base)
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ENTREGAS(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Empregado TEXT, '              'Nome_entrega TEXT, Data_entrega TEXT)')
    texto_add = "INSERT INTO ENTREGAS (Empregado, Nome_entrega, Data_entrega) values (?,?,?)"
    cur.execute(texto_add,(entry_1.get(),entry_2.get(),entry_3.get()))
    con.commit()
    messagebox.showinfo("Info", "Registro Salvo com Sucesso")
    entry_1.delete(0,100)
    entry_2.delete(0,100)
    entry_3.delete(0,100)
    cur.close()
    con.close()

def busca () :
    global lista
    global top
    con = sqlite3.connect(base)
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ENTREGAS(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Empregado TEXT, '              'Nome_entrega TEXT, Data_entrega TEXT)')
    top = Toplevel()
    top.title('Busca Registros')
    top.geometry('370x350')
    Label(top,anchor = 'w' ,text = 'Empregado / Entrega / Data',width=30,font=(10)).place(x=15,y=10)
    Button(top, text='Apagar Registro',width=20,bg='brown',fg='white', command = apaga).place(x=110,y=300)
    lista = Listbox(top,font = ("Arial","15"), width = 30 )
    nome = entry_1.get()
    
    if nome is not "":
        cur.execute("SELECT * FROM ENTREGAS WHERE Empregado is '%s'" %(nome))
    else :
        cur.execute("SELECT * FROM ENTREGAS")
    
    for linha in cur.fetchall() :
        
        lista.insert(1,linha[1:])
    
    lista.place(x=15,y=35)
    
    cur.close()
    con.close()

def apaga() :
    global top
    con = sqlite3.connect(base)
    cur = con.cursor()
    try :
        select = str(lista.get(lista.curselection()))
    except :
        messagebox.showinfo("Alerta", "Selecione um registro!")
        top.withdraw()
        top.deiconify()
        return
    
    select = select.split()
    select = select[1]
    
    cur.execute("DELETE FROM Entregas WHERE Nome_entrega is '%s'" %(select[1:-2]))
    con.commit()
    top.withdraw()
    messagebox.showinfo("Info", "Registro Apagado com Sucesso")
    cur.close()
    con.close()
    busca()
    
Label(root,text = 'Cadastro de Entrega',width=20,font=20).place(x=150,y=30)
    
Label(root, anchor = 'w',text = 'Nome Empregado',width=20,font=(10)).place(x=15,y=80)
entry_1 = Entry(root,width=20,font=(10))
entry_1.place(x=200,y=80)

Label(root,anchor = 'w' ,text = 'Entrega',width=20,font=(10)).place(x=15,y=110)
entry_2 = Entry(root,width=20,font=(10))
entry_2.place(x=200,y=110)

Label(root,anchor = 'w' ,text = 'Data da Entrega',width=20,font=(10)).place(x=15,y=140)
entry_3 = Entry(root,width=20,font=(10))
entry_3.place(x=200,y=140)


Button(root, text='Salvar Registro',width=20,bg='brown',fg='white', command = add).place(x=250,y=300)
Button(root, text='Buscar Registro',width=20,bg='brown',fg='white', command = busca).place(x=70,y=300)



root.mainloop()


# In[6]:


import pandas as pd
con = sqlite3.connect(base)
db = pd.read_sql_query("SELECT * FROM ENTREGAS",con)
db = db.drop(columns='id')
db

