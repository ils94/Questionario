import tkinter as tk
from tkinter import filedialog
import dbAcoes
import variaveisGlobais
import checkBase64
import textwrap
import mostrarImagem
import os

correta = ""
corretas = 0
incorretas = 0
dados = []
respondida = True


def abrir_criador():
    os.startfile("criador.exe")


def text_wrap(text):
    max_characters_per_line = 150

    wrapped = textwrap.fill(text, width=max_characters_per_line)

    return wrapped


def conferir_resposta():
    global correta, corretas, incorretas, dados, respondida

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

        corretas = corretas + 1

        label_corretas.config(text=f"{corretas} CORRETAS")
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

        incorretas = incorretas + 1

        label_incorretas.config(text=f"INCORRETAS {incorretas}")

    for button in [check_button1, check_button2, check_button3, check_button4, check_button5]:
        button.config(state="disabled")

        explicacao_text.config(state="normal")
        explicacao_text.pack(fill=tk.BOTH, expand=True)
        explicacao_text.delete("1.0", tk.END)
        explicacao_text.insert(tk.END, str(dados[9]))
        explicacao_text.config(state="disabled")

        if checkBase64.is_valid_image(dados[10]):
            button_explicacao_imagem.pack(side=tk.LEFT, pady=5)
            button_explicacao_imagem.configure(command=lambda: mostrarImagem.mostrar(dados[10]))

        respondida = True


def carregar_materia():
    global corretas, incorretas, respondida

    db = filedialog.askopenfilename(defaultextension=".db", filetypes=[("DB files", "*.db")])

    if db:
        filename = os.path.basename(db)

        filename = filename.replace(".db", "")

        root.title(f"Questionario - {filename}")

        variaveisGlobais.dbNAME = db

        corretas = 0
        incorretas = 0

        label_corretas.configure(text="0 CORRETAS")
        label_incorretas.configure(text="INCORRETAS 0")

        frame_ui.pack(fill=tk.BOTH, expand=True)

        respondida = True

        carregar_questao(None)


def carregar_questao(event):
    global correta, dados, respondida

    if respondida:
        explicacao_text.forget()
        button_explicacao_imagem.forget()

        dados = dbAcoes.selecionar_questao()

        label_enunciado.config(text=text_wrap(dados[1]))

        if checkBase64.is_valid_image(dados[2]):
            button_imagem.pack(side=tk.LEFT, padx=5, pady=5)
            button_imagem.configure(command=lambda: mostrarImagem.mostrar(dados[2]))
        else:
            button_imagem.forget()

        if dados[3]:
            check_button1.pack(side=tk.LEFT)
            check_button1.config(text="A) " + text_wrap(dados[3]))
        else:
            check_button1.forget()

        if dados[4]:
            check_button2.pack(side=tk.LEFT)
            check_button2.config(text="B) " + text_wrap(dados[4]))
        else:
            check_button2.forget()

        if dados[5]:
            check_button3.pack(side=tk.LEFT)
            check_button3.config(text="C) " + text_wrap(dados[5]))
        else:
            check_button3.forget()

        if dados[6]:
            check_button4.pack(side=tk.LEFT)
            check_button4.config(text="D) " + text_wrap(dados[6]))
        else:
            check_button4.forget()

        if dados[7]:
            check_button5.pack(side=tk.LEFT)
            check_button5.config(text="E) " + text_wrap(dados[7]))
        else:
            check_button5.forget()

        correta = dados[8]

        for button in [check_button1, check_button2, check_button3, check_button4, check_button5]:
            button.config(state="normal", disabledforeground="black")

        var.set(None)

        respondida = False


root = tk.Tk()
root.state("zoomed")
root.title("Questionario")
root.bind("<space>", carregar_questao)
if os.path.isfile("questionarioicon.ico"):
    root.iconbitmap("questionarioicon.ico")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu_button = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=menu_button)

menu_button.add_command(label="Carregar Materia", command=carregar_materia)
menu_button.add_separator()
menu_button.add_command(label="Abrir Criador", command=abrir_criador)

fonte = ("Arial", 12, "bold")

frame_ui = tk.Frame(root)

frame_score = tk.Frame(frame_ui)
frame_score.pack(padx=5, pady=5)

frame_score_1 = tk.Frame(frame_score)
frame_score_1.grid(row=0, column=0)

label_incorretas = tk.Label(frame_score_1, font=fonte, fg="red")
label_incorretas.pack()

frame_score_2 = tk.Frame(frame_score)
frame_score_2.grid(row=0, column=1)

label_separador = tk.Label(frame_score_2, text="|", font=fonte, fg="black")
label_separador.pack()

frame_score_3 = tk.Frame(frame_score)
frame_score_3.grid(row=0, column=2)

label_corretas = tk.Label(frame_score_3, font=fonte, fg="green")
label_corretas.pack()

frame_enunciado = tk.Frame(frame_ui)
frame_enunciado.pack(fill=tk.X, padx=5, pady=10)

label_enunciado = tk.Label(frame_enunciado, anchor=tk.W, font=fonte, justify=tk.LEFT)
label_enunciado.pack(side=tk.LEFT)

frame_imagem = tk.Frame(frame_ui)
frame_imagem.pack(fill=tk.X)

button_imagem = tk.Button(frame_imagem, text="Imagem", font=fonte)

frame_alternativas = tk.Frame(frame_ui)
frame_alternativas.pack(fill=tk.X, padx=5, pady=10)

frame_a = tk.Frame(frame_alternativas)
frame_a.pack(fill=tk.X, padx=5, pady=5)

var = tk.StringVar()

var.set(None)

check_button1 = tk.Checkbutton(frame_a, variable=var, onvalue="A", justify="left", font=fonte,
                               command=conferir_resposta)
check_button1.pack(side=tk.LEFT)

frame_b = tk.Frame(frame_alternativas)
frame_b.pack(fill=tk.X, padx=5, pady=5)

check_button2 = tk.Checkbutton(frame_b, variable=var, onvalue="B", justify="left", font=fonte,
                               command=conferir_resposta)
check_button2.pack(side=tk.LEFT)

frame_c = tk.Frame(frame_alternativas)
frame_c.pack(fill=tk.X, padx=5, pady=5)

check_button3 = tk.Checkbutton(frame_c, variable=var, onvalue="C", justify="left", font=fonte,
                               command=conferir_resposta)
check_button3.pack(side=tk.LEFT)

frame_d = tk.Frame(frame_alternativas)
frame_d.pack(fill=tk.X, padx=5, pady=5)

check_button4 = tk.Checkbutton(frame_d, variable=var, onvalue="D", justify="left", font=fonte,
                               command=conferir_resposta)
check_button4.pack(side=tk.LEFT)

frame_e = tk.Frame(frame_alternativas)
frame_e.pack(fill=tk.X, padx=5, pady=5)

check_button5 = tk.Checkbutton(frame_e, variable=var, onvalue="E", justify="left", font=fonte,
                               command=conferir_resposta)
check_button5.pack(side=tk.LEFT)

frame_explicacao = tk.Frame(frame_ui)
frame_explicacao.pack(fill=tk.X, padx=5, pady=5)

explicacao_text = tk.Text(frame_explicacao, height=10)
button_explicacao_imagem = tk.Button(frame_explicacao, text="Imagem", font=fonte)

root.mainloop()
