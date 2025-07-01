import fdb
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

def conectar_banco():
    """
    Conecta ao banco de dados Firebird usando credenciais do arquivo .env.
    Retorna uma conexão ativa ou levanta uma exceção se houver erro.
    """
    try:
        # Caminho da DLL do Firebird (fbclient.dll)
        os.environ["FIREBIRD"] = os.getenv("FIREBIRD_PATH")

        # Criar conexão com o banco
        con = fdb.connect(
            dsn=os.getenv("FIREBIRD_DSN"),
            user=os.getenv("FIREBIRD_USER"),
            password=os.getenv("FIREBIRD_PASSWORD"),
            charset='UTF8'
        )
        return con

    except Exception as e:
        print("Erro ao conectar ao banco de dados:")
        print(e)
        raise
