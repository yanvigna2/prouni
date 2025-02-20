import pandas as pd
import mysql.connector


# Código para conexão ao banco MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='prouni_db'
)

cursor = conn.cursor()

# Realizar o carregamento dos dados
df = pd.read_csv("D:/Portifolio DADOS/Projeto PROUNI/data/raw/cursos-prouni.csv")

# Remover duplicatas
df.drop_duplicates(inplace=True)

# Preencher valores nulos com 0 nas colunas númericas 
cols_numericas = ["bolsa_integral_cotas", "bolsa_integral_ampla", "bolsa_parcial_cotas", "bolsa_parcial_ampla", "nota_integral_ampla", 
                  "nota_integral_cotas", "nota_parcial_ampla", "nota_parcial_cotas" ]
df[cols_numericas] = df[cols_numericas].fillna(0)

# Inserção dos dados no banco
colunas_corretas = ["grau", "turno", "mensalidade", "bolsa_integral_cotas", "bolsa_integral_ampla", 
                    "bolsa_parcial_cotas", "bolsa_parcial_ampla", "curso_id", "curso_busca", "cidade_busca", "uf_busca", 
                    "universidade_nome", "campus_nome", "nota_integral_ampla", "nota_integral_cotas", 
                    "nota_parcial_ampla", "nota_parcial_cotas"]

for _, row in df[colunas_corretas].iterrows():
    valores = tuple(None if pd.isna(x) else x for x in row)  # Substitui NaN por None
    cursor.execute("""
        INSERT INTO cursos_prouni (grau, turno, mensalidade, bolsa_integral_cotas, bolsa_integral_ampla, 
        bolsa_parcial_cotas, bolsa_parcial_ampla, curso_id, curso_busca, cidade_busca, uf_busca, universidade_nome, 
        campus_nome, nota_integral_ampla, nota_integral_cotas, nota_parcial_ampla, nota_parcial_cotas)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, valores)

conn.commit()
cursor.close()
conn.close()