import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import criarDB
import dbAcoes
import variaveisGlobais
import cleanText


def inserir():
    if entry_1.get() == "" or entry_3.get() == "" or entry_4.get() == "" or entry_5.get() == "" or entry_6.get() == "" or entry_7.get() == "" or entry_8.get() == "":
        messagebox.showerror("Erro", "É necessario o Enunciado, as alternativas e a alternativa correta.")
    else:
        dados = (cleanText.clean_string(entry_1.get()),
                 cleanText.clean_string(entry_2.get()),
                 cleanText.clean_string(entry_3.get()),
                 cleanText.clean_string(entry_4.get()),
                 cleanText.clean_string(entry_5.get()),
                 cleanText.clean_string(entry_6.get()),
                 cleanText.clean_string(entry_7.get()),
                 cleanText.clean_string(entry_8.get()),
                 entry_9.get("1.0", tk.END))

        dbAcoes.inserir(dados)


def carregar_db():
    variaveisGlobais.dbNAME = filedialog.askopenfilename(defaultextension=".db", filetypes=[("DB files", "*.db")])


root = tk.Tk()
root.state("zoomed")
root.minsize(800, 600)
root.title("Criador ")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu_button = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=menu_button)

menu_button.add_command(label="Criar DB", command=criarDB.criar_db)
menu_button.add_command(label="Carregar DB", command=carregar_db)

width = 15

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

label_2 = tk.Label(frame_1_b, text="Imagem:", width=width, anchor=tk.W)
label_2.pack(side=tk.LEFT)

entry_2 = tk.Entry(frame_1_b)
entry_2.pack(side=tk.LEFT, fill=tk.X, expand=True)

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

frame_2 = tk.Frame(frame_1)
frame_2.pack(fill=tk.X, pady=5)

button_adicionar = tk.Button(frame_2, text="Adicionar", width=15, command=inserir)
button_adicionar.pack(side=tk.LEFT)

button_editar = tk.Button(frame_2, text="Editar", width=15)
button_editar.pack(side=tk.LEFT, padx=5)

button_deletar = tk.Button(frame_2, text="Deletar", width=15)
button_deletar.pack(side=tk.RIGHT)

tree_frame = tk.Frame(root)
tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

treeview = ttk.Treeview(tree_frame, show="headings", selectmode="browse")

treeview['columns'] = ("ID", "ENUNCIADO", "IMAGEM", "ALTERNATIVA A", "ALTERNATIVA B", "ALTERNATIVA C", "ALTERNATIVA D",
                       "ALTERNATIVA E", "ALTERNATIVA CORRETA", "EXPLICAÇÃO")

treeview.column("#0", width=0, minwidth=0)
treeview.column("ID", width=10, minwidth=10)

treeview.heading("#0", text="")
treeview.heading("ID", text="ID")
treeview.heading("ENUNCIADO", text="ENUNCIADO")
treeview.heading("IMAGEM", text="IMAGEM")
treeview.heading("ALTERNATIVA A", text="ALTERNATIVA A")
treeview.heading("ALTERNATIVA B", text="ALTERNATIVA B")
treeview.heading("ALTERNATIVA C", text="ALTERNATIVA C")
treeview.heading("ALTERNATIVA D", text="ALTERNATIVA D")
treeview.heading("ALTERNATIVA E", text="ALTERNATIVA E")
treeview.heading("ALTERNATIVA CORRETA", text="ALTERNATIVA CORRETA")
treeview.heading("EXPLICAÇÃO", text="EXPLICAÇÃO")

tree_frame.grid_rowconfigure(0, weight=1)
tree_frame.grid_columnconfigure(0, weight=1)

vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=treeview.yview)
vsb.grid(row=0, column=1, sticky="ns")
treeview.configure(yscrollcommand=vsb.set)

hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=treeview.xview)
hsb.grid(row=1, column=0, sticky="ew")
treeview.configure(xscrollcommand=hsb.set)

treeview.grid(row=0, column=0, sticky="nsew")

pesquisar_frame = tk.Frame(root)
pesquisar_frame.pack(fill=tk.X, padx=2)

label_pesquisar = tk.Label(pesquisar_frame, text="Pesquisar:", anchor=tk.W)
label_pesquisar.pack(side=tk.LEFT)

entry_pesquisar = tk.Entry(pesquisar_frame)
entry_pesquisar.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=5)

root.mainloop()
