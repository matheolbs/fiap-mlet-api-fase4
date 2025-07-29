# fiap-mlet-api-fase4

## Visão Geral

Este projeto faz parte da entrega da disciplina de Machine Learning Engineering da FIAP, com o objetivo de construir, treinar e disponibilizar uma API para predição de séries temporais utilizando redes neurais LSTM (Long Short-Term Memory). O foco principal está na construção do modelo, desde a preparação dos dados até a implementação e disponibilização do modelo treinado.

## Estrutura do Projeto

```plaintext
fiap-mlet-api-fase4/
│
├── modelo-app/
│   ├── Model/
│   │   ├── busca_hiperparametros_lstm.ipynb
│   │   └── lstm.ipynb
│   └── src/
│       ├── Dockerfile
│       ├── modelo_lstm_acao.h5
│       ├── requirements.txt
│       └── run.py
├── .gitignore
└── README.md
```

- **Model/**: Notebooks de desenvolvimento e experimentação do modelo LSTM.  
- **src/**: Código fonte da API, modelo treinado, dependências e Dockerfile para deploy.


## Construção do Modelo

1. Preparação dos Dados
A preparação dos dados foi realizada nos notebooks presentes em Model/. Os dados foram tratados, normalizados e estruturados em janelas temporais para alimentar a rede LSTM, que é especialmente eficaz para problemas de séries temporais devido à sua capacidade de capturar dependências de longo prazo.

2. Busca de Hiperparâmetros
O notebook busca_hiperparametros_lstm.ipynb explora diferentes configurações de hiperparâmetros, como número de camadas, unidades LSTM, taxa de aprendizado e batch size, utilizando técnicas de validação cruzada para encontrar a melhor combinação para o problema.

3. Treinamento do Modelo
O notebook lstm.ipynb contém o pipeline de treinamento do modelo LSTM, incluindo:
Definição da arquitetura da rede (camadas LSTM, Dropout, Dense).
Compilação do modelo com função de perda adequada (ex: MSE) e otimizador (ex: Adam).
Treinamento e avaliação do desempenho em dados de validação.
Salvamento do modelo treinado em modelo_lstm_acao.h5.

4. Disponibilização via API
O arquivo run.py implementa uma API (por exemplo, usando Flask ou FastAPI) que carrega o modelo treinado e expõe endpoints para receber dados de entrada e retornar previsões. O deploy pode ser realizado via Docker, conforme especificado no Dockerfile.


## Como Executar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute a API:**
   ```bash
   python run.py
   ```

3. **Deploy via Docker:**
   ```bash
   docker build -t fiap-mlet-api-fase4 .
   docker run -p 5000:5000 fiap-mlet-api-fase4
   ```

---

## Considerações Finais

O projeto demonstra a aplicação prática de técnicas de Deep Learning para previsão de séries temporais, desde a experimentação e ajuste do modelo até a entrega de uma solução pronta para produção. O uso de LSTM foi motivado pela sua robustez em capturar padrões temporais complexos, tornando-o adequado para aplicações financeiras, previsão de demanda, entre outros cenários.