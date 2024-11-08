# Hapolo Backend

Um backend simples rodando em Python com SQLAlchemy para interagir com um banco de dados MySQL.
A aplicação roda inteiramente em linha de comando.

## Instalação

Lembre-se de ter o Python instalado em sua máquina e também o MySQL.

Clone o repositório do Hapolo Backend:

```bash
git clone https://github.com/dryingcore/hapolo_backend.git && cd hapolo_backend
```

Crie o arquivo .env e adicione as informações do seu banco de dados.
Rode essa query no banco para criar a tabela de usuários:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
```



Para instalar o Hapolo Backend, siga as instruções abaixo:

```bash
pip install -r requirements.txt
```

## Execução

Para executar o Hapolo Backend, siga as instruções abaixo:

```bash
python main.py
```

