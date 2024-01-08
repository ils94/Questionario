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
