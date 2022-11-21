import tkinter as tk
from tkinter import ttk
import pickle
from Cliente import Cliente

listaClientes = []

def altaCliente():
    repetido = False
    for i in listaClientes:
        if i.getCod() == txCodigo.get():
            repetido = True

    if repetido == False:
        listaClientes.append(Cliente(txCodigo.get(), txNombre.get(), txDni.get()))
        escribirLista()
        rellenarTabla()


def listarClientes():
    for i in listaClientes:
        print(i.getCod())

def bajaClientes():
    for i in listaClientes:
        if i.getCod() == txCodigo.get():
            listaClientes.remove(i)
            escribirLista()
            rellenarTabla()

def modificarCliente():
    for i in listaClientes:
        if i.getCod() == txCodigo.get():
            bajaClientes()
            altaCliente()

    
def escribirLista():
    fichero_binario = open("clientes", "wb")
    pickle.dump(listaClientes, fichero_binario)
    fichero_binario.close()


def rellenarTabla():
    tree.delete(*tree.get_children())
    for i in listaClientes:
        tree.insert("", 0, values=(i.getCod(), i.getNombre(), i.getDni()))





root = tk.Tk()
root.title("Administracion de clientes")
root.config(width= 600, height= 400)

lbNombre = ttk.Label(text="Nombre:")
lbNombre.place(x = 20, y = 20)
txNombre = ttk.Entry()
txNombre.place(x = 100, y = 20)

lbCodigo = ttk.Label(text="Codigo:")
lbCodigo.place(x = 20, y = 60)
txCodigo = ttk.Entry()
txCodigo.place(x = 100, y = 60)

lbDni = ttk.Label(text="Dni:")
lbDni.place(x = 20, y = 100)
txDni = ttk.Entry()
txDni.place(x = 100, y = 100)


btAlta = ttk.Button(text= "Alta", command= altaCliente)
btAlta.place(x= 300, y = 100)
btListar = ttk.Button(text= "Baja", command= bajaClientes)
btListar.place(x=400, y=100)
btModificar = ttk.Button(text= "Modificar", command= modificarCliente)
btModificar.place(x=500, y=100)
#btListar = ttk.Button(text= "Listar", command= listarClientes)
#btListar.place(x=500, y=100)

tree = ttk.Treeview(root, height=10, columns=("Codigo", "nombre", "Dni"))
tree.column("#0", width="0", minwidth=0)
tree.column("Codigo", width= 150, anchor= "center")
tree.column("nombre", width= 150, anchor="center")
tree.column("Dni", width= 150, anchor="center")
tree.heading("Codigo", text="Código")
tree.heading("nombre", text="Nombre")
tree.heading("Dni", text= "Dni")
tree.place(x=20, y= 150)

#cargarLista()
try:
    fichero_binario = open("clientes", "rb")
    listaClientes = pickle.load(fichero_binario)
    fichero_binario.close
    rellenarTabla()
except FileNotFoundError:
    print("archivo no encontrdo, se creará uno al dar de alta algun cliente")

root.mainloop()


