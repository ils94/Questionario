import tkinter as tk
from PIL import Image, ImageTk
import base64
import io
import centralizarJanelas


def convert_and_display(string, label):
    image_data = base64.b64decode(string)

    image = Image.open(io.BytesIO(image_data))

    resized_image = ImageTk.PhotoImage(image)

    label.config(image=resized_image)
    label.image = resized_image


def mostrar(imagem):
    toplevel = tk.Toplevel()
    toplevel.title("Imagem")
    toplevel.geometry("500x500")
    toplevel.attributes("-topmost", True)
    toplevel.minsize(500, 500)
    centralizarJanelas.center_window(toplevel, 500, 500)

    label_imagem = tk.Label(toplevel)
    label_imagem.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    convert_and_display(imagem, label_imagem)
