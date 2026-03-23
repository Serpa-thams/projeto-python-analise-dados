import pandas as pd

df = pd.read_excel("fluxo_caixa.xlsx", header=1)

df["Categoria"] = df["Categoria"].str.strip().str.upper()
df = df[df["Categoria"] != "PAGAMENTO DE FATURA"]

df["valor"] = df["Valor recebido"].fillna(0) - df["Valor pago"].fillna(0)

total_receitas = df[df["valor"] > 0]["valor"].sum()
total_despesas = df[df["valor"] < 0]["valor"].sum()
saldo = df["valor"].sum()

print(f"Total receitas: R$ {total_receitas:.2f}")
print(f"Total despesas: R$ {total_despesas:.2f}")
print(f"Saldo final: R$ {saldo:.2f}")

total_por_categoria = df.groupby("Categoria")["valor"].sum().sort_values()

print("\nTotal por categoria:")
print(total_por_categoria)

top_despesas = total_por_categoria.head(5)
top_receitas = total_por_categoria.tail(5)

print("\nTop 5 maiores despesas:")
print(top_despesas)

print("\nTop 5 receitas:")
print(top_receitas)