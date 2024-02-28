import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from tkinter import ttk, messagebox
from customtkinter import CTk, CTkFrame
from tkinter.font import BOLD
import src.utils.generic as util

from src.app.master.masterview import MasterPanel
from src.app.user.usercontroller import User
from src.app.archive.supplier.suppliercontroller import Supplier

class Master(MasterPanel):
    #Metodo de inicializacion
    def __init__(self):
        super().__init__()
        
    def close(self):
        messagebox.showinfo(message='No puede Cerra la ventana principal, existen ventanas secundarias abiertas', title='Confimar Cierre')
        if self.statewindowsprimary is True:
            self.windows.destroy()
            
    def getChangeState(self):
        if self.statewindowsprimary is True:
            self.statewindowsprimary = False
        else:
            self.statewindowsprimary = True
    
        
    def statePrimaryPage(self):
        if self.statewindowsprimary is False:
            self.windows.protocol("WM_DELETE_WINDOW", lambda: None)
        else:
            self.windows.protocol("WM_DELETE_WINDOW", self.close)
              
    def getPageHome(self):
        self.main_page.select([self.home_frame])
        self.home_frame.columnconfigure(0, weight=1)
        self.home_frame.rowconfigure(0, weight=1)
        
    def getPageArchive(self):
        self.main_page.select([self.archive_frame])
        self.archive_frame.columnconfigure(0, weight=1)
        self.archive_frame.rowconfigure(0, weight=1)
        
    def getPageTransaction(self):
        self.main_page.select([self.transaction_frame])
        self.transaction_frame.columnconfigure(0, weight=1)
        self.transaction_frame.rowconfigure(0, weight=1)
        
    def getPageReport(self):
        self.main_page.select([self.report_frame])
        self.report_frame.columnconfigure(0, weight=1)
        self.report_frame.rowconfigure(0, weight=1)
        
    def getPageSetting(self):
        self.main_page.select([self.setting_frame])
        self.setting_frame.columnconfigure(0, weight=1)
        self.setting_frame.rowconfigure(0, weight=1)
        
    def getPagePlus(self):
        self.main_page.select([self.various_frame])
        self.various_frame.columnconfigure(0, weight=1)
        self.various_frame.rowconfigure(0, weight=1)
        
    def getUserSetting(self):
        self.windows.destroy()
        User()
    
    def getSupplier(self):
        #self.windows.destroy()
        self.getChangeState()
        Supplier()