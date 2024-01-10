import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import criarDB
import dbAcoes
import variaveisGlobais
import cleanText
import convertToBase64


def converter_imagem(event, entry):
    arquivo = filedialog.askopenfilename()

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
    enunciado = cleanText.clean_string(entry_1.get())

    if dbAcoes.verificar(enunciado):
        messagebox.showerror("Erro", "Questão já existe.")
        return
    else:
        dados = (enunciado,
                 cleanText.clean_string(entry_2.get("1.0", tk.END)),
                 cleanText.clean_string(entry_3.get()),
                 cleanText.clean_string(entry_4.get()),
                 cleanText.clean_string(entry_5.get()),
                 cleanText.clean_string(entry_6.get()),
                 cleanText.clean_string(entry_7.get()),
                 cleanText.clean_string(entry_8.get()),
                 entry_9.get("1.0", tk.END),
                 cleanText.clean_string(entry_10.get("1.0", tk.END)))

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

    enunciado = cleanText.clean_string(entry_1.get())

    resultado = dbAcoes.verificar_completo(enunciado)

    filtro = ""

    if resultado:
        for entry in [entry_1.get(), entry_2.get("1.0", tk.END), entry_3.get(), entry_4.get(), entry_5.get(),
                      entry_6.get(), entry_7.get(), entry_8.get(), entry_9.get("1.0", tk.END),
                      entry_10.get("1.0", tk.END)]:
            filtro = filtro + entry.replace(" ", "").replace("\n", "").strip()

        if resultado == filtro:
            messagebox.showerror("Erro", "Questão já existe.")
            return

    dados = (enunciado,
             cleanText.clean_string(entry_2.get("1.0", tk.END)),
             cleanText.clean_string(entry_3.get()),
             cleanText.clean_string(entry_4.get()),
             cleanText.clean_string(entry_5.get()),
             cleanText.clean_string(entry_6.get()),
             cleanText.clean_string(entry_7.get()),
             cleanText.clean_string(entry_8.get()),
             entry_9.get("1.0", tk.END),
             cleanText.clean_string(entry_10.get("1.0", tk.END)),
             variaveisGlobais.ID)

    dbAcoes.alterar(dados)


def deletar():
    dbAcoes.deletar(variaveisGlobais.ID)


def carregar_db():
    variaveisGlobais.dbNAME = filedialog.askopenfilename(defaultextension=".db", filetypes=[("DB files", "*.db")])


root = tk.Tk()
root.state("zoomed")
root.title("Criador ")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu_button = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=menu_button)

menu_button.add_command(label="Criar DB", command=criarDB.criar_db)
menu_button.add_command(label="Carregar DB", command=carregar_db)

width = 20

frame_1 = tk.Frame(root)
frame_1.pack(fill=tk.X, padx=5, pady=5)

frame_1_a = tk.Frame(frame_1)
frame_1_a.pack(fill=tk.X)

label_1 = tk.Label(frame_1_a, text="Enunciado:", width=width, anchor=tk.W)
label_1.pack(side=tk.LEFT)

entry_1 = tk.Entry(frame_1_a)
entry_1.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_b = tk.Frame(frame_1)
frame_1_b.pack(fill=tk.X)

label_2 = tk.Label(frame_1_b, text="Imagem do Enunciado:", width=width, anchor=tk.W)
label_2.pack(side=tk.LEFT)

entry_2 = tk.Text(frame_1_b, height=1)
entry_2.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry_2.bind("<Double-Button-1>", lambda event, entry=entry_2: converter_imagem(None, entry))

frame_1_c = tk.Frame(frame_1)
frame_1_c.pack(fill=tk.X)

label_3 = tk.Label(frame_1_c, text="Alternativa A:", width=width, anchor=tk.W)
label_3.pack(side=tk.LEFT)

entry_3 = tk.Entry(frame_1_c)
entry_3.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_d = tk.Frame(frame_1)
frame_1_d.pack(fill=tk.X)

label_4 = tk.Label(frame_1_d, text="Alternativa B:", width=width, anchor=tk.W)
label_4.pack(side=tk.LEFT)

entry_4 = tk.Entry(frame_1_d)
entry_4.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_e = tk.Frame(frame_1)
frame_1_e.pack(fill=tk.X)

label_5 = tk.Label(frame_1_e, text="Alternativa C:", width=width, anchor=tk.W)
label_5.pack(side=tk.LEFT)

entry_5 = tk.Entry(frame_1_e)
entry_5.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_f = tk.Frame(frame_1)
frame_1_f.pack(fill=tk.X)

label_6 = tk.Label(frame_1_f, text="Alternativa D:", width=width, anchor=tk.W)
label_6.pack(side=tk.LEFT)

entry_6 = tk.Entry(frame_1_f)
entry_6.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_g = tk.Frame(frame_1)
frame_1_g.pack(fill=tk.X)

label_7 = tk.Label(frame_1_g, text="Alternativa E:", width=width, anchor=tk.W)
label_7.pack(side=tk.LEFT)

entry_7 = tk.Entry(frame_1_g)
entry_7.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_h = tk.Frame(frame_1)
frame_1_h.pack(fill=tk.X)

label_8 = tk.Label(frame_1_h, text="Alternativa Correta:", width=width, anchor=tk.W)
label_8.pack(side=tk.LEFT)

entry_8 = tk.Entry(frame_1_h)
entry_8.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_1_i = tk.Frame(frame_1)
frame_1_i.pack(fill=tk.X, expand=True)

frame_1_i_a = tk.Frame(frame_1_i)
frame_1_i_a.pack(fill=tk.X, expand=True)

label_9 = tk.Label(frame_1_i_a, text="Explicação:", width=width, anchor=tk.W)
label_9.pack(side=tk.LEFT)

entry_9 = tk.Text(frame_1_i, height=10)
entry_9.pack(fill=tk.BOTH, expand=True)

frame_1_i_b = tk.Frame(frame_1_i)
frame_1_i_b.pack(fill=tk.X, expand=True)

label_10 = tk.Label(frame_1_i_b, text="Imagem da Explicação:", width=width, anchor=tk.W)
label_10.pack(side=tk.LEFT)

entry_10 = tk.Text(frame_1_i_b, height=1)
entry_10.pack(fill=tk.BOTH, expand=True, pady=5)
entry_10.bind("<Double-Button-1>", lambda event, entry=entry_10: converter_imagem(None, entry))

frame_2 = tk.Frame(frame_1)
frame_2.pack(fill=tk.X, pady=5)

button_adicionar = tk.Button(frame_2, text="Adicionar", width=15, command=inserir)
button_adicionar.pack(side=tk.LEFT)

button_editar = tk.Button(frame_2, text="Editar", width=15, command=alterar)
button_editar.pack(side=tk.LEFT, padx=5)

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
pesquisar_frame.pack(fill=tk.X, padx=2)

label_pesquisar = tk.Label(pesquisar_frame, text="Pesquisar:", anchor=tk.W)
label_pesquisar.pack(side=tk.LEFT)

entry_pesquisar = tk.Entry(pesquisar_frame)
entry_pesquisar.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=5)
entry_pesquisar.bind("<Return>", pesquisar)

variaveisGlobais.treeview = treeview
variaveisGlobais.pesquisar_entry = entry_pesquisar

root.mainloop()
