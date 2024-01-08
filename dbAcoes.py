import sqlite3
import variaveisGlobais
import dbQueries


def inserir(dados):
    conn = sqlite3.connect(variaveisGlobais.dbNAME)
    cursor = conn.cursor()

    cursor.execute(dbQueries.insert_query, dados)

    conn.commit()
    conn.close()


def selecionar_questao():
    conn = sqlite3.connect(variaveisGlobais.dbNAME)
    cursor = conn.cursor()

    cursor.execute(dbQueries.select_query)
    random_row = cursor.fetchone()

    conn.close()

    return random_row
