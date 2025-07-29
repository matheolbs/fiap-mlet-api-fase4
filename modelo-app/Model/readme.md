# 🔍 Busca de Hiperparâmetros para Previsão com LSTM

Este notebook tem como **objetivo automatizar a busca pelos melhores hiperparâmetros** para um modelo de previsão de séries temporais baseado em LSTM. Ele **não representa a versão final do modelo**, mas sim uma ferramenta auxiliar para **testar diferentes configurações e comparar o desempenho via MAPE**.

---

## 📌 Objetivo

- Testar automaticamente diferentes **combinações de hiperparâmetros**.
- Avaliar o desempenho de cada configuração usando a métrica **MAPE (Mean Absolute Percentage Error)**.
- Identificar a melhor configuração para ser aplicada no **modelo definitivo**, implementado em outro arquivo.

> ⚠️ **Nota:** O modelo final de previsão com LSTM está em outro arquivo/script. Este notebook serve exclusivamente para suporte à etapa de **tuning de parâmetros**.

---

## ⚙️ O que o notebook faz

1. **Baixa os dados históricos** de uma ação (default: `AAPL`) usando `yfinance`.
2. Aplica pré-processamento e normalização.
3. Gera subconjuntos de treino/teste baseados em janelas de tempo.
4. Para cada execução:
   - Gera uma configuração aleatória de hiperparâmetros.
   - Treina um modelo LSTM simples.
   - Avalia o desempenho com base no **MAPE**.
5. Ao final, imprime a **melhor configuração** testada.

---

## 🧪 Hiperparâmetros testados aleatoriamente

| Parâmetro       | Valores testados             |
|------------------|------------------------------|
| `time_step`      | 30, 60, 90                   |
| `lstm_units`     | 50, 64, 100, 128             |
| `dropout`        | 0.1, 0.2, 0.3, 0.5           |
| `batch_size`     | 16, 32, 64                   |
| `learning_rate`  | 0.001, 0.0005, 0.0001        |

> Número de combinações testadas definido por `n_iter`.

---

## 🧠 Tecnologias e Bibliotecas

- Python 3.x
- NumPy, Pandas
- yFinance
- Scikit-learn
- TensorFlow / Keras

Instalação:

```bash
pip install numpy pandas yfinance scikit-learn tensorflow