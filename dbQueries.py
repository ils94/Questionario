createDB = """
CREATE TABLE IF NOT EXISTS QUESTOES (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Enunciado TEXT,
Image BLOB,
Alternativa_A TEXT,
Alternativa_B TEXT,
Alternativa_C TEXT,
Alternativa_D TEXT,
Alternativa_E TEXT,
Alternativa_Correta TEXT,
Explicacao BLOB
);
"""

insert_query = "INSERT INTO QUESTOES (Enunciado, Image, Alternativa_A, Alternativa_B, Alternativa_C, Alternativa_D, Alternativa_E, Alternativa_Correta, Explicacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

update_query = """
UPDATE QUESTOES
SET Enunciado = ?,
Image = ?,
Alternativa_A = ?,
Alternativa_B = ?,
Alternativa_C = ?,
Alternativa_D = ?,
Alternativa_E = ?,
Alternativa_Correta = ?,
Explicacao = ?
WHERE ID = ?
"""

delete_query = "DELETE FROM QUESTOES WHERE ID = ?"

search_query = """
SELECT * FROM QUESTOES WHERE 
Enunciado LIKE ? OR
Alternativa_A LIKE ? OR
Alternativa_B LIKE ? OR
Alternativa_C LIKE ? OR
Alternativa_D LIKE ? OR
Alternativa_E LIKE ? OR
Alternativa_Correta LIKE ? OR
Explicacao = ?
"""

select_query = f'SELECT * FROM QUESTOES ORDER BY RANDOM() LIMIT 1;'
