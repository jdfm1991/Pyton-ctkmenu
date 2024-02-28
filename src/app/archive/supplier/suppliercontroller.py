import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from tkinter import ttk
from customtkinter import CTk, CTkFrame
from tkinter.font import BOLD

from src.app.archive.supplier.supplierwiew import SupplierPanel

class Supplier(SupplierPanel):
    #Metodo de inicializacion
    def __init__(self):
        super().__init__()
    
    def getChangeState(self):
        if self.statewindowsprimary is True:
            self.statewindowsprimary = False
        else:
            self.statewindowsprimary = True
    
    def getHome(self):
        self.supplier.destroy()
        #self.getChangeState()
