#!/usr/bin/env python
# coding: utf-8

# In[10]:


from tkinter import *
from hashlib import blake2b
from tkinter.filedialog import askopenfilename

sen = ''

def senha():
    tipo = str(c.get())
    tipo = bytes(tipo.encode())
    file = arquivo[0]
    file = bytes(file.encode())
    senha = blake2b(digest_size=30,key=tipo)
    senha.update(file)
    return senha.hexdigest()

def gera():
    global sen
    entry_1 = Label(root,text = 'Password Generated successfully')
    entry_1.place(x=170,y=230)
    
    entry_2 = Text(root,bg = 'white',bd = 3,height = 1, width =50)
    entry_2.insert(INSERT,str(senha()))
    entry_2.place(x=50,y=260)
    sen = entry_2.get("1.0",END)
    
def copia() :
    global sen
    root .clipboard_clear()  
    root.clipboard_append(sen)
    
root = Tk()
root.geometry('500x400')
root.title("PassGen_v1")

label_0 = Label(root, text="Password Generator",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Selected File:",width=20,font=(10))
label_1.place(x=80,y=130)

arquivo = askopenfilename()
arquivo = arquivo.split(sep='/')
arquivo = arquivo[len(arquivo) - 1]
arquivo = arquivo.split(sep='.')

label_2 = Label(root, text=arquivo[0],width=20,font=("bold", 8))
label_2.place(x=250,y=130)

label_3 = Label(root, text="Type",width=20,font=(10))
label_3.place(x=45,y=180)
list1 = ['File_type1','File_type2','File_type3','File_type4'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=20)
c.set('File_type1') 
droplist.place(x=240,y=180)


Button(root, text='Generate Password',width=20,bg='brown',fg='white', command = gera).place(x=180,y=300)
Button(root, text='Copy Password',width=20,bg='brown',fg='white', command = copia).place(x=180,y=340)
 

root.mainloop()

