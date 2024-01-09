import sqlite3
import variaveisGlobais
import dbQueries
from tkinter import messagebox


def inserir(dados):
    try:
        conn = sqlite3.connect(variaveisGlobais.dbNAME)
        cursor = conn.cursor()

        cursor.execute(dbQueries.insert_query, dados)

        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def alterar(dados):
    try:
        conn = sqlite3.connect(variaveisGlobais.dbNAME)
        cursor = conn.cursor()

        cursor.execute(dbQueries.update_query, dados)

        conn.commit()
        conn.close()

        variaveisGlobais.ID = None

    except Exception as e:
        messagebox.showerror("Error", str(e))


def deletar(ID):
    try:
        conn = sqlite3.connect(variaveisGlobais.dbNAME)
        cursor = conn.cursor()

        cursor.execute(dbQueries.delete_query, (ID,))

        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def selecionar_questao():
    try:
        conn = sqlite3.connect(variaveisGlobais.dbNAME)
        cursor = conn.cursor()

        cursor.execute(dbQueries.select_query)
        random_row = cursor.fetchone()

        conn.close()

        return random_row
    except Exception as e:
        messagebox.showerror("Error", str(e))


def procurar():
    conn = sqlite3.connect(variaveisGlobais.dbNAME)
    cursor = conn.cursor()

    cursor.execute(dbQueries.search_query,
                   (f"%{variaveisGlobais.pesquisar_entry.get()}%",) * 7 + (variaveisGlobais.pesquisar_entry.get(),))

    search_results = cursor.fetchall()

    cursor.close()
    conn.close()

    for row in variaveisGlobais.treeview.get_children():
        variaveisGlobais.treeview.delete(row)

    for row in search_results:
        variaveisGlobais.treeview.insert('', 'end', values=row)
