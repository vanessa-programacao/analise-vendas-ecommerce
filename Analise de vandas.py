import pandas as pd
import matplotlib.pyplot as plt

# Função 1: Carregamento e limpeza dos dados
def carregar_dados(caminho):
    df = pd.read_csv(caminho, sep=';')
    df.columns = df.columns.str.strip()
    return df

# Função 2: Conversão da coluna de datas
def converter_datas(df):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df

# Função 3: Produtos mais vendidos
def produtos_mais_vendidos(df):
    produtos = df.groupby('Product Category')['Quantity'].sum().sort_values(ascending=False)
    produtos.plot(kind='bar', title='Produtos mais vendidos', figsize=(10,5), color='orange')
    plt.xlabel('Categoria de Produto')
    plt.ylabel('Quantidade Vendida')
    plt.tight_layout()
    plt.show()

# Função 4: Categorias mais lucrativas
def categorias_mais_lucrativas(df):
    lucro = df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False)
    lucro.plot(kind='bar', title='Categorias mais lucrativas', figsize=(10,5), color='green')
    plt.xlabel('Categoria de Produto')
    plt.ylabel('Faturamento Total')
    plt.tight_layout()
    plt.show()

# Função 5: Perfil dos clientes
def perfil_clientes(df):
    genero = df['Gender'].value_counts()
    idade = df['Age']

    plt.figure(figsize=(12,5))

    plt.subplot(1,2,1)
    genero.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightpink'])
    plt.title('Distribuição por Gênero')
    plt.ylabel('')

    plt.subplot(1,2,2)
    plt.hist(idade, bins=10, color='gray', edgecolor='black')
    plt.title('Distribuição de Idade dos Clientes')
    plt.xlabel('Idade')
    plt.ylabel('Frequência')

    plt.tight_layout()
    plt.show()

# Função 6: Variação de vendas por mês
def vendas_por_mes(df):
    df['AnoMes'] = df['Date'].dt.to_period('M')
    vendas = df.groupby('AnoMes')['Total Amount'].sum()
    vendas.plot(kind='line', marker='o', title='Vendas por Mês', figsize=(10,5), color='purple')
    plt.xlabel('Mês')
    plt.ylabel('Total Vendido')
    plt.tight_layout()
    plt.show()

# Função 7: Valor médio de compra por cliente
def ticket_medio(df):
    ticket = df.groupby('Customer ID')['Total Amount'].mean().sort_values(ascending=False)
    print("\nTop 10 clientes com maior ticket médio:")
    print(ticket.head(10))

    plt.figure(figsize=(10,5))
    ticket.head(10).plot(kind='bar', color='skyblue')
    plt.title('Top 10 Clientes com Maior Ticket Médio')
    plt.xlabel('Customer ID')
    plt.ylabel('Ticket Médio')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Função 8: Exportar os dados tratados para CSV
def exportar_csv(df, caminho_saida):
    df.to_csv(caminho_saida, index=False)
    print(f"\n Arquivo CSV exportado com sucesso para:\n{caminho_saida}")

# Execução do script
if __name__ == "__main__":
    caminho = r"C:\Users\Vanessa\Desktop\analise-vendas-ecommerce\Analise de vendas.csv"
    df = carregar_dados(caminho)
    df = converter_datas(df)

    produtos_mais_vendidos(df)
    categorias_mais_lucrativas(df)
    perfil_clientes(df)
    vendas_por_mes(df)
    ticket_medio(df)

    # Exporta o DataFrame final tratado
    saida_csv = r"C:\Users\Vanessa\Desktop\analise-vendas-ecommerce\Analise de vendas pronta.csv"
    exportar_csv(df, saida_csv)

    import pandas as pd
    df.to_csv('vendas_processadas.csv', index=False)
    print("Arquivo CSV exportado com sucesso!")

