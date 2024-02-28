import tkinter as tk
from customtkinter import *
import customtkinter as ctk
from tkinter import ttk
import src.utils.generic as util
 
class UserPanel():
    
    def register(self):
        pass
    
    def getRegister(self):
        pass
    
    def searchRegister(self):
        pass
    
    def deleteRegister(self):
        pass
    
    def uptateRegister(self):
        pass
     
    def dataCapture(self, event):
        pass
    def cleanfields(self):
        pass
    
    def cleanfields2(self):
        pass
     
    def statustable(self):
        pass
     
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.windows = ctk.CTk()
        self.windows.title("Master Panel")
        w, h = self.windows.winfo_screenwidth(), self.windows.winfo_screenheight()
        self.windows.geometry("%dx%d+0+0" % (w-150, h-150))
        #self.windows.minsize(width=w/2, height=h/2)
        self.windows.columnconfigure(0, weight=1)
        self.windows.rowconfigure(0, weight=1)
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme('green')
        
        self.update = False
 
        self.main_frame = ctk.CTkFrame(self.windows)
        self.main_frame.pack(expand=True, fill=tk.BOTH)
        
        #self.img_setting = tk.PhotoImage(file ='./img/menu/setting_white.png')
        
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.pack(side='left', expand=True, fill=tk.BOTH, padx=5, pady=5)
        #frame form user
        user_tag = ctk.CTkLabel(form_frame, text='Usuario', font=('Times', 14), anchor='w')
        user_tag.pack(fill=tk.X, padx=20, pady=5)
        self.user = ctk.CTkEntry(form_frame, font=('Times', 14))
        #self.user = ttk.Entry(form_frame, font=('Times', 14))
        self.user.pack(fill=tk.X, padx=20, pady=10)
        #end frame form user
        
        #frame form pass
        pass_tag = ctk.CTkLabel(form_frame, text='Contraseña', font=('Times', 14), anchor='w')
        pass_tag.pack(fill=tk.X, padx=20, pady=5)
        self.passw = ctk.CTkEntry(form_frame, font=('Times', 14))
        self.passw.pack(fill=tk.X, padx=20, pady=10)
        self.passw.configure(show='*')
        
        confirm_tag = ctk.CTkLabel(form_frame, text='Contraseña', font=('Times', 14), anchor='w')
        confirm_tag.pack(fill=tk.X, padx=20, pady=5)
        self.confirm = ctk.CTkEntry(form_frame, font=('Times', 14))
        self.confirm.pack(fill=tk.X, padx=20, pady=10)
        self.passw.configure(show='*')
        
        opt_menu = ctk.CTkButton(form_frame, text='limpiar formulario', command=self.cleanfields2)
        opt_menu.pack(padx=20, pady=10)
        opt_menu.bind("<Return>", (lambda event : self.cleanfields2()))
        
        #end frame form pass
        
        
        
        self.bottom_frame = ctk.CTkFrame(self.main_frame)
        self.bottom_frame.pack(side='left', expand=True, fill=tk.BOTH, padx=5, pady=5)
        
        self.btn_save_user = ctk.CTkButton(self.bottom_frame, text="Nueva Informacion", command=self.register)
        self.btn_save_user.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.btn_save_user.bind("<Return>", (lambda event : self.register()))
        
        self.btn_delete_user = ctk.CTkButton(self.bottom_frame, text="Eliminar informacion", command=self.deleteRegister)
        self.btn_delete_user.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.btn_delete_user.bind("<Return>", (lambda event : self.deleteRegister()))
        
        self.btn_uptade_user = ctk.CTkButton(self.bottom_frame, text="Modificar informacion", command=self.uptateRegister)
        self.btn_uptade_user.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.btn_uptade_user.bind("<Return>", (lambda event : self.uptateRegister()))
        
        
       
        self.user_search = ctk.CTkEntry(self.bottom_frame, font=('Times', 14))
        self.user_search.pack(padx=20, pady=10)
        
        self.btn_search_user = ctk.CTkButton(self.bottom_frame, text='Bucar Usuario', command=self.searchRegister)
        self.btn_search_user.pack(padx=20, pady=10)
        self.btn_search_user.bind("<Return>", (lambda event : self.searchRegister()))
        
        self.btn_reset = ctk.CTkButton(self.bottom_frame, text='Refrecar', command=self.getRegister)
        self.btn_reset.pack(padx=20, pady=10)
        self.btn_reset.bind("<Return>", (lambda event : self.getRegister()))
        
       
        
        
        self.frame_user_table = ctk.CTkFrame(self.windows)
        self.frame_user_table.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.user_table = ttk.Treeview(self.frame_user_table, selectmode=None)
        self.user_table.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        self.utsx = ttk.Scrollbar(self.user_table, orient='horizontal',command=self.user_table.xview)
        self.utsx.pack(side='bottom',fill=tk.X)
        #self.utsx.grid(column=0, row = 1, sticky='ew') 
        
        self.utsy = ttk.Scrollbar(self.user_table, orient='vertical',command=self.user_table.yview)
        self.utsy.pack(side='right', fill=tk.Y)
        #self.utsy.grid(column = 1, row = 0, sticky='ns')
        
        self.user_table.configure(xscrollcommand=self.utsx.set, yscrollcommand = self.utsy.set)
        self.user_table['columns'] = ('Usuario', 'Contraseña')
        
        self.user_table.column('#0', minwidth=10,anchor='center', stretch=NO)
        self.user_table.column('Usuario',  anchor='center', stretch=NO)
        self.user_table.column('Contraseña',  anchor='center', stretch=NO)
        
        self.user_table.heading('#0', text='Codigo', anchor ='center')
        self.user_table.heading('Usuario', text='Usuario', anchor ='center')
        self.user_table.heading('Contraseña', text='Contraseña', anchor ='center')
        
        self.user_table.bind('<<TreeviewSelect>>', self.dataCapture)

        
        
        #self.statustable()
        self.getRegister()
        self.statustable()
        self.windows.mainloop()
