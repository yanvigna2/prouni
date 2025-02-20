-- Active: 1739473433283@@127.0.0.1@3306@prouni_db

# 1. Verificação estados com mais bolsas
SELECT uf_busca, COUNT(*) AS total_bolsas
FROM cursos_prouni
GROUP BY uf_busca
ORDER BY total_bolsas DESC;

# 2. Cursos com maior nota de corte

SELECT curso_busca, AVG(nota_integral_ampla) AS media_nota
FROM cursos_prouni
GROUP BY curso_busca
ORDER BY media_nota DESC
LIMIT 10;