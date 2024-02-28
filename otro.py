import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from tkinter import ttk
from customtkinter import CTk, CTkFrame
from tkinter.font import BOLD

from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk

from src.utils.archive import ArchiveVariable

class SupplierPanel():
    
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
        ctk.set_default_color_theme('green')
        
        img_arch = Image.open('./src/utils/img/menu/archive.png')
        img_arch_mod = img_arch.resize((250,250),Image.ANTIALIAS)
        self.img_archive = ImageTk.PhotoImage(image=img_arch_mod)
        
        #self.supplier.protocol("WM_DELETE_WINDOW", lambda: None)
        
        btn_archive = ctk.CTkButton(self.supplier, image=self.img_archive, text='Archivos', font=("Times", 30, BOLD),  anchor='center', compound=tk.TOP)
        btn_archive.place(x=30, relx=0.0, rely=0.1, relwidth=0.3, relheight=0.4)
        
        self.supplier.mainloop()
        
        
SupplierPanel()