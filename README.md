Projeto de Automação: Leitor de Excel para Banco de Dados
Este é um protótipo de automação desenvolvido em Python que lê dados de uma planilha do Excel, realiza uma transformação simples e os armazena em um banco de dados SQLite.

🚀 O que o script faz?
Extração: Lê os dados do arquivo PlanilhaTest.xlsx.

Transformação: Calcula uma nova coluna ("Valor Total") com base nos dados existentes.

Carga: Salva os dados transformados em uma tabela chamada vendas dentro de um banco de dados meu_banco.db.

Verificação: Lê os dados diretamente do banco recém-criado para confirmar que a operação foi bem-sucedida.

🛠️ Stack Tecnológico
Linguagem: Python

Editor: Visual Studio Code (VSCode)

Gerenciador de Ambiente: Venv

Bibliotecas Principais:

pandas: Para manipulação de dados.

SQLAlchemy: Para fazer a ponte com o banco de dados.

openpyxl: Como motor para o pandas ler arquivos .xlsx.

⚙️ Instruções de Reprodução
Siga os passos abaixo para configurar e executar o projeto em sua máquina.

1. Pré-requisitos
Ter o Python (versão 3.8 ou superior) instalado.

Ter o Git instalado para clonar o repositório.

2. Preparando os Arquivos
Antes de tudo, precisamos listar nossas dependências. No seu terminal, com o ambiente virtual ativado, rode o comando abaixo. Ele criará um arquivo que lista todas as bibliotecas que o projeto precisa.

Bash

pip freeze > requirements.txt
Agora, adicione e "commite" os seguintes arquivos no seu repositório Git:

ler_planilha.py (nosso script principal)

PlanilhaTest.xlsx (nossa planilha de dados)

requirements.txt (o arquivo que acabamos de criar)

3. Configuração do Ambiente
Bash

# 1. Clone o repositório para a sua máquina local
git clone <URL_DO_SEU_REPOSITORIO_GIT>

# 2. Navegue para a pasta do projeto
cd <NOME_DA_PASTA_DO_PROJETO>

# 3. Crie um ambiente virtual chamado 'venv'
python -m venv venv

# 4. Ative o ambiente virtual
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
4. Instalação das Dependências
Com o ambiente virtual ativado, instale todas as bibliotecas necessárias de uma só vez usando o arquivo requirements.txt.

Bash

pip install -r requirements.txt
5. Executando a Automação
Agora que tudo está configurado, basta rodar o script principal.

Bash

python ler_planilha.py
