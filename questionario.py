import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import base64
import io

import dbAcoes
import variaveisGlobais


def show_checked_items():
    checked_items = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]
    print("Checked items:", checked_items)


def carregar_materia():
    variaveisGlobais.dbNAME = filedialog.askopenfilename(defaultextension=".db", filetypes=[("DB files", "*.db")])


def carregar_questao():
    dados = dbAcoes.selecionar_questao()

    convert_and_display(dados[2])


def convert_and_display(string):
    base64_string = string
    image_data = base64.b64decode(base64_string)

    image = Image.open(io.BytesIO(image_data))
    # Resize the image to a specific width and height
    resized_image = image.resize((200, 200))  # Change the dimensions as needed

    resized_image = ImageTk.PhotoImage(resized_image)

    label_imagem.config(image=resized_image)
    label_imagem.image = resized_image


# Create a Tkinter window
root = tk.Tk()
root.state("zoomed")
root.minsize(800, 600)
root.title("PyQuestionario")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a menu button
menu_button = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=menu_button)

# Add options to the menu button
menu_button.add_command(label="Carregar Materia", command=carregar_materia)

fonte = ("Arial", 14)

image_path = "gato.jpg"
image = Image.open(image_path)
image = image.resize((200, 200))
photo = ImageTk.PhotoImage(image)

frame_score = tk.Frame(root)
frame_score.pack(fill=tk.X, padx=5, pady=1)

label_erros = tk.Label(frame_score, text="Erros: 0", anchor=tk.W, font=fonte, fg="red")
label_erros.pack(side=tk.RIGHT, padx=5, pady=5)

label_acertos = tk.Label(frame_score, text="Acertos: 0", anchor=tk.W, font=fonte, fg="green")
label_acertos.pack(side=tk.RIGHT, padx=5, pady=5)

frame_enunciado = tk.Frame(root)
frame_enunciado.pack(fill=tk.X, padx=5, pady=5)

# Create a label
label_enunciado = tk.Label(frame_enunciado, text="Enunciado da questão aqui.", anchor=tk.W, font=fonte)
label_enunciado.pack(side=tk.LEFT)

frame_imagem = tk.Frame(root)
frame_imagem.pack(fill=tk.X, padx=5, pady=5)

label_imagem = tk.Label(root, anchor=tk.W, font=fonte)
label_imagem.pack(padx=5, pady=10)

# imagem_button = tk.Button(frame_imagem, text="Mostrar Imagem", command=show_checked_items, font=fonte)
# imagem_button.pack(side=tk.LEFT)

frame_alternativas = tk.Frame(root)
frame_alternativas.pack(fill=tk.X, padx=5, pady=10)

frame_a = tk.Frame(frame_alternativas)
frame_a.pack(fill=tk.X, padx=5, pady=5)

var1 = tk.IntVar()
check_button1 = tk.Checkbutton(frame_a, text="A:    Alternativa A", variable=var1, font=fonte)
check_button1.pack(side=tk.LEFT)

frame_b = tk.Frame(frame_alternativas)
frame_b.pack(fill=tk.X, padx=5, pady=5)

var2 = tk.IntVar()
check_button2 = tk.Checkbutton(frame_b, text="B:    Alternativa B", variable=var2, font=fonte)
check_button2.pack(side=tk.LEFT)

frame_c = tk.Frame(frame_alternativas)
frame_c.pack(fill=tk.X, padx=5, pady=5)

var3 = tk.IntVar()
check_button3 = tk.Checkbutton(frame_c, text="C:    Alternativa C", variable=var3, font=fonte)
check_button3.pack(side=tk.LEFT)

frame_d = tk.Frame(frame_alternativas)
frame_d.pack(fill=tk.X, padx=5, pady=5)

var4 = tk.IntVar()
check_button4 = tk.Checkbutton(frame_d, text="D:    Alternativa D", variable=var4, font=fonte)
check_button4.pack(side=tk.LEFT)

frame_e = tk.Frame(frame_alternativas)
frame_e.pack(fill=tk.X, padx=5, pady=5)

var5 = tk.IntVar()
check_button5 = tk.Checkbutton(frame_e, text="E:    Alternativa E", variable=var5, font=fonte)
check_button5.pack(side=tk.LEFT)

frame_imagem = tk.Frame(root)
frame_imagem.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

# imagem_button = tk.Button(frame_imagem, text="Mostrar Imagem", command=show_checked_items, font=fonte)
# imagem_button.pack(side=tk.LEFT)

proxima_questao_button = tk.Button(frame_imagem, text="Proxima Questão", command=carregar_questao, font=fonte)
proxima_questao_button.pack(side=tk.LEFT)

# Run the Tkinter main loop
root.mainloop()
