import tkinter as tk
from customtkinter import *
import customtkinter as ctk
from tkinter import ttk
from tkinter.font import BOLD
import src.utils.generic as util
 
class LoginPanel():
    
    #Metodo para verifica usuario
    def verify(self):
       pass
         
    #Metodo para Crear usuario usuario
    def create(self):
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
        
        #llamada de logo
        logo = util.read_img("./src/utils/img/logo.png", (200, 200))
        
        #contenido de la aplicacion
        
        #frame  que guarda el logo
        frame_logo = ctk.CTkFrame(self.windows)
        frame_logo.pack(side='left',expand=tk.NO, fill=tk.BOTH )
        label = ctk.CTkLabel(frame_logo, text='', image=logo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        #frame  que guarda el logo (fin)
        
        #frame  que guarda el formulario de login
        frame_form = ctk.CTkFrame(self.windows)
        frame_form.pack(side='right', expand=tk.YES, fill=tk.BOTH)
        
        #frame form title
        form_title = ctk.CTkFrame(frame_form, height=50)
        form_title.pack(side='top', fill=tk.X)
        label_title = ctk.CTkLabel(form_title, text='Inicio de Sesion', font=('Times', 30))
        label_title.pack(fill=tk.BOTH, pady=50)
        #frame form title (fin)
        
        #frame form body
        form_body = ctk.CTkFrame(frame_form)
        form_body.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)
        #frame form foot (fin)
        
        #frame form user
        user_tag = ctk.CTkLabel(form_body, text='Usuario', font=('Times', 14), anchor='w')
        user_tag.pack(fill=tk.X, padx=20, pady=5)
        self.user = ctk.CTkEntry(form_body, font=('Times', 14))
        self.user.pack(fill=tk.X, padx=20, pady=10)
        #end frame form user
        
        #frame form pass
        pass_tag = ctk.CTkLabel(form_body, text='Contraseña', font=('Times', 14), anchor='w')
        pass_tag.pack(fill=tk.X, padx=20, pady=5)
        self.passw = ctk.CTkEntry(form_body, font=('Times', 14))
        self.passw.pack(fill=tk.X, padx=20, pady=10)
        self.passw.configure(show='*')
        #end frame form pass
        
        #frame form buttom
        start = ctk.CTkButton(form_body, text='Iniciar sesion', font=('Times', 15, BOLD), command=self.verify)
        start.pack(side='left', fill=tk.X, padx=20, pady=20)
        start.bind("<Return>", (lambda event : self.verify()))
        
        '''start = ctk.CTkButton(form_body, text='Registrar usuario', font=('Times', 15, BOLD), command=self.create)
        start.pack(side='right', fill=tk.X, padx=20, pady=20)
        start.bind("<Return>", (lambda event : self.create()))'''
        #end frame form buttom
        
        self.windows.mainloop()
        