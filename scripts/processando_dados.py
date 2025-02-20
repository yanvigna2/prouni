import pandas as pd
import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='prouni_db'
)

query = "SELECT * FROM cursos_prouni"
df = pd.read_sql(query, conn)

# Só verificando se há valores nulos na base do banco de dados
print(df.isnull().sum())



conn.close()