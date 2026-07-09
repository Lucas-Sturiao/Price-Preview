from database import carregar_dados
from data_prep import preparar_dados
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def executar_treinamento():
    df = carregar_dados()
    X, y = preparar_dados(df)

    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = LinearRegression()
    modelo.fit(X_treino, y_treino)

    previsoes = modelo.predict(X_teste)

    joblib.dump(modelo, 'modelo_precos.pkl')

    mse = mean_squared_error(y_teste, previsoes)
    r2 = r2_score(y_teste, previsoes)

    print("--- RESULTADOS DO MODELO ---")
    print(f"Pesos Modelares (w): {modelo.coef_}")
    print(f"Interceção (b): {modelo.intercept_:.4f}")
    print(f"Erro Quadrático (MSE): {mse:.4f}")
    print(f"R-Quadrado (R2): {r2:.4f}")

if __name__ == "__main__":
    executar_treinamento()