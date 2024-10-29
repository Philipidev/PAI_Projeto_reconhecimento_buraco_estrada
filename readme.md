# PAI_Projeto_reconhecimento_buraco_estrada

Este projeto faz parte de um trabalho prático da disciplina de Processamento e Análise de Imagens, alinhado com o **Plano Brasileiro de Inteligência Artificial (PBIA) 2024-2028**. O objetivo é desenvolver uma aplicação de **processamento de imagens** com **aprendizado de máquina** para reconhecer buracos em estradas, buscando solucionar total ou parcialmente problemas práticos no Brasil. A aplicação utiliza técnicas de redes neurais e processamento de imagens para identificar e avaliar buracos em fotos de estradas.

## Estrutura do Projeto

```plaintext
PAI_Projeto_reconhecimento_buraco_estrada
│
└───WebScraper
    │   readme.md
    │   requirements.txt
    │   scraper.py
    │
    └───chromeDriver
            chromedriver.exe
            LICENSE.chromedriver
            THIRD_PARTY_NOTICES.chromedriver
```

### Descrição das Pastas

- **WebScraper**: Contém o código para coleta de imagens de buracos de estrada usando Selenium e `requests`. Essas imagens serão utilizadas para treinamento e validação do modelo de IA.
- **chromeDriver**: Contém o `chromedriver.exe` e arquivos de licença, necessários para rodar o Selenium no ambiente do projeto.

## Fases do Projeto

### Fase 1: Coleta de Dados com Web Scraping
A primeira etapa do projeto envolve a coleta de imagens de buracos em estradas. Utilizamos o Selenium para navegar em um site de imagens e coletar automaticamente fotos que serão utilizadas para treinar o modelo de IA.

**Arquivos principais**:
- **scraper.py**: Script principal para coleta de imagens, configurado para baixar imagens de buracos em estradas de um site específico.
- **requirements.txt**: Lista das dependências necessárias para rodar o scraper.
- **chromeDriver**: Inclui o `chromedriver.exe`, necessário para o Selenium funcionar.

### Fase 2: Pré-processamento e Validação das Imagens
Depois de coletar as imagens, será necessário realizar uma etapa de pré-processamento. Isso inclui:
- Remover imagens que não correspondem ao tema (buracos de estrada).
- Realizar ajustes de brilho, contraste, redimensionamento, e possíveis rotações para padronizar os dados.

### Fase 3: Treinamento do Modelo de IA
Nesta fase, o objetivo é treinar uma rede neural para reconhecer buracos nas imagens coletadas. Os passos para essa fase incluem:
- **Aumento Artificial de Dados** (Data Augmentation): Aplicar técnicas de transformação nas imagens (espelhamento, rotação, etc.) para aumentar a base de dados de treinamento.
- **Divisão dos Dados**: Separar os dados em conjuntos de treinamento, validação e teste.
- **Treinamento do Modelo**: Implementar uma rede neural (ou outro método de aprendizado de máquina) para treinar o modelo com as imagens pré-processadas.
- **Avaliação de Overfitting**: Monitorar e ajustar o modelo para evitar overfitting.
- **Análise de Desempenho**: Avaliar o desempenho do modelo no conjunto de testes.

### Fase 4: Documentação e Apresentação
- **Documentação do Código**: Produzir um vídeo explicativo sobre o código, incluindo o processo de treinamento e análise de desempenho do modelo.
- **Apresentação Prática**: Apresentar os resultados em sala de aula, abordando o problema, a solução adotada e os resultados obtidos.

## Requisitos do Trabalho

### Objetivos
- Aplicar técnicas de processamento de imagens para resolver ou atenuar problemas práticos no Brasil.
- Desenvolver uma solução em IA com redes neurais para detecção de buracos em estradas, ajudando a priorizar a manutenção.

### Requisitos Técnicos
- **Definir a base de dados**: Implementar um mecanismo para coleta de imagens (já abordado com o WebScraper).
- **Data Augmentation**: Aumentar artificialmente o conjunto de dados.
- **Separação dos Dados**: Dividir em conjuntos de treino, validação e teste.
- **Treinamento do Modelo**: Utilizar redes neurais para treinamento.
- **Avaliação de Overfitting** e **Análise de Desempenho**: Ajustar e analisar o modelo com base nos conjuntos de dados.

### Requisitos de Apresentação
- **Vídeo Documentação**: Explicar o código e o processo de desenvolvimento.
- **Apresentação Prática**: Demonstração da solução e dos resultados obtidos.

## Execução do Web Scraper

Para executar o WebScraper, siga os passos abaixo:

1. **Instale as dependências**: No diretório `WebScraper`, execute:
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute o script**:
   ```bash
   python scraper.py
   ```
   As imagens serão baixadas para a pasta `imagens_buracos` automaticamente.

## Próximos Passos

Após a coleta e pré-processamento das imagens, o próximo passo é iniciar o treinamento da rede neural, seguindo os requisitos especificados para o trabalho prático.

---

Este `README.md` serve como documentação inicial do projeto, fornecendo uma visão geral da estrutura, objetivos e etapas planejadas para o desenvolvimento da solução.
```

### Explicação do `README.md`

Esse arquivo fornece:
- **Visão Geral do Projeto**: Introduz o objetivo e alinhamento do projeto com o PBIA.
- **Estrutura do Projeto**: Descrição da organização das pastas e arquivos.
- **Fases do Projeto**: Divide o projeto em etapas claras, incluindo a coleta de dados, pré-processamento, treinamento do modelo e documentação.
- **Requisitos do Trabalho**: Lista os requisitos específicos do trabalho prático, de acordo com o enunciado fornecido.
- **Instruções de Execução**: Passos para rodar o WebScraper.
- **Próximos Passos**: Direcionamento para a continuidade do projeto após a coleta de dados.