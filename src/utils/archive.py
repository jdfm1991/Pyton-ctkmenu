from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk

class ArchiveVariable():
    
    def __init__(self):
        super().__init__()
        
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