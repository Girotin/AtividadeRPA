# Passo 1: Importar a biblioteca Pandas
# A gente dá um "apelido" de 'pd' pra ela, que é um padrão na comunidade Python.
import pandas as pd

# Passo 2: Definir o nome do arquivo que queremos ler
# Como o script e a planilha estão na mesma pasta, só o nome já basta.
nome_do_arquivo = 'PlanilhaTeste.xlsx'

# Passo 3: Ler a planilha e guardar os dados
# Usamos a função 'read_excel' do pandas para ler o arquivo.
# O pandas vai guardar todos os dados da planilha em uma variável.
# Essa variável, que chamamos de 'df', é um objeto especial chamado DataFrame.
# Pense no DataFrame como uma tabela em memória, super poderosa.
print(f"Lendo o arquivo: {nome_do_arquivo}...")
df = pd.read_excel(nome_do_arquivo)

# Passo 4: Mostrar os dados na tela
# Agora que os dados estão no nosso DataFrame 'df', podemos simplesmente
# usar a função 'print()' para ver o que tem dentro dele.
print("\nPlanilha lida com sucesso! Aqui estão os dados:")
print(df)

# Bônus: Fazer um cálculo simples com os dados
# O Pandas torna muito fácil criar novas colunas.
# Vamos calcular o 'Valor Total' de cada linha (Quantidade * Preço Unitário)
df['Valor Total'] = df['Quantidade'] * df['Preço Unitário']

# Mostrando a tabela de novo, agora com a coluna nova
print("\nBônus: Tabela com o cálculo do Valor Total:")
print(df)