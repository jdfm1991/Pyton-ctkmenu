import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from tkinter import ttk, PhotoImage
from customtkinter import CTk, CTkFrame
from tkinter.font import BOLD
from PIL import Image, ImageTk


class SupplierPanel:
    
    def getPageHome(self):
        pass
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.supplier = ctk.CTk()
        self.supplier.title("Panel Administrativo de Proveedores")
        w, h = self.supplier.winfo_screenwidth(), self.supplier.winfo_screenheight()
        self.supplier.geometry("%dx%d+0+0" % (w-150, h-150))
        #self.windows.minsize(width=w/2, height=h/2)
        self.supplier.columnconfigure(0, weight=1)
        self.supplier.rowconfigure(0, weight=1)
        
        ctk.set_appearance_mode("System")
        
        

        
 
        self.main_frame = ctk.CTkFrame(self.supplier)
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        
        img_home = Image.open('./src/utils/img/menu/home.png')
        img_home_mod = img_home.resize((30,30),Image.ANTIALIAS)
        self.img_house = ImageTk.PhotoImage(image=img_home_mod)
        
        #Diseño visual de la primera pagina del menu de icono
        title_home = ctk.CTkLabel(self.main_frame, text='Panel de Control Inicial', font=('Times', 28, BOLD), anchor='center')
        title_home.pack(fill=tk.X, padx=20, pady=5)
        btn_home = ctk.CTkButton(self.main_frame, image=self.img_house, text='', width=40, height=40, compound=tk.TOP, command=self.getPageHome)
        btn_home.place(x=20, y=10)    
        
        self.supplier.mainloop()