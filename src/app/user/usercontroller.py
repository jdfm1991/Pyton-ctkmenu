import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from tkinter import ttk, messagebox
from customtkinter import CTk, CTkFrame
from tkinter.font import BOLD

import src.utils.generic as util
import src.utils.encryp as en

from src.app.master.masterview import MasterPanel
from src.app.user.userview import UserPanel
from src.app.user.userpersistence import AuthUserRp
from db.tablemodelDB import AuthUser


class User(UserPanel):
    #Metodo de inicializacion (Se establece la tabla en la que se realizaran las consultas)
    def __init__(self):
        self.AuthRep = AuthUserRp()
        super().__init__()
        
    #Metodo que recoge los valores en pantalla los organiza y los guarda en la base de datos
    def register(self):
        user = AuthUser()
        user.userBD = self.user.get()
        #user.passw = self.passw.get()
        if (len(user.userBD)):
            print(len(user.userBD))
            if (self.isConfirmPassw()):
                user_db: AuthUser = self.AuthRep.getUserByName(self.user.get())
                reg = self.isUserReg(user_db)
                if (reg == True):
                    user.passw = en.encrypted(self.passw.get())
                    self.AuthRep.insertUser(user)
                    messagebox.showinfo(message="Registro Exitoso", title="Mensaje")
                    self.getRegister()
                    #self.windows.destroy()
        else:
            messagebox.showinfo(message="Los Campos no pueden dejarse vacios", title="Mensaje")
    
    #Metodo que recoge los valores de la base de datos organiza y muestra los datos en pantalla    
    def getRegister(self):
        self.emptyRegister()
        data = self.AuthRep.queryUser()
        for utd in data:
            print(utd)
            id     = utd.id
            userBD = utd.userBD
            passw  = utd.passw
            self.user_table.insert("", END, id, text=id, values=(userBD, passw))
            
    #Metodo para buscar un usuario
    def searchRegister(self):
        user_s = self.user_search.get()
        if (len(user_s)):
            print(user_s)
            self.emptyRegister()
            data = self.AuthRep.searchByName(user_s)
            for utd in data:
                print(utd)
                id     = utd.id
                userBD = utd.userBD
                passw  = utd.passw
                self.user_table.insert("", END, id, text=id, values=(userBD, passw))
        else:
            messagebox.showinfo(message="Los Campos no pueden dejarse vacios", title="Mensaje")
            
    #Metodo que elimina los datos en pantalla y en la base de datos      
    def deleteRegister(self):
        id = self.user_table.selection()[0]
        print(id)
        if int(id) > 0:
            self.AuthRep.deleteUser(id)
            self.user_table.delete(id)
            messagebox.showinfo(message='Registro borrado', title='Mensaje')
    
    #Metodo que recoge los valores de la base de datos organiza y actualiza los datos en pantalla    
    def uptateRegister(self):
        id = self.user_table.selection()[0]
        user = self.user.get()
        if (len(user)):
            if (self.isConfirmPassw()):
                passw = en.encrypted(self.passw.get())
                print(id, user, passw)
                if int(id) > 0:
                    self.AuthRep.uptadeUser(id,user,passw)            
                    messagebox.showinfo(message='Registro Actualizado Exitosamente', title='Mensaje')
                    self.cleanfields2()
                    self.getRegister()
    
    #Metodo que recoge los valores en pantalla que son seleccionados con el mouse   
    def dataCapture(self, event):
        self.update = True
        self.statustable()
        #Obtencion de valores selecionados en la tabla
        id = self.user_table.selection()[0]
        select = self.user_table.set(id)
        print(select)
        #limpieza de campos para cargar valores nuevos
        self.cleanfields()    
        
        #Cargar valores nuevos
        self.user.insert(0, select['Usuario'])
        self.passw.insert(0, select['Contraseña'])
        self.confirm.insert(0, select['Contraseña'])
    
    #Metodo usado para limpiar el formulario antes de cargar el nuevo valor seleccionado con el mouse
    def cleanfields(self):
        #limpieza de campos para cargar valores nuevos
        self.user.delete(0, END)
        self.passw.delete(0, END)
        self.confirm.delete(0, END)
        
    #Metodo usado para limpiar el formulario al precionar el boton de limpiar Formulario
    def cleanfields2(self):
        self.update = False
        self.statustable()
        #limpieza de campos para cargar valores nuevos
        self.user.delete(0, END)
        self.passw.delete(0, END)
        self.confirm.delete(0, END)
        
    #Metodo usado para cambiar el estatus de la opeacion a realizar para habilitar y deshabilitar los botones del menu
    def statustable(self):
        if (self.update == False):
            self.user_table.config(selectmode=None)
            self.btn_save_user.configure(state=NORMAL)
            self.btn_uptade_user.configure(state=DISABLED)
            self.btn_delete_user.configure(state=DISABLED)
        else:
            self.user_table.config(selectmode=BROWSE)
            self.btn_save_user.configure(state=DISABLED)
            self.btn_delete_user.configure(state=NORMAL)
            self.btn_uptade_user.configure(state=NORMAL)
            
    #Metodo usado para vaciar la tabla y volverla a llenar en cada consulta     
    def emptyRegister(self):
        file = self.user_table.get_children()
        for files in file:
            self.user_table.delete(files)
            
    #Metodo usado para validar si el usuario que se quiere registrar ya existe en la base de datos        
    def isConfirmPassw(self):
        status : bool = True
        if (self.passw.get() != self.confirm.get()):
            status = False
            messagebox.showerror(message="las contraseñas no coinciden", title="mensaje")
            self.passw.delete(0, tk.END)
            self.confirm.delete(0,tk.END)
        return status
    
    #Metodo usado para validar si el usuario que se quiere registrar ya existe en la base de datos      
    def isUserReg(self, user: AuthUser):
        status : bool = True
        if (user != None):
            status = False
            messagebox.showerror(message="Usuario ya existe", title="mensaje")
        return status
    
