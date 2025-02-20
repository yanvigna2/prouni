import pandas as pd

df = pd.read_csv("D:/Portifolio DADOS/Projeto PROUNI/data/processed/cursos_prouni_limpo.csv")

df = df[df['mensalidade'] > 0]

df["categoria_nota"] = pd.cut(df['nota_integral_ampla'], bins=[0, 450, 600 , 750, 900], labels=["Baixa", "Media", "Alta", "Muito Alta"])

df.to_csv("D:/Portifolio DADOS/Projeto PROUNI/data/processed/cursos_prouni_transformado.csv", index=False)