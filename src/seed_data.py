import numpy as np
import pandas as pd
from database import obter_conexao
from datetime import datetime, timedelta
from sqlalchemy import text

def popular_banco():
    engine = obter_conexao()
    
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS historico_precos (
                id SERIAL PRIMARY KEY,
                data_registo DATE,
                preco_ativo DECIMAL(10, 2),
                taxa_inflacao DECIMAL(5, 4),
                volume_negociado INT,
                taxa_juros DECIMAL(5, 4)
            );
        """))
        conn.commit()

    np.random.seed(42)
    n = 250
    datas = [datetime(2024,1,1) + timedelta(days=i) for i in range(n)]

    taxa_inflacao = np.random.uniform(0.02, 0.07, n)
    taxa_juros = np.random.uniform(0.06, 0.13, n)
    volume_negociado = np.random.randint(1500, 6000, n)

    preco = 120 + (450 * taxa_inflacao) - (180 * taxa_juros) + np.random.normal(0, 1.5, n)

    df = pd.DataFrame({
        'data_registo': datas,
        'preco_ativo': np.round(preco, 2),
        'taxa_inflacao': taxa_inflacao,
        'volume_negociado': volume_negociado,
        'taxa_juros': taxa_juros
    })

    df.to_sql('historico_precos', engine, if_exists='append', index=False)
    print("Base populada com sucesso!")

if __name__ == "__main__":
    popular_banco()