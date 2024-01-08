import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import base64
import io
import dbAcoes
import variaveisGlobais

correta = ""
acertos = 0
erros = 0


def conferir_resposta():
    global correta, acertos, erros

    print(var.get())

    user_choice = var.get()

    correct_answer = correta.upper()

    if correct_answer == "A":
        check_button1.configure(disabledforeground="green")
    elif correct_answer == "B":
        check_button2.configure(disabledforeground="green")
    elif correct_answer == "C":
        check_button3.configure(disabledforeground="green")
    elif correct_answer == "D":
        check_button4.configure(disabledforeground="green")
    elif correct_answer == "E":
        check_button5.configure(disabledforeground="green")

    if user_choice == correct_answer:
        if user_choice == "A":
            check_button1.configure(disabledforeground="green")
        elif user_choice == "B":
            check_button2.configure(disabledforeground="green")
        elif user_choice == "C":
            check_button3.configure(disabledforeground="green")
        elif user_choice == "D":
            check_button4.configure(disabledforeground="green")
        elif user_choice == "E":
            check_button5.configure(disabledforeground="green")

        acertos = acertos + 1

        label_corretas.config(text=f"Corretas: {acertos}")
    else:
        if user_choice == "A":
            check_button1.configure(disabledforeground="red")
        elif user_choice == "B":
            check_button2.configure(disabledforeground="red")
        elif user_choice == "C":
            check_button3.configure(disabledforeground="red")
        elif user_choice == "D":
            check_button4.configure(disabledforeground="red")
        elif user_choice == "E":
            check_button5.configure(disabledforeground="red")

        erros = erros + 1

        label_incorretas.config(text=f"Incorretas: {erros}")

    for button in [check_button1, check_button2, check_button3, check_button4, check_button5]:
        button.config(state="disabled")


def carregar_materia():
    variaveisGlobais.dbNAME = filedialog.askopenfilename(defaultextension=".db", filetypes=[("DB files", "*.db")])

    proxima_questao_button.config(state="normal")


def carregar_questao():
    global correta

    dados = dbAcoes.selecionar_questao()

    label_enunciado.config(text=dados[1])

    convert_and_display(dados[2])

    check_button1.config(text=dados[3])
    check_button2.config(text=dados[4])
    check_button3.config(text=dados[5])
    check_button4.config(text=dados[6])
    check_button5.config(text=dados[7])

    correta = dados[8]

    for button in [check_button1, check_button2, check_button3, check_button4, check_button5]:
        button.config(state="normal", disabledforeground="black")

    var.set(None)

    proxima_questao_button.config(text="Próxima Questão")


def convert_and_display(string):
    base64_string = string

    if base64_string:
        image_data = base64.b64decode(base64_string)

        image = Image.open(io.BytesIO(image_data))
        # Resize the image to a specific width and height
        resized_image = image.resize((200, 200))  # Change the dimensions as needed

        resized_image = ImageTk.PhotoImage(resized_image)

        label_imagem.config(image=resized_image)
        label_imagem.image = resized_image
    else:
        label_imagem.config(image="")


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

label_incorretas = tk.Label(frame_score, text="Incorretas: 0", anchor=tk.W, font=fonte, fg="red")
label_incorretas.pack(side=tk.RIGHT, padx=5, pady=5)

label_corretas = tk.Label(frame_score, text="Corretas: 0", anchor=tk.W, font=fonte, fg="green")
label_corretas.pack(side=tk.RIGHT, padx=5, pady=5)

frame_enunciado = tk.Frame(root)
frame_enunciado.pack(fill=tk.X, padx=5, pady=5)

# Create a label
label_enunciado = tk.Label(frame_enunciado, text="...", anchor=tk.W, font=fonte)
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

var = tk.StringVar()

var.set(None)

check_button1 = tk.Checkbutton(frame_a, text="...", variable=var, onvalue="A", font=fonte,
                               command=conferir_resposta)
check_button1.pack(side=tk.LEFT)

frame_b = tk.Frame(frame_alternativas)
frame_b.pack(fill=tk.X, padx=5, pady=5)

check_button2 = tk.Checkbutton(frame_b, text="...", variable=var, onvalue="B", font=fonte,
                               command=conferir_resposta)
check_button2.pack(side=tk.LEFT)

frame_c = tk.Frame(frame_alternativas)
frame_c.pack(fill=tk.X, padx=5, pady=5)

check_button3 = tk.Checkbutton(frame_c, text="...", variable=var, onvalue="C", font=fonte,
                               command=conferir_resposta)
check_button3.pack(side=tk.LEFT)

frame_d = tk.Frame(frame_alternativas)
frame_d.pack(fill=tk.X, padx=5, pady=5)

check_button4 = tk.Checkbutton(frame_d, text="...", variable=var, onvalue="D", font=fonte,
                               command=conferir_resposta)
check_button4.pack(side=tk.LEFT)

frame_e = tk.Frame(frame_alternativas)
frame_e.pack(fill=tk.X, padx=5, pady=5)

check_button5 = tk.Checkbutton(frame_e, text="...", variable=var, onvalue="E", font=fonte,
                               command=conferir_resposta)
check_button5.pack(side=tk.LEFT)

frame_imagem = tk.Frame(root)
frame_imagem.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

# imagem_button = tk.Button(frame_imagem, text="Mostrar Imagem", command=show_checked_items, font=fonte)
# imagem_button.pack(side=tk.LEFT)

proxima_questao_button = tk.Button(frame_imagem, text="Iniciar", command=carregar_questao, font=fonte)
proxima_questao_button.pack(side=tk.LEFT)

proxima_questao_button.config(state="disabled")

for button in [check_button1, check_button2, check_button3, check_button4, check_button5]:
    button.config(state="disabled")

# Run the Tkinter main loop
root.mainloop()
