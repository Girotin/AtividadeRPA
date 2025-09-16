# Passo 1: Importar as bibliotecas necessárias
import pandas as pd
from sqlalchemy import create_engine # Importamos a função para criar a conexão

# Passo 2: Definir o nome do arquivo que queremos ler
nome_do_arquivo = 'PlanilhaTeste.xlsx'

# Passo 3: Ler a planilha e guardar os dados em um DataFrame
print(f"Lendo o arquivo: {nome_do_arquivo}...")
df = pd.read_excel(nome_do_arquivo)

# Passo 4: Fazer o cálculo da nova coluna
df['Valor Total'] = df['Quantidade'] * df['Preço Unitário']

# --- A MÁGICA DO BANCO DE DADOS COMEÇA AQUI ---

# Passo 5: Definir o nome do nosso banco de dados
# Este será o nome do arquivo que vai aparecer na sua pasta
nome_do_banco = 'meu_banco.db'

# Passo 6: Criar a conexão com o banco de dados
# A string 'sqlite:///' diz para o SQLAlchemy que estamos usando um banco SQLite
# e que o arquivo dele estará na mesma pasta do script.
engine = create_engine(f'sqlite:///{nome_do_banco}')

# Passo 7: Salvar o DataFrame no banco de dados
print(f"Salvando dados no banco de dados: {nome_do_banco}...")
# Usamos a função 'to_sql' do DataFrame para fazer todo o trabalho pesado.
# 'vendas': será o nome da tabela criada dentro do banco de dados.
# engine: é a nossa conexão com o banco.
# if_exists='replace': Se a tabela 'vendas' já existir, ela será apagada e recriada.
#                      Isso é ótimo para testar! (Outra opção é 'append' para adicionar os dados).
# index=False: Para não salvar o índice do DataFrame como uma coluna no banco.
df.to_sql('vendas', engine, if_exists='replace', index=False)

print("Processo concluído com sucesso!")