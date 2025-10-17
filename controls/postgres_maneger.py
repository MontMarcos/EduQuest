import psycopg2
from typing import List, Dict, Optional
import os
from dotenv import load_dotenv 

load_dotenv()

class PostgresManager:

    def __init__(self):
        self.db_params = {
            "dbname": os.getenv("DB_NAME", "eduquest"),
            "user": os.getenv("DB_USER", "postgres"),
            "password": os.getenv("DB_PASS", ""),
            "host": os.getenv("DB_HOST", "localhost"),
            "port": os.getenv("DB_PORT", "5432")
        }
        self.ensure_table_exists()

    def get_connection(self):
        """Estabelece e retorna uma conexão com o banco de dados."""
        try:
            return psycopg2.connect(**self.db_params)
        except Exception as e:
            print(f"Erro de conexão com o Banco de Dados. Verifique o arquivo .env e o status do seu PostgreSQL. Erro: {e}")
            raise 

    def ensure_table_exists(self):
        """Cria a tabela 'users' se ela não existir."""
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(20) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL
                );
            """)
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao garantir que a tabela exista: {e}") 

    def create_user(self, username: str, password_hash: str) -> bool:
        """Insere um novo usuário no banco de dados."""
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
                (username, password_hash)
            )
            conn.commit()
            cur.close()
            conn.close()
            return True
        except psycopg2.errors.UniqueViolation:
            return False
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            return False

    def read_all_users(self) -> List[Dict[str, str]]:
        """Lê todos os usuários do banco de dados."""
        users = []
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute("SELECT username, password_hash FROM users")
            
            for row in cur.fetchall():
                users.append({"username": row[0], "password": row[1]}) 
            
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao ler usuários: {e}")
            
        return users

    def get_user_by_username(self, username: str) -> Optional[Dict[str, str]]:
        """Recupera os dados de um único usuário pelo nome de usuário."""
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute(
                "SELECT username, password_hash FROM users WHERE username = %s",
                (username,)
            )
            user_data = cur.fetchone()
            cur.close()
            conn.close()
            
            if user_data:
                return {"username": user_data[0], "password": user_data[1]}
            return None

        except Exception as e:
            print(f"Erro ao recuperar usuário: {e}")
            return None