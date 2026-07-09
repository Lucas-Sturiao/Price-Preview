import pandas as pd

def preparar_dados(df):
    df = df.dropna()

    X = df[['taxa_inflacao', 'volume_negociado', 'taxa_juros']]
    y = df['preco_ativo']

    return X, y