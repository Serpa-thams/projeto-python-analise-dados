import pandas as pd

# Ler o Excel usando a primeira linha como cabeçalho
df = pd.read_excel("fluxo_caixa.xlsx", header=1)

# Mostrar as primeiras linhas
print(df.head())

print(df.columns)

# Padronizar texto da categoria
df["Categoria"] = df["Categoria"].str.strip().str.upper()

# Remover pagamentos de fatura
df = df[df["Categoria"] != "PAGAMENTO DE FATURA"]

# Verificar se funcionou
print(df["Categoria"].unique())

# Criar coluna valor
df["valor"] = df["Valor recebido"].fillna(0) - df["Valor pago"].fillna(0)

# Mostrar resultado
print(df[["Valor recebido", "Valor pago", "valor"]].head())

# Total de receitas (valores positivos)
total_receitas = df[df["valor"] > 0]["valor"].sum()

# Total de despesas (valores negativos)
total_despesas = df[df["valor"] < 0]["valor"].sum()

# Saldo final
saldo = df["valor"].sum()

print("Total receitas: R$", round(total_receitas, 2))
print("Total despesas: R$", round(total_despesas, 2))
print("Saldo final: R$", round(saldo, 2))

# Agrupar por categoria
total_por_categoria = df.groupby("Categoria")["valor"].sum()

# Ordenar do maior gasto para o menor
total_por_categoria = total_por_categoria.sort_values()

print(total_por_categoria)

# Top 5 maiores despesas
top_despesas = total_por_categoria.head(5)

print("\nTop 5 maiores despesas:")
print(top_despesas)

# Top 5 receitas
top_receitas = total_por_categoria.tail(5)

print("\nTop 5 receitas:")
print(top_receitas)