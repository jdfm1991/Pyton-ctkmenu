import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from tkinter import ttk, messagebox
from customtkinter import CTk, CTkFrame
from tkinter.font import BOLD

import src.utils.generic as util
import src.utils.encryp as en

from src.app.login.registerview import RegisterPanel

class Register(RegisterPanel):
    #Metodo de inicializacion (Se establece la tabla en la que se realizaran las consultas)
    def __init__(self):
        super().__init__()