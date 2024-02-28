import tkinter as tk
from customtkinter import *
import customtkinter as ctk
from tkinter import ttk
from tkinter.font import BOLD
import src.utils.generic as util
 
class RegisterPanel():
    
    #Metodo para Registar usuario
    def register(self):
       pass
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.windows = ctk.CTk()
        self.windows.title("Inicio de Sesion")
        self.windows.geometry('600x450')
        self.windows.config(bg='#fcfcfc')
        self.windows.resizable(width=0, height=0)
        util.center_windows(self.windows,600,450)
        
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme('dark-blue')
        
        self.windows.mainloop()