# ETL-Fake-Products

📌 Descrição
Este projeto implementa um pipeline de **ETL (Extract, Transform, Load)** para gerar e processar dados de produtos fictícios da API Fake Products.  
Ele tem como objetivo demonstrar uma arquitetura de ETL modular, com extração, transformação e carga em um **banco de dados PostgreSQL**.

### Este projeto requer um banco de dados **PostgreSQL** ativo para que a etapa de carga (Load) funcione corretamente. O pipeline ETL se conecta ao banco, insere os dados processados e depende das credenciais e da estrutura de tabelas configuradas previamente.
### Instale o PostgreSql em sua maquina, selecionando a versão 17.x.
[PostgreSQL Downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
Após a instalação, crie o banco de dados e a tabela de destino, e configure corretamente usuário, senha e porta de acesso no arquivo `config/db_connection.py` do projeto.


## Principais módulos

| Módulo        | Responsabilidade |
|----------------|-------------------|
| `extract_data.py`   | extrair dados de fonte (API).                     |
| `transform_data.py` | realizar limpeza, mapeamentos, regras de negócio. |
| `load.py`      | gravar os dados transformados no sistema destino.      |
| `config/`      | configurações de conexão com o Banco de Dados.         |
| `main.py`      | Orquestração das operações de ETL.                     |
| `tables/`      | scripts SQL / definição de tabelas usadas no Banco.    |

## 🛠️ Tecnologias / Dependências

- Python 3.13 
- Pandas 2.3.1
- Bibliotecas de acesso a banco: psycopg2 2.9.10
- Requests / HTTP client  
- Outras bibliotecas conforme `requirements.txt`


## 🚀 Como rodar

### 1. Clonar o repositório

```bash
git clone https://github.com/Ryangustv/ETL-Fake-Products.git
cd ETL-Fake-Products
```

### 2. Criar ambiente virtual
``` bash
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux / macOS
source venv/bin/activate
```

### 3. Instalar dependências
`pip install -r requirements.txt`

### 4. Após a instalação:
  1. Crie um novo banco de dados.
  2. Execute o script SQL `tables/promocao.sql` para criar a tabela de destino.
  3. Configure usuário, senha, host e porta no arquivo `config/db_connection.py`.

### 5. Rodando o projeto.
`python main.py`
