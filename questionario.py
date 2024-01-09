import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import base64
import io
import dbAcoes
import variaveisGlobais
import checkBase64
import textwrap

correta = ""
acertos = 0
erros = 0
dados = []


def text_wrap(text):
    max_characters_per_line = 200

    wrapped = textwrap.fill(text, width=max_characters_per_line)

    return wrapped


def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


def on_canvas_mousewheel(event):
    on_mouse_wheel(event)


def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


def on_canvas_configure(event):
    canvas.itemconfig(canvas_id, width=event.width)


def conferir_resposta():
    global correta, acertos, erros, dados

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

    if checkBase64.is_valid_image(dados[9]):
        label_imagem_explicacao.pack(fill=tk.BOTH)
        convert_and_display(dados[9], label_imagem_explicacao)
    else:
        explicacao_text.config(state="normal")
        explicacao_text.pack(fill=tk.BOTH)
        explicacao_text.delete("1.0", tk.END)
        explicacao_text.insert(tk.END, str(dados[9]))
        explicacao_text.config(state="disabled")


def carregar_materia():
    variaveisGlobais.dbNAME = filedialog.askopenfilename(defaultextension=".db", filetypes=[("DB files", "*.db")])

    carregar_questao(None)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


def carregar_questao(event):
    global correta, dados

    explicacao_text.forget()
    label_imagem_explicacao.forget()

    dados = dbAcoes.selecionar_questao()

    label_enunciado.config(text=text_wrap(dados[1]))

    if checkBase64.is_valid_image(dados[2]):
        convert_and_display(dados[2], label_imagem)
    else:
        convert_and_display("", label_imagem)

    check_button1.config(text="A    " + text_wrap(dados[3]))
    check_button2.config(text="B    " + text_wrap(dados[4]))
    check_button3.config(text="C    " + text_wrap(dados[5]))
    check_button4.config(text="D    " + text_wrap(dados[6]))
    check_button5.config(text="E    " + text_wrap(dados[7]))

    correta = dados[8]

    for button in [check_button1, check_button2, check_button3, check_button4, check_button5]:
        button.config(state="normal", disabledforeground="black")

    var.set(None)


def convert_and_display(string, label):
    base64_string = string

    if base64_string:
        image_data = base64.b64decode(base64_string)

        image = Image.open(io.BytesIO(image_data))
        resized_image = image.resize((300, 300))

        resized_image = ImageTk.PhotoImage(resized_image)

        label.config(image=resized_image)
        label.image = resized_image
    else:
        label.config(image="")


root = tk.Tk()
root.state("zoomed")
root.minsize(800, 600)
root.title("PyQuestionario")
root.bind("<space>", carregar_questao)
root.bind_all("<MouseWheel>", on_canvas_mousewheel)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu_button = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=menu_button)

menu_button.add_command(label="Carregar Materia", command=carregar_materia)

fonte = ("Arial", 14)

canvas = tk.Canvas(root)
canvas.bind('<Configure>', on_canvas_configure)

frame_canvas = tk.Frame(canvas)
canvas_id = canvas.create_window((0, 0), window=frame_canvas, anchor="w")

frame_canvas.bind("<Configure>", on_configure)

frame_score = tk.Frame(frame_canvas)
frame_score.pack(fill=tk.X, padx=5, pady=1)

label_incorretas = tk.Label(frame_score, text="Incorretas: 0", anchor=tk.W, font=fonte, fg="red")
label_incorretas.pack(side=tk.RIGHT, padx=5, pady=5)

label_corretas = tk.Label(frame_score, text="Corretas: 0", anchor=tk.W, font=fonte, fg="green")
label_corretas.pack(side=tk.RIGHT, padx=5, pady=5)

frame_enunciado = tk.Frame(frame_canvas)
frame_enunciado.pack(fill=tk.X, padx=5, pady=5)

label_enunciado = tk.Label(frame_enunciado, anchor=tk.W, font=fonte, justify=tk.LEFT)
label_enunciado.pack(side=tk.LEFT)

frame_imagem = tk.Frame(frame_canvas)
frame_imagem.pack(fill=tk.X, padx=5, pady=5)

label_imagem = tk.Label(frame_canvas)
label_imagem.pack(padx=5, pady=10)

frame_alternativas = tk.Frame(frame_canvas)
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

frame_explicacao = tk.Frame(frame_canvas)
frame_explicacao.pack(fill=tk.X, padx=5, pady=5)

explicacao_text = tk.Text(frame_explicacao)
label_imagem_explicacao = tk.Label(frame_explicacao)

for button in [check_button1, check_button2, check_button3, check_button4, check_button5]:
    button.config(state="disabled")

root.mainloop()
