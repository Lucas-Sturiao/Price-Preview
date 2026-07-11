# 📈 Previsão de Preços com Regressão Linear Clássica

Um projeto prático e modular focado nos fundamentos de Engenharia de Dados e Machine Learning Clássico. O objetivo é prever o preço de ativos financeiros com base em indicadores macroeconómicos, aplicando conceitos puros de Álgebra Linear e Estatística.

---

## 🛠️ Pré-requisitos

- **Linguagem:** Python 3.10+
- **Base de Dados e Infraestrutura:** PostgreSQL e Docker Compose
- **Manipulação Numérica e Análise:** Pandas e NumPy
- **Machine Learning e Estatística:** Scikit-Learn e Joblib
- **Visualização de Dados (Notebook):** Matplotlib e Seaborn

---

## 📂 Arquitetura do Projeto

A estrutura foi desenhada para separar o ambiente de experimentação (Jupyter) do código de produção (`src/`).

```text
price_preview/
├── data/
│   ├── raw/                       # Armazenamento de dados brutos (cache/backups)
│   └── processed/                 # Dados após limpeza e transformações
├── notebooks/
│   └── 01_analise_estatistica.ipynb # Exploração estatística, correlações e testes
├── src/
│   ├── database.py                # Camada de ligação ao PostgreSQL (SQLAlchemy)
│   ├── seed_data.py               # Geração de dados históricos baseados em ruído gaussiano
│   ├── data_prep.py               # Limpeza e separação de Matrizes (X e y)
│   ├── train_model.py             # Treinamento da Regressão Linear e métricas
│   └── predict.py                 # Script de inferência utilizando o modelo salvo (.pkl)
├── .env                           # Credenciais locais seguras
├── .gitignore                     # Filtro de versionamento (exclui .env, .pkl e dados grandes)
├── docker-compose.yml             # Orquestração do banco de dados isolado
└── requirements.txt               # Lista de dependências Python
```

---

## ▶️ Como Executar o Projeto

Siga os passos abaixo para testar o pipeline completo na sua máquina.

**1. Clonar o Repositório:**
É necessário ter o git instalado e configurado na sua Máquina:

```bash
git clone https://github.com/lucas-sturiao/price_preview.git
```
```
cd price_preview
```

**2. Subir a Base de Dados (Docker)**
Certifique-se de ter o Docker instalado e inicie o container do PostgreSQL em segundo plano:
```bash
docker compose up -d
```

**3. Instalar Dependências**
Crie um ambiente virtual (opcional, mas recomendado) e instale os pacotes necessários:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**4. Popular a Base de Dados**
Gere os dados sintéticos que simulam um cenário real de mercado (inflação vs. juros vs. preço):
```bash
python src/seed_data.py
```

**5. Treinar o Modelo Preditivo**
Extraia os dados, aplique a regressão e veja os resultados matemáticos e estatísticos (MSE e R²):
```bash
python src/train_model.py
```
*(O modelo será salvo automaticamente como `modelo_precos.pkl` na raiz do projeto).*

**6. Realizar uma Previsão (Inferência)**
Teste o modelo treinado perante novos dados do dia a dia:
```bash
python src/predict.py
```

---

## 📐 Fundamentos Matemáticos

Este projeto se baseia na **Regressão Linear Múltipla**, que resolve a equação matricial:
**y = Xw + b**

Onde:
- **y:** Preço do ativo (Vetor alvo)
- **X:** Matriz de atributos (Inflação, Juros)
- **w:** Pesos dos coeficientes angulares encontrados pelo algoritmo (Equação Normal dos Mínimos Quadrados)
- **b:** Interceção ou viés (Valor base do ativo)

O algoritmo atinge uma precisão estatística elevada (R² > 0.95), validando que a relação económica modelada possui forte correlação linear.

---

## 📌 Melhorias Futuras

Este projeto foi desenhado como a **Fase 1 (Fundamentos e Dados)**. O próximo passo transformará esta base analítica num produto de software completo para o utilizador final.

- [ ] **Integração com API (Fase 2):** Criar uma API utilizando **FastAPI** para receber os parâmetros macroeconómicos em tempo real via formato JSON.
- [ ] **Interface Web para o Utilizador Final:** Desenvolver um dashboard interativo (ex: **Streamlit** ou frontend em React) onde o utilizador não necessite de lidar com o terminal, apenas digitando a inflação e juros num formulário e vendo o preço no ecrã.
- [ ] **Pipeline Avançado de Engenharia de Dados:** Substituir a geração sintética (`seed_data.py`) pela integração de uma API financeira real (ex: Alpha Vantage ou Banco Central) via DAGs do Apache Airflow.
- [ ] **Avaliação de Novos Algoritmos:** Comparar a performance da Regressão Clássica contra modelos não-lineares, como Random Forest Regressor e XGBoost.

---

## 🤝 Contribuições

Contribuições são sempre bem-vindas!

Caso encontre algum problema ou tenha sugestões de melhorias:

1. Faça um Fork do projeto.
2. Crie uma nova Branch.
3. Faça suas alterações.
4. Envie um Pull Request.

Ou entre em contato via *E-mail*: [lucasltstb@gmail.com](mailto:lucasltstb@gmail.com)
