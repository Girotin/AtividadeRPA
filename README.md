# Projeto de Automação: Leitor de Excel para Banco de Dados

Este é um protótipo de automação desenvolvido em Python que lê dados de uma planilha do Excel, realiza uma transformação simples e os armazena em um banco de dados SQLite.

## 🚀 O que o script faz?

1.  **Extração:** Lê os dados do arquivo `PlanilhaTest.xlsx`.
2.  **Transformação:** Calcula uma nova coluna ("Valor Total") com base nos dados existentes.
3.  **Carga:** Salva os dados transformados em uma tabela chamada `vendas` dentro de um banco de dados `meu_banco.db`.
4.  **Verificação:** Lê os dados diretamente do banco recém-criado para confirmar que a operação foi bem-sucedida.

## 🛠️ Stack Tecnológico

* **Linguagem:** Python
* **Editor:** Visual Studio Code (VSCode)
* **Gerenciador de Ambiente:** Venv
* **Bibliotecas Principais:**
    * `pandas`: Para manipulação de dados.
    * `SQLAlchemy`: Para fazer a ponte com o banco de dados.
    * `openpyxl`: Como motor para o pandas ler arquivos `.xlsx`.

## ⚙️ Instruções de Reprodução

Siga os passos abaixo para configurar e executar o projeto em sua máquina.

### 1. Pré-requisitos

* Ter o [Python](https://www.python.org/downloads/) (versão 3.8 ou superior) instalado.
* Ter o [Git](https://git-scm.com/downloads) instalado para clonar o repositório.

### 2. Configuração do Ambiente

```bash
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
