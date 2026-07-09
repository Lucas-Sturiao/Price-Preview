import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def obter_conexao():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    db = os.getenv("POSTGRES_DB")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url)

def carregar_dados():
    engine = obter_conexao()
    query = """
        SELECT preco_ativo, taxa_inflacao, volume_negociado, taxa_juros
        FROM historico_precos;
    """
    return pd.read_sql(query, engine)