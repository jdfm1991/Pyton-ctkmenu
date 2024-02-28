from PIL import ImageTk, Image

#Metodo utilizado para redimensionar las imagenen que se utilizan  la aplicacion
def read_img(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

#Metodo utilizado para cengtralizar la ventana de la aplicacion 
def center_windows(windows, app_width, app_height):
    screen_width = windows.winfo_screenwidth()
    screen_height =windows.winfo_screenheight()
    x = int((screen_width/2) - (app_width/2))
    y = int((screen_height/2) - (app_height/2))
    return windows.geometry(f"{app_width}x{app_height}+{x}+{y}")
    