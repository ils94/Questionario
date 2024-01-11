import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import criarDB
import dbAcoes
import variaveisGlobais
import cleanText
import convertToBase64
import os


def apagar_tudo():

    variaveisGlobais.ID = None

    entry_1.delete(0, tk.END)
    entry_2.delete("1.0", tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)
    entry_5.delete(0, tk.END)
    entry_6.delete(0, tk.END)
    entry_7.delete(0, tk.END)
    entry_8.delete(0, tk.END)
    entry_9.delete("1.0", tk.END)
    entry_10.delete("1.0", tk.END)


def abrir_questionario():
    os.startfile("questionario.exe")


def verificar_questao_existente(enunciado):
    resultado = dbAcoes.verificar_completo(enunciado)

    filtro = ""

    if resultado:
        for entry in [entry_1.get(), entry_2.get("1.0", tk.END), entry_3.get(), entry_4.get(), entry_5.get(),
                      entry_6.get(), entry_7.get(), entry_8.get(), entry_9.get("1.0", tk.END),
                      entry_10.get("1.0", tk.END)]:
            filtro = filtro + entry.strip()

        if resultado == filtro:
            messagebox.showerror("Erro", "Questão já existe.")
            return True
        else:
            return False


def converter_imagem(event, entry):
    image_types = [('Image Files', '*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.ico')]

    arquivo = filedialog.askopenfilename(filetypes=image_types)

    if arquivo:
        entry.insert("1.0", convertToBase64.image_to_base64(arquivo))


def on_click(event):
    item = treeview.item(treeview.focus())
    values = item["values"]

    variaveisGlobais.ID = values[0]

    entry_1.delete(0, tk.END)
    entry_2.delete("1.0", tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)
    entry_5.delete(0, tk.END)
    entry_6.delete(0, tk.END)
    entry_7.delete(0, tk.END)
    entry_8.delete(0, tk.END)
    entry_9.delete("1.0", tk.END)
    entry_10.delete("1.0", tk.END)

    entry_1.insert(tk.END, values[1])
    entry_2.insert("1.0", values[2])
    entry_3.insert(tk.END, values[3])
    entry_4.insert(tk.END, values[4])
    entry_5.insert(tk.END, values[5])
    entry_6.insert(tk.END, values[6])
    entry_7.insert(tk.END, values[7])
    entry_8.insert(tk.END, values[8])
    entry_9.insert(tk.END, values[9])
    entry_10.insert("1.0", values[10])


def pesquisar(event):
    dbAcoes.procurar()


def inserir():
    enunciado = cleanText.clean_string_line_breakers(entry_1.get())

    if not verificar_questao_existente(enunciado):
        dados = (enunciado,
                 cleanText.clean_string_spaces(entry_2.get("1.0", "end-1c")),
                 cleanText.clean_string_spaces(entry_3.get()),
                 cleanText.clean_string_spaces(entry_4.get()),
                 cleanText.clean_string_spaces(entry_5.get()),
                 cleanText.clean_string_spaces(entry_6.get()),
                 cleanText.clean_string_spaces(entry_7.get()),
                 cleanText.clean_string_spaces(entry_8.get()),
                 cleanText.clean_string_line_breakers(entry_9.get("1.0", "end-1c")),
                 cleanText.clean_string_spaces(entry_10.get("1.0", "end-1c")))

        dbAcoes.inserir(dados)

        entry_1.delete(0, tk.END)
        entry_2.delete("1.0", tk.END)
        entry_3.delete(0, tk.END)
        entry_4.delete(0, tk.END)
        entry_5.delete(0, tk.END)
        entry_6.delete(0, tk.END)
        entry_7.delete(0, tk.END)
        entry_8.delete(0, tk.END)
        entry_9.delete("1.0", tk.END)
        entry_10.delete("1.0", tk.END)


def alterar():
    if not variaveisGlobais.ID:
        messagebox.showerror("Erro", "Selecione um item para alteração.")
        return

    enunciado = cleanText.clean_string_spaces(entry_1.get())

    if not verificar_questao_existente(enunciado):
        dados = (enunciado,
                 cleanText.clean_string_spaces(entry_2.get("1.0", "end-1c")),
                 cleanText.clean_string_spaces(entry_3.get()),
                 cleanText.clean_string_spaces(entry_4.get()),
                 cleanText.clean_string_spaces(entry_5.get()),
                 cleanText.clean_string_spaces(entry_6.get()),
                 cleanText.clean_string_spaces(entry_7.get()),
                 cleanText.clean_string_spaces(entry_8.get()),
                 cleanText.clean_string_line_breakers(entry_9.get("1.0", "end-1c")),
                 cleanText.clean_string_spaces(entry_10.get("1.0", "end-1c")),
                 variaveisGlobais.ID)

        dbAcoes.alterar(dados)


def deletar():
    dbAcoes.deletar(variaveisGlobais.ID)


def carregar_db():
    db = filedialog.askopenfilename(defaultextension=".db", filetypes=[("DB files", "*.db")])

    if db:
        filename = os.path.basename(db)

        filename = filename.replace(".db", "")

        root.title(f"Criador - {filename}")

        variaveisGlobais.dbNAME = db


root = tk.Tk()
root.state("zoomed")
root.title("Criador")
if os.path.isfile("criadoricon.ico"):
    root.iconbitmap("criadoricon.ico")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu_button = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=menu_button)

menu_button.add_command(label="Criar DB", command=criarDB.criar_db)
menu_button.add_command(label="Carregar DB", command=carregar_db)
menu_button.add_separator()
menu_button.add_command(label="Abrir Questionario", command=abrir_questionario)

width = 25

frame_1 = tk.Frame(root)
frame_1.pack(fill=tk.X, padx=5, pady=5)

frame_1_a = tk.Frame(frame_1)
frame_1_a.pack(fill=tk.X, pady=3)

label_1 = tk.Label(frame_1_a, text="Enunciado:", width=width, anchor=tk.W)
label_1.pack(side=tk.LEFT)

entry_1 = tk.Entry(frame_1_a)
entry_1.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_b = tk.Frame(frame_1)
frame_1_b.pack(fill=tk.X, pady=3)

label_2 = tk.Label(frame_1_b, text="Imagem do Enunciado (Base64):", width=width, anchor=tk.W)
label_2.pack(side=tk.LEFT)

button_selecionar_imagem_enunciado = tk.Button(frame_1_b, text="Abrir")
button_selecionar_imagem_enunciado.pack(side=tk.LEFT)

entry_2 = tk.Text(frame_1_b, height=1)
entry_2.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
entry_2.bind("<Double-Button-1>", lambda: converter_imagem(None, entry_2))

button_selecionar_imagem_enunciado.configure(command=lambda: converter_imagem(None, entry_2))

frame_1_c = tk.Frame(frame_1)
frame_1_c.pack(fill=tk.X, pady=3)

label_3 = tk.Label(frame_1_c, text="Alternativa A:", width=width, anchor=tk.W)
label_3.pack(side=tk.LEFT)

entry_3 = tk.Entry(frame_1_c)
entry_3.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_d = tk.Frame(frame_1)
frame_1_d.pack(fill=tk.X, pady=3)

label_4 = tk.Label(frame_1_d, text="Alternativa B:", width=width, anchor=tk.W)
label_4.pack(side=tk.LEFT)

entry_4 = tk.Entry(frame_1_d)
entry_4.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_e = tk.Frame(frame_1)
frame_1_e.pack(fill=tk.X, pady=3)

label_5 = tk.Label(frame_1_e, text="Alternativa C:", width=width, anchor=tk.W)
label_5.pack(side=tk.LEFT)

entry_5 = tk.Entry(frame_1_e)
entry_5.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_f = tk.Frame(frame_1)
frame_1_f.pack(fill=tk.X, pady=3)

label_6 = tk.Label(frame_1_f, text="Alternativa D:", width=width, anchor=tk.W)
label_6.pack(side=tk.LEFT)

entry_6 = tk.Entry(frame_1_f)
entry_6.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_g = tk.Frame(frame_1)
frame_1_g.pack(fill=tk.X, pady=3)

label_7 = tk.Label(frame_1_g, text="Alternativa E:", width=width, anchor=tk.W)
label_7.pack(side=tk.LEFT)

entry_7 = tk.Entry(frame_1_g)
entry_7.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_h = tk.Frame(frame_1)
frame_1_h.pack(fill=tk.X, pady=3)

label_8 = tk.Label(frame_1_h, text="Alternativa Correta:", width=width, anchor=tk.W)
label_8.pack(side=tk.LEFT)

entry_8 = tk.Entry(frame_1_h)
entry_8.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_i = tk.Frame(frame_1)
frame_1_i.pack(fill=tk.X, pady=3)

frame_1_i_a = tk.Frame(frame_1_i)
frame_1_i_a.pack(fill=tk.X, expand=True, pady=3)

label_9 = tk.Label(frame_1_i_a, text="Explicação:", width=width, anchor=tk.W)
label_9.pack(side=tk.LEFT)

entry_9 = tk.Text(frame_1_i, height=10)
entry_9.pack(fill=tk.BOTH, expand=True)

frame_1_i_b = tk.Frame(frame_1_i)
frame_1_i_b.pack(fill=tk.X, expand=True, pady=3)

label_10 = tk.Label(frame_1_i_b, text="Imagem da Explicação (Base64):", width=width, anchor=tk.W)
label_10.pack(side=tk.LEFT)

button_selecionar_imagem_explicacao = tk.Button(frame_1_i_b, text="Abrir")
button_selecionar_imagem_explicacao.pack(side=tk.LEFT)

entry_10 = tk.Text(frame_1_i_b, height=1)
entry_10.pack(fill=tk.X, expand=True, padx=5)
entry_10.bind("<Double-Button-1>", lambda event, entry=entry_10: converter_imagem(None, entry))

button_selecionar_imagem_explicacao.configure(command=lambda: converter_imagem(None, entry_10))

frame_2 = tk.Frame(frame_1)
frame_2.pack(fill=tk.X, pady=3)

button_adicionar = tk.Button(frame_2, text="Adicionar", width=15, command=inserir)
button_adicionar.pack(side=tk.LEFT)

button_editar = tk.Button(frame_2, text="Alterar", width=15, command=alterar)
button_editar.pack(side=tk.LEFT, padx=5)

button_apagar = tk.Button(frame_2, text="Apagar Tudo", width=15, command=apagar_tudo)
button_apagar.pack(side=tk.LEFT)

button_deletar = tk.Button(frame_2, text="Deletar", width=15, command=deletar)
button_deletar.pack(side=tk.RIGHT)

tree_frame = tk.Frame(root)
tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

treeview = ttk.Treeview(tree_frame, show="headings", selectmode="browse")

treeview['columns'] = (
    "ID", "ENUNCIADO", "IMAGEM DO ENUNCIADO", "ALTERNATIVA A", "ALTERNATIVA B", "ALTERNATIVA C", "ALTERNATIVA D",
    "ALTERNATIVA E", "ALTERNATIVA CORRETA", "EXPLICAÇÃO", "IMAGEM DA EXPLICAÇÃO")

treeview.column("#0", width=0, minwidth=0)
treeview.column("ID", width=10, minwidth=10)

treeview.heading("#0", text="")
treeview.heading("ID", text="ID")
treeview.heading("ENUNCIADO", text="ENUNCIADO")
treeview.heading("IMAGEM DO ENUNCIADO", text="IMAGEM DO ENUNCIADO")
treeview.heading("ALTERNATIVA A", text="ALTERNATIVA A")
treeview.heading("ALTERNATIVA B", text="ALTERNATIVA B")
treeview.heading("ALTERNATIVA C", text="ALTERNATIVA C")
treeview.heading("ALTERNATIVA D", text="ALTERNATIVA D")
treeview.heading("ALTERNATIVA E", text="ALTERNATIVA E")
treeview.heading("ALTERNATIVA CORRETA", text="ALTERNATIVA CORRETA")
treeview.heading("EXPLICAÇÃO", text="EXPLICAÇÃO")
treeview.heading("IMAGEM DA EXPLICAÇÃO", text="IMAGEM DA EXPLICAÇÃO")

tree_frame.grid_rowconfigure(0, weight=1)
tree_frame.grid_columnconfigure(0, weight=1)

vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=treeview.yview)
vsb.grid(row=0, column=1, sticky="ns")
treeview.configure(yscrollcommand=vsb.set)

hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=treeview.xview)
hsb.grid(row=1, column=0, sticky="ew")
treeview.configure(xscrollcommand=hsb.set)

treeview.grid(row=0, column=0, sticky="nsew")

treeview.bind("<<TreeviewSelect>>", on_click)

pesquisar_frame = tk.Frame(root)
pesquisar_frame.pack(fill=tk.X, padx=5, pady=5)

label_pesquisar = tk.Label(pesquisar_frame, text="Pesquisar:", anchor=tk.W)
label_pesquisar.pack(side=tk.LEFT)

entry_pesquisar = tk.Entry(pesquisar_frame)
entry_pesquisar.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=5)
entry_pesquisar.bind("<Return>", pesquisar)

variaveisGlobais.treeview = treeview
variaveisGlobais.pesquisar_entry = entry_pesquisar

root.mainloop()
