import joblib
import pandas as pd

def executar_inferencia(inflacao, volume, juros):
    modelo = joblib.load('modelo_precos.pkl')
    
    novos_dados = pd.DataFrame({
        'taxa_inflacao': [inflacao],
        'volume_negociado': [volume],
        'taxa_juros': [juros]
    })
    
    preco_previsto = modelo.predict(novos_dados)[0]
    
    print(f"Parâmetros Inseridos -> Inflação: {inflacao}, Volume: {volume}, Juros: {juros}")
    print(f"Preço Previsto do Ativo: {preco_previsto:.2f}")

if __name__ == "__main__":
    executar_inferencia(inflacao=0.045, volume=3500, juros=0.09)