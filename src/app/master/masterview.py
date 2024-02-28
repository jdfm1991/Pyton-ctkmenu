import customtkinter as ctk
import tkinter as tk
import tkinterweb as tw
import webbrowser as web
from customtkinter import *
from tkinter import ttk, PhotoImage
from customtkinter import CTk, CTkFrame
from PIL import Image, ImageTk
from tkinterweb import HtmlFrame
from tkinter.font import BOLD
import src.utils.generic as util

 
class MasterPanel:
    
    def statePrimaryPage(self):
        pass
    
    def getPageHome(self):
        pass
    
    def getPageArchive(self):
        pass
    
    def getPageTransaction(self):
        pass
    
    def getPageReport(self):
        pass
    
    def getPageSetting(self):
        pass
    
    def getPagePlus(self):
        pass
    
    def getSupplier(self):
        pass
    
    '''def getlink(self):
        web.open_new('http://contribuyente.seniat.gob.ve/BuscaRif/BuscaRif.jsp')
        
    def getlink2(self):
        self.winlink = ctk.CTkToplevel()
        frame_link = tw.HtmlFrame(self.winlink )
        frame_link.load_url('http://contribuyente.seniat.gob.ve/BuscaRif/BuscaRif.jsp')
        frame_link.pack(fill="both", expand=True)
        self.winlink.mainloop()'''
        
    def __init__(self):
        #super().__init__()
        self.windows = ctk.CTk()
        self.windows.title("Master Panel")
        w, h = self.windows.winfo_screenwidth(), self.windows.winfo_screenheight()
        self.windows.geometry("%dx%d+0+0" % (w-150, h-150))
        self.windows.minsize(width=w-500, height=h-200)
        self.windows.columnconfigure(0, weight=1)
        self.windows.rowconfigure(0, weight=1)
        
        ctk.set_appearance_mode("dark")
        
        self.statewindowsprimary = True
        
 
        self.main_frame = ctk.CTkFrame(self.windows,)
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        
        #Carga de imagenes sistemas
        #Opciones del menu maestro
        img_home = Image.open('./src/utils/img/menu/home.png')
        img_home_mod = img_home.resize((30,30),Image.ANTIALIAS)
        self.img_house = ImageTk.PhotoImage(image=img_home_mod)
        
        img_arch = Image.open('./src/utils/img/menu/archive.png')
        img_arch_mod = img_arch.resize((250,250),Image.ANTIALIAS)
        self.img_archive = ImageTk.PhotoImage(image=img_arch_mod)
        
        img_trans = Image.open('./src/utils/img/menu/transaction.png')
        img_trans_mod = img_trans.resize((250,250),Image.ANTIALIAS)
        self.img_transaction = ImageTk.PhotoImage(image=img_trans_mod)
        
        img_rep = Image.open('./src/utils/img/menu/report.png')
        img_rep_mod = img_rep.resize((250,250),Image.ANTIALIAS)
        self.img_report = ImageTk.PhotoImage(image=img_rep_mod)
        
        img_set = Image.open('./src/utils/img/menu/setting.png')
        img_set_mod = img_set.resize((250,250),Image.ANTIALIAS)
        self.img_setting = ImageTk.PhotoImage(image=img_set_mod)
        
        img_var = Image.open('./src/utils/img/menu/varius.png')
        img_var_mod = img_var.resize((250,250),Image.ANTIALIAS)
        self.img_varius = ImageTk.PhotoImage(image=img_var_mod)
        
        #Opciones del menu Archivo
        img_sup = Image.open('./src/utils/img/menu/supplier.png')
        img_sup_mod = img_sup.resize((250,250),Image.ANTIALIAS)
        self.supplier = ImageTk.PhotoImage(image=img_sup_mod)
        
        img_custom = Image.open('./src/utils/img/menu/customer.png')
        img_custom_mod = img_custom.resize((250,250),Image.ANTIALIAS)
        self.customer = ImageTk.PhotoImage(image=img_custom_mod)
        
        img_sel = Image.open('./src/utils/img/menu/seller.png')
        img_sel_mod = img_sel.resize((250,250),Image.ANTIALIAS)
        self.seller = ImageTk.PhotoImage(image=img_sel_mod)
        
        img_invent = Image.open('./src/utils/img/menu/inventory.png')
        img_invent_mod = img_invent.resize((250,250),Image.ANTIALIAS)
        self.inventory = ImageTk.PhotoImage(image=img_invent_mod)
        
        img_service = Image.open('./src/utils/img/menu/services.png')
        img_service_mod = img_service.resize((250,250),Image.ANTIALIAS)
        self.services = ImageTk.PhotoImage(image=img_service_mod)
        
      
        
        #Diseño visual de la primera pagina del menu de icono
        title_home = ctk.CTkLabel(self.main_frame, text='Panel de Control Inicial', font=('Times', 28, BOLD), anchor='center')
        title_home.pack(fill=tk.X, padx=20, pady=5)
        btn_home = ctk.CTkButton(self.main_frame, image=self.img_house, text='', width=40, height=40, compound=tk.TOP, command=self.getPageHome)
        btn_home.place(x=20, y=10)        
        
        #Deficion del estilo visual se la vista de las paginas del menu de icono (contenedor de botones)
        style = ttk.Style()
        style.configure("TNotebook", background='#2b2b2b', padding=0, foreground='#2b2b2b', borderwidth=0)
        style.theme_use("default")
        style.configure("TNotebook", background='#2b2b2b', borderwidth=0)
        style.configure("TNotebook.Tab", background="#2b2b2b", borderwidth=0)
        style.map("TNotebook", background=[("selected", '#2b2b2b')])
        style.map("TNotebook.Tab", background=[("selected", '#2b2b2b')],  foreground=[("selected", '#2b2b2b')])
        
        #Deficion del menu de icono (contenedor de botones)
        self.main_page = ttk.Notebook(self.main_frame, style='TNotebook')
        self.main_page.pack(expand=True, fill=tk.BOTH, padx=20, pady=20, anchor='center')
        
        #Deficion de paginas del menu de icono (contenedor de botones)
        self.home_frame = ctk.CTkFrame(self.main_page)
        self.archive_frame = ctk.CTkFrame(self.main_page)
        self.transaction_frame = ctk.CTkFrame(self.main_page)
        self.report_frame = ctk.CTkFrame(self.main_page)
        self.setting_frame = ctk.CTkFrame(self.main_page)
        self.various_frame = ctk.CTkFrame(self.main_page)
        
        #Incorporacion de las paginas al menu de icono (contenedor de botones)
        self.main_page.add(self.home_frame)
        self.main_page.add(self.archive_frame)
        self.main_page.add(self.transaction_frame)
        self.main_page.add(self.report_frame)
        self.main_page.add(self.setting_frame)
        self.main_page.add(self.various_frame) 
        
        #Creacion de pagina home y Ubicacion de los botones del panel maestro de las opciones del menu situadas en la pagina HOME (INICIO)
        btn_archive = ctk.CTkButton(self.home_frame, image=self.img_archive, text='Archivos', font=("Times", 30, BOLD),  anchor='center', compound=tk.TOP, command=self.getPageArchive)
        btn_archive.place(x=30, relx=0.0, rely=0.1, relwidth=0.3, relheight=0.4)
        #btn_archive.bind("<Return>", (lambda event : self.getArchivePanel()))
        
        btn_transaction= ctk.CTkButton(self.home_frame, image=self.img_transaction, text='Trasacciones', font=("Times", 30, BOLD), anchor='center', compound=tk.TOP, command=self.getPageTransaction)
        btn_transaction.place(x=50, relx=0.3, rely=0.1, relwidth=0.3, relheight=0.4)
        
        btn_report = ctk.CTkButton(self.home_frame, image=self.img_report, text='Reportes', font=("Times", 30, BOLD), anchor='center', compound=tk.TOP, command=self.getPageReport)
        btn_report.place(x=70, relx=0.6, rely=0.1, relwidth=0.3, relheight=0.4)
        
        btn_setting = ctk.CTkButton(self.home_frame, image=self.img_setting, text='Ajustes', font=("Times", 30, BOLD), anchor='center', compound=tk.TOP, command=self.getPageSetting)
        btn_setting.place(x=30, y=20, relx=0.0, rely=0.5, relwidth=0.3, relheight=0.4)
        #btn_setting.bind("<Return>", (lambda event : self.getUserSetting()))
        
        btn_various = ctk.CTkButton(self.home_frame, image=self.img_varius, text='Varios', font=("Times", 30, BOLD), anchor='center', compound=tk.TOP, command=self.getPagePlus)
        btn_various.place(x=50, y=20, relx=0.3, rely=0.5, relwidth=0.3, relheight=0.4)
        #Creacion de pagina home y Ubicacion de los botones del panel maestro de las opciones del menu situadas en la pagina HOME (FIN)
        
        
        #Creacion de pagina archive (INICIO)
        title_archive = ctk.CTkLabel(self.archive_frame, text='Panel de Control de Archivos', font=('Times', 28), anchor='center')
        title_archive.pack(fill=tk.X, padx=20, pady=5)
        
        #Creacion de pagina archive y Ubicacion de los botones del panel maestro de las opciones del menu situadas en la pagina archive (INICIO)
        btn_supplier = ctk.CTkButton(self.archive_frame, image=self.supplier, text='Proveedor', font=("Times", 30, BOLD),  anchor='center', compound=tk.TOP, command=self.getSupplier)
        btn_supplier.place(x=30, relx=0.0, rely=0.1, relwidth=0.3, relheight=0.4)
        
        btn_customer= ctk.CTkButton(self.archive_frame, image=self.customer, text='Cliente', font=("Times", 30, BOLD), anchor='center', compound=tk.TOP)
        btn_customer.place(x=50, relx=0.3, rely=0.1, relwidth=0.3, relheight=0.4)
        
        btn_seller = ctk.CTkButton(self.archive_frame, image=self.seller, text='Vendedor', font=("Times", 30, BOLD), anchor='center', compound=tk.TOP)
        btn_seller.place(x=70, relx=0.6, rely=0.1, relwidth=0.3, relheight=0.4)
        
        btn_inventory = ctk.CTkButton(self.archive_frame, image=self.inventory, text='Inventario', font=("Times", 30, BOLD), anchor='center', compound=tk.TOP)
        btn_inventory.place(x=30, y=20, relx=0.0, rely=0.5, relwidth=0.3, relheight=0.4)
        #btn_setting.bind("<Return>", (lambda event : self.getUserSetting()))
        
        btn_services = ctk.CTkButton(self.archive_frame, image=self.services, text='Servicios', font=("Times", 30, BOLD), anchor='center', compound=tk.TOP)
        btn_services.place(x=50, y=20, relx=0.3, rely=0.5, relwidth=0.3, relheight=0.4)
        #Creacion de pagina archive y Ubicacion de los botones del panel maestro de las opciones del menu situadas en la pagina archive (FIN)
        
        #Creacion de pagina archive (FIN)
        
        
        #Creacion de pagina transaction (INICIO)
        title_transaction = ctk.CTkLabel(self.transaction_frame, text='Panel de Control de Transacciones', font=('Times', 28), anchor='center')
        title_transaction.pack(fill=tk.X, padx=20, pady=5)
        
        #Creacion de pagina transaction (FIN)
        
        
        #Creacion de pagina report (INICIO)
        title_report = ctk.CTkLabel(self.report_frame, text='Panel de Control de Reportes', font=('Times', 28), anchor='center')
        title_report.pack(fill=tk.X, padx=20, pady=5)
        
        #Creacion de pagina report (FIN)
        
        
        #Creacion de pagina setting (INICIO)
        title_setting = ctk.CTkLabel(self.setting_frame, text='Panel de Control de Configuracion', font=('Times', 28), anchor='center')
        title_setting.pack(fill=tk.X, padx=20, pady=5)
        
        #Creacion de pagina setting (FIN)
        
        
        #Creacion de pagina various (INICIO)
        title_various = ctk.CTkLabel(self.various_frame, text='Panel de Control General', font=('Times', 28), anchor='center')
        title_various.pack(fill=tk.X, padx=20, pady=5)
        
        #Creacion de pagina various (FIN)
        

        
        
        '''opt_menu = ctk.CTkButton(self.windows, text='link', command=self.getlink)
        opt_menu.pack(fill=tk.X, padx=20, pady=10)
        opt_menu.bind("<Return>", (lambda event : self.getlink()))
        
        opt_menu = ctk.CTkButton(self.windows, text='link2', command=self.getlink2)
        opt_menu.pack(fill=tk.X, padx=20, pady=10)
        opt_menu.bind("<Return>", (lambda event : self.getlink2()))'''
        
        self.statePrimaryPage()
        self.windows.mainloop()
