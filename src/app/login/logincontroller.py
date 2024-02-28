import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from tkinter import ttk, messagebox
from customtkinter import CTk, CTkFrame
from tkinter.font import BOLD

import src.utils.generic as util
import src.utils.encryp as en

from src.app.master.mastercontroller import Master
from src.app.login.registercontroller import Register
from src.app.login.loginview import LoginPanel
from src.app.user.userpersistence import AuthUserRp
from db.tablemodelDB import AuthUser

class Login(LoginPanel):
    #Metodo de inicializacion (Se establece la tabla en la que se realizaran las consultas)
    def __init__(self):
        self.AuthRep = AuthUserRp()
        super().__init__()
        
    #Metodo para verifica usuario
    def verify(self):
        user_db: AuthUser = self.AuthRep.getUserByName(self.user.get())
        if (self.isUSer(user_db)):
              self.isPass(self.passw.get(),user_db)
              
    #Metodo para Crear usuario usuario
    def create(self):
        Register().mainloop()
            
    #Metodo de verificacion de usuario
    def isUSer(self, user:AuthUser):
        status : bool = True
        if (user == None):
            status = False
            messagebox.showerror(message="usuario no registrado", title="Mensaje")
        return status
    
    #Metodo de verificacion de clave
    def isPass(self, passw:str, user:AuthUser):
        b_passw = en.decrypt(user.passw)
        if (passw == b_passw):
            self.windows.destroy()
            Master()
        else:
           messagebox.showerror(message="Clave Errada", title="Mensaje") 
           