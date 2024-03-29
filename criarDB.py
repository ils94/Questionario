import sqlite3
from tkinter import filedialog
import dbQueries
import variaveisGlobais
import os


def criar_db():
    output_file = filedialog.asksaveasfilename(defaultextension=".db", filetypes=[("DB files", "*.db")])

    if output_file:
        conn = sqlite3.connect(output_file)
        cursor = conn.cursor()

        cursor.execute(dbQueries.createDB)

        conn.commit()
        conn.close()

        variaveisGlobais.dbNAME = output_file

        filename = os.path.basename(output_file)

        filename = filename.replace(".db", "")

        variaveisGlobais.root.title(f"Criador - {filename}")
